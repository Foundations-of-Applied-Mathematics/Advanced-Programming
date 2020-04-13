import os
import re
import scrape_utils
import time
import pdb

from bs4 import BeautifulSoup
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm

def scrape_submissions(admin_username, admin_password, destination=os.path.join(os.getcwd(), "submissions"), slugs=scrape_utils.SLUGS):
    """Scrape and save all student submissions for each given assignment.
    Assignments are identified by their slugs. Slugs are the last part of the
    URL for the assignment (as in hackerrank.com/<slug>).

    Parameters:
        admin_username(str) : The username associated with an hackerrank
                              account with admin priveleges for the contests
                              desired. The username and password will be used
                              to sign in to hackerrank on a selenium browser.
                              This is required for access to contest
                              submissions.
        admin_password(str) : The password associated with an hackerrank
                              account with admin priveleges for the contests
                              desired.
        destination (str)   : Destination directory to save the files. Files
                              will be saved in subdirectories by assignment
                              slug, in files with hackerrank ids as names.
                              Default is to create a new folder called
                              'submissions' in the current working directory.
        slugs (list)        : A list of slugs pertaining to the assignments that
                              are to be scraped. Slugs are the last part of the
                              URL for the assignment (as in
                              hackerrank.com/<slug>). Default is the list of
                              slugs provided in the source file.
    """
    # URLs for quick navigation.
    base_url = "https://www.hackerrank.com/"
    submissions_url = "https://www.hackerrank.com/contests/{}/judge/submissions/challenge"

    # Regular expressions.
    problem_slug_finder = re.compile(r".*/challenge/(.*)$")

    # Open a selenium driver. Selenium is used because code from submissions is
    # loaded through JavaScript.
    browser = scrape_utils.init_browser()

    try:
        # Login to hackerrank.
        scrape_utils.hackerrank_login(browser, admin_username, admin_password)

        # Get submissions for each slug.
        tqdm_slugs = tqdm(slugs)
        for slug in tqdm_slugs:
            # Here we first get all of the URLs for each slug's submissions.
            # They are stored in a dictionary, keyed by problem name.
            urls = defaultdict(list)
            time.sleep(1)
            browser.get(submissions_url.format(slug))

            tqdm_slugs.set_description_str("Gathering submission URLs")

            # Loop through every page.
            while True:
                # Wait for the page to load.
                scrape_utils.wait_for_load(browser, "browser.find_element_by_xpath(\"//div[@class='table-wrap']\")")
                soup = BeautifulSoup(browser.page_source, "html.parser")
                # Get submissions from page source.
                submissions = soup.find("div", class_="table-body").find_all("div", class_="judge-submissions-list-view")
                for submission in submissions:
                    # Only get the source if the submission was accepted.
                    if submission.find(class_='span3') is not None and submission.find(class_='span3').text.strip() == "Accepted":
                        urls[problem_slug_finder.findall(submission.find(class_="span2").a['href'])[0]].append(submission.find(class_="view-results")['href'])
                # Go to the next page.
                button = soup.find("a", class_="backbone", attrs={"data-attr1" : "Right"})
                # If we couldn't find a button, we break the loop.
                if button is None:
                    break
                time.sleep(1)
                browser.get(base_url + button['href'])

            tqdm_slugs.set_description_str("")

            # Scrape every submission from the gathered list.
            for key in tqdm(urls):
                # Create the directory if it does not exist. This is required
                # before we save any files there.
                problem_destination = os.path.join(destination, key)
                if not os.path.exists(problem_destination):
                    os.makedirs(problem_destination)
                # A counter for the number of submissions per username.
                user_counter = Counter()
                for url in tqdm(urls[key]):
                    time.sleep(1)
                    browser.get(base_url + url)
                    # Wait for the page to load.
                    scrape_utils.wait_for_load(browser, "browser.find_element_by_id('submission-code')")
                    soup = BeautifulSoup(browser.page_source, "html.parser")
                    # Get submission username.
                    user_name = "undefined_user"
                    # Try to get the name. If it is not found, then the user
                    # has deleted their account. We still save the name, but as
                    # an undefined user.
                    try:
                        user_name = soup.find("div", class_="alert").find("span", class_="bold").text.strip()
                    except:
                        pass
                    # Begin reading the code to a file in the directory.
                    lines = soup.find(id="submission-code").find_all("pre")
                    # The files are stored with the path '.code', as it is not
                    # certain what language they will be written in.
                    with open(os.path.join(problem_destination, f"{user_name}_{user_counter[user_name]}.code"), "w") as f:
                        for line in lines:
                            # Since the HTML uses &nbsp; characters, we have to
                            # replace them with regular indentations. The
                            # &nbsp; characters appear as ' \xa0' when read in
                            # by beautiful soup. Additionally, sometimes
                            # "\u200b" will appear. This is a zero-width space,
                            # and is accordingly replaced with nothing.
                            f.write(line.text.replace(" \xa0", "    ").replace("\u200b", "") + "\n")
    finally:
        browser.close()

def scrape_solutions(admin_username, admin_password, destination=os.path.join(os.getcwd(), "solutions"), slugs=scrape_utils.SLUGS):
    """Scrape and save all solutions to the requested assignments. Assignments
    are identified by their slugs. Slugs are the last part of the URL for the
    assignment (as in hackerrank.com/<slug>).

    In order to get the solutions for each problem, the slugs for the
    particular problems are required. Rather than require the user to provide
    the problem slugs themselves, the problem slugs are simply scraped from the
    assignments.

    Parameters:
        admin_username(str) : The username associated with an hackerrank
                              account with access to the editorials for the
                              problems in each desired assignment. If the
                              account does not have access to a given
                              assignment's editorial, then no solution code
                              will be extracted. To obtain access, the problem
                              has to either be solved or purchased with
                              "hackos" on the account. The username and
                              password will be used to sign in to hackerrank on
                              a selenium browser.
        admin_password(str) : The password associated with an hackerrank
                              account with access to the editorials for the
                              problems in each desired assignment.
        destination (str)   : Destination directory to save the files. Files
                              will be saved in subdirectories by assignment
                              slug, in files with hackerrank ids as names.
                              Default is to create a new folder called
                              'solutions' in the current working directory.
        slugs (list)        : A list of slugs pertaining to the assignments that
                              are to be scraped. Slugs are the last part of the
                              URL for the assignment (as in
                              hackerrank.com/<slug>). Default is the list of
                              slugs provided in the source file.
    """
    # URLs for quick navigation.
    solution_url = "https://www.hackerrank.com/challenges/{}/editorial"
    assignment_url = "https://www.hackerrank.com/{}/challenges"

    # Regular expressions.
    problem_slug_finder = re.compile(r".*/challenges/(.*)$")

    # Open a selenium driver. Selenium is used because code from solutions are
    # hidden unless the user has either solved the problem or unlocked the
    # solution with an account.
    browser = scrape_utils.init_browser()

    try:
        # Login to hackerrank.
        scrape_utils.hackerrank_login(browser, admin_username, admin_password)

        # Get the problem slugs.
        problem_slugs = []
        # To obtain them, we loop through every assignment slug (from the slugs
        # parameter passed to this function).

        # TODO: This needs to be able to handle multiple pages of problems.
        # Currently, it only scrapes the first page. If an assignment is
        # larger, thenproblems will be missed.

        print("Gathering assignment slugs")

        for slug in tqdm(slugs):
            # Go to the assignment page.
            time.sleep(1)
            browser.get(assignment_url.format(slug))
            # Wait for the page to load. The condition is on whether the
            # problems have appeared on the page or not.
            scrape_utils.wait_for_load(browser, "browser.find_element_by_id('contest-challenges-problem')")
            # Get all the problems for this assignment.
            problems = BeautifulSoup(browser.page_source, "html.parser").find_all("div", id="contest-challenges-problem")
            # Extract each slug from the problem.
            for problem in problems:
                problem_slugs.append(problem_slug_finder.findall(problem.find("div", class_="span12").find("a")['href'])[0])

        # Now that we have the slugs, get all the code from the editorial page.
        # This is the page where the solutions are provided.

        print("Scraping solutions for each problem")
        for slug in tqdm(problem_slugs):
            time.sleep(1)
            browser.get(solution_url.format(slug))
            # This is a static page, so we don't need to wait for it to load.
            # Note that if an error occurs around here, it is likely because
            # the account used does not have access to the editorial page. If
            # this is the case, the account either needs to solve the problem
            # or obtain access using "hackos".

            # Create the directory if it does not already exist.
            problem_destination = os.path.join(destination, slug)
            if not os.path.exists(problem_destination):
                os.makedirs(problem_destination)
            for i, pre in enumerate(BeautifulSoup(browser.page_source, "html.parser").find_all("pre")):
                # The files are stored with the path '.code', as it is not
                # certain what language they will be written in.
                with open(os.path.join(problem_destination, f"{i}.code"), "w") as f:
                    f.write(pre.text.strip())
    finally:
        browser.close()

def submissions_against_submissions(submission_directory=os.path.join(os.getcwd(), "submissions"), threshold=.95, skip=[]):
    """Checks all submissions for every problem against other submissions for
    the same problem submitted by other students. This implementation uses
    python's built in diff library to perform a sequence match, which
    determines how close two files are to each other. The user can provide a
    custom threshold to raise an alert whenever two files are closer than the
    threshold.

    Student submissions are only compared against submissions from other
    students. If a student has submitted more than once, the submissions will
    not be checked against each other.

    Note that care should be taken to examine the complexity of a problem,
    especially if many alerts are raised for a given problem. There are only so
    many ways to write 'print("Hello, world!")'.

    Parameters:
        submission_directory : The directory where the submissions are stored.
                               These files can be obtained with the provided
                               scraping code in scrape.py, or can be uploaded
                               manually into a directory. Note that all files
                               should be .code files. The default value for
                               this parameter is the submissions folder in the
                               current working directory.
        threshold            : The threshold for when comparisons should raise
                               an alert. Any diff comparison done using the
                               SequenceMatcher method that has a ratio greater
                               than or equal to this value will raise an alert.
                               Default is .95.
        skip (list)          : A list of problem slugs to be skipped in the
                               comparison. If not provided, no problems will be
                               skipped."""
    # Regular expressions.
    username_finder = re.compile(r"(.*)_\d+.code$")

    for problem_folder in os.listdir(submission_directory):
        if problem_folder in skip:
            continue
        print(problem_folder)
        problem_directory = os.path.join(submission_directory, problem_folder)
        submissions = os.listdir(problem_directory)
        for submission in submissions:
            # Get the username associated with this submission.
            submission_user = username_finder.findall(submission)[0]
            submission_path = os.path.join(problem_directory, submission)
            for submission_other in submissions:
                # Check that the submissions are not made by the same user.
                if submission_user != username_finder.findall(submission_other)[0]:
                    submission_other_path = os.path.join(problem_directory, submission_other)
                    # Compare the submissions using SequenceMatcher.
                    a = open(submission_path, "r")
                    b = open(submission_other_path, "r")
                    ratio = SequenceMatcher(None, a.read(), b.read()).ratio()
                    if ratio >= threshold:
                        print("",submission, submission_other,ratio,sep="\t")
                    a.close()
                    b.close()
        # Pause between each problem. This can be removed in the future,
        # although I believe it makes it easier to see each individual problem.
        input("Press enter to continue to the next problem.")

def submissions_against_solutions(submission_directory=os.path.join(os.getcwd(), "submissions"), solution_directory=os.path.join(os.getcwd(), "solutions"), threshold=.95, skip=[]):
    """Checks all submissions against provided solutions. This implementation
    uses python's built in diff library to perform a sequence match, which
    determines how close two files are to each other. The user can provide a
    custom threshold to raise an alert whenever two files are closer than the
    threshold.

    These solutions should come from the Editorial pages on HackerRank,
    although, if desired, solutions may also be provided from the forum
    sections of HackerRank, to ensure no answers were copied from there.

    Note that care should be taken to examine the complexity of a problem,
    especially if many alerts are raised for a given problem. There are only so
    many ways to write 'print("Hello, world!")'.

    Parameters:
        submission_directory : The directory where the submissions are stored.
                               These files can be obtained with the provided
                               scraping code in scrape.py, or can be uploaded
                               manually into a directory. Note that all files
                               should be .code files. The default value for
                               this parameter is the submissions folder in the
                               current working directory.
        solution_directory   : The directory where the solutions are stored.
                               These files can be obtained with the provided
                               scraping code in scrape.py, or can be uploaded
                               manually into a directory. Note that all files
                               should be .code files. The default value for
                               this parameter is the solutions folder in the
                               current working directory.
        threshold            : The threshold for when comparisons should raise
                               an alert. Any diff comparison done using the
                               SequenceMatcher method that has a ratio greater
                               than or equal to this value will raise an alert.
                               Default is .95.
        skip (list)          : A list of problem slugs to be skipped in the
                               comparison. If not provided, no problems will be
                               skipped."""
    for problem_folder in os.listdir(submission_directory):
        if problem_folder in skip:
            continue
        print(problem_folder)
        problem_directory = os.path.join(submission_directory, problem_folder)
        solution_problem_directory = os.path.join(solution_directory, problem_folder)
        for submission in os.listdir(problem_directory):
            submission_path = os.path.join(problem_directory, submission)
            for solution in os.listdir(solution_problem_directory):
                solution_path = os.path.join(solution_problem_directory, solution)
                # Compare the submissions using SequenceMatcher.
                a = open(submission_path, "r")
                b = open(solution_path, "r")
                ratio = SequenceMatcher(None, a.read(), b.read()).ratio()
                if ratio >= threshold:
                    print("",submission, solution,ratio,sep="\t")
                a.close()
                b.close()
        # Pause between each problem. This can be removed in the future,
        # although I believe it makes it easier to see each individual problem.
        input("Press enter to continue to the next problem.")

def cheating_checker(admin_username, admin_password, slugs=scrape_utils.SLUGS, submission_directory=os.path.join(os.getcwd(), "submissions"), solution_directory=os.path.join(os.getcwd(), "solutions"), threshold=.95, skip=[], get_submissions=True, get_solutions = False):
    if not get_submissions:
        if not os.path.exists(submission_directory):
            raise ValueError("Submissions were not requested to be scraped, but there is no submissions directory. Please specify the correct directory or set get_submisisons to True to scrape the submissions.")
    else:
        print("##### Scraping Submissions #####")
        scrape_submissions(admin_username, admin_password, destination=submission_directory, slugs=slugs)
    if not get_solutions:
        if not os.path.exists(solution_directory):
            raise ValueError("Solutions were not requested to be scraped, but there is no solutions directory. Please specify the correct directory or set get_solutions to True to scrape the solutions.")
    else:
        print("#####  Scraping Solutions  #####")
        scrape_solutions(admin_username, admin_password, destination=solution_directory, slugs=slugs)
    submissions_against_submissions(submission_directory=submission_directory, threshold=threshold, skip=[])
    submissions_against_solutions(submission_directory=submission_directory, solution_directory=solution_directory, threshold=threshold, skip=[])
