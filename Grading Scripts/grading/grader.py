import os
import pandas as pd
import scrape_utils
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm
from getpass import getpass

def scrape_grades(admin_username, admin_password, filename="raw_grades.csv", slugs=scrape_utils.SLUGS, destination=os.getcwd(), headless=False):
    admin_password = getpass()
    """Scrape scores from each requested assignment. The grades are saved in a
    raw data file. Before these grades can be uploaded to LearningSuite, they
    must be converted using the grade.py file.

    Note that this scraper assumes that each assignment is set up to use the
    Default HackerRank Leaderboard. If the assignment uses the ACM Style
    Leaderboard, the scraper will crash. If an ACM leaderboard is absolutely
    necessary, functionality will need to be added to this scraper.

    Parameters:
        admin_username (str) : The username associated with a hackerrank
                               account with either moderator/administrator
                               privileges for the desired assignments, or has
                               signed up for each assignment. The username and
                               password will be used to sign in to hackerrank
                               on a selenium browser.
        admin_password (str) : The password associated with a hackerrank
                               account with either moderator/administrator
                               privileges for the desired assignments, or has
                               signed up for each assignment.
        filename (str)       : The name of the file the data will be saved to.
                               This file will be saved in the destination
                               directory, provided by the user through the
                               destination parameter.
        slugs (list)         : A list of slugs pertaining to the assignments that
                               are to be scraped. Slugs are the last part of the
                               URL for the assignment (as in
                               hackerrank.com/<slug>). Default is the list of
                               slugs provided in the source file.
        destination (str)    : The direcory in which the file will be saved.
                               Default value is the current working directory
                               if no value is provided.
        headless (bool)      : Whether or not the browser will run in 'headless'
                               mode. If set to True, the browser will not be
                               visible while it is running. Default value is
                               True."""
    # URLs for quick navigation.
    base_url = "https://www.hackerrank.com"
    leaderboard_url_template = "https://www.hackerrank.com/{}/leaderboard"

    # Open a selenium driver. Selenium is used because we need to be signed in
    # to a HackerRank account to see the assignment results.
    browser = scrape_utils.init_browser(headless=headless)
    print("Opened selenium")

    try:
        # Login to hackerrank.
        scrape_utils.hackerrank_login(browser, admin_username, admin_password)
        print("Opened hackerrank")

        # The grades will be stored in a data frame, indexed by student's
        # HackerRank id, and with columns being the assignment slugs.
        grades = pd.DataFrame(columns=slugs)

        data = pd.DataFrame()

        # Visit each assignment leaderboard and scrape the data.
        for slug in tqdm(slugs):
            time.sleep(1)
            browser.get(leaderboard_url_template.format(slug))
            column = pd.Series()
            # Loop through each page.
            while True:
                scrape_utils.wait_for_load(browser, "browser.find_element_by_id('leaders')")
                # Get all leaders from the leaderboard and loop through them to
                # extract the data desired.
                soup = BeautifulSoup(browser.page_source, "html.parser")
                leaders = soup.find("div", id="leaders")
                for leader in leaders.find_all("div", class_="leaderboard-list-view"):
                    user_name = leader.find("div", class_="span-flex-4").text.strip()
                    score = leader.find("div", class_="span-flex-3").text.strip()
                    # column.set_value(user_name, score)
                    column.at[user_name] = score
                # Get next page.
                button = soup.find("a", class_="backbone", attrs={"data-attr1" : "Right"})
                # If we couldn't find a button, we break the loop.
                if button is None:
                    break
                time.sleep(1)
                browser.get(base_url + button['href'])

            column.name = slug
            data = data.append(column)

        # Flip the data to place the students as the index.
        data = data.transpose()
        data.index.name = "hackerrank_id"
        if not os.path.exists(destination):
            os.makedirs(destination)
        data.to_csv(os.path.join(destination, filename))
    finally:
        browser.close()

def clean_grades(info_file=os.path.join(os.getcwd(), "student_info.csv"), grades_file=os.path.join(os.getcwd(), "raw_grades.csv"), destination_file=os.path.join(os.getcwd(), 'grades.csv'),
slugs=scrape_utils.SLUGS):
    """Clean the raw grades after they have been scraped. This function
    requires a student info file, containing information about students,
    specifically Net ID, associated hackerrank_id, and Hours (as in, credit
    hours). The actual scores for each assignment are calculated, and the
    cleaned file is saved as a new CSV file.

    Parameters:
        info_file (str)             : The path to the file with all of the
                                      student info. This file should be a CSV
                                      with three columns: one for Net ID, one
                                      for hackerrank_id, and one for Hours.
        grades_file (str)           : The path to the file containing the raw
                                      grades scraped from hackerrank. This file
                                      should be a CSV with columns for
                                      hackerrank_id and the assignment scores
                                      (named by their respective slugs).
        destination_file (str)      : The path to the file where the cleaned
                                      grades should be saved. These grades will
                                      be saved as a CSV file."""
    info = pd.read_csv(info_file)
    info.set_index("hackerrank_id", inplace=True)
    grades = pd.read_csv(grades_file)
    grades.set_index("hackerrank_id", inplace=True)
    combined = pd.concat([info, grades], axis=1, sort=False)
    for slug in tqdm(slugs):
        if slug in combined.columns:
            combined[slug] = (combined[slug] / (combined['Hours'] * 10)).clip(upper=1) * 20
    combined.set_index("Net ID", inplace=True)
    combined.drop(columns=["Hours"], inplace=True)
    combined.fillna(0, inplace=True)
    combined.to_csv(destination_file)

def grader(admin_username, admin_password='', filename="grades.csv", slugs=scrape_utils.SLUGS, directory=os.getcwd(), info_file=os.path.join(os.getcwd(), "student_info.csv"), keep_raw=False):
    print("##### Scraping Grades #####")
    scrape_grades(admin_username, admin_password, slugs=slugs, destination=directory)
    print("##### Cleaning Grades #####")
    clean_grades(info_file=info_file, grades_file=os.path.join(directory, 'raw_grades.csv'), destination_file=os.path.join(directory, filename))
    # Clean up the temporary file
    if not keep_raw:
        os.remove(os.path.join(directory, 'raw_grades.csv'))
