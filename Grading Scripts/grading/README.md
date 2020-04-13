# Competitive Coding Tools

Note that all provided scraping tools will likely require maintenance to account for changes made to hackerrank.com.

## Grading

Included is a scraper that obtains scores from HackerRank.

### scrape_grades

This function scrapes grades from each provided assignment.

Run with headless mode OFF to debug.
                           
### clean_grades

This function cleans grades that are obtained.
A CSV file is required, containing 3 columns: one for Net ID, one for hackerrank_id, and one containing the number of credit hours.
                                  
The output file will be a file that can be uploaded to LearningSuite with minimal work.

### grader

This method runs the previous two methods 

## Cheating Checker

Included is a scraper that checks for cheating. Note that this scraping process takes a bit longer. A naive diff check is used to compare submissions.

### scrape_submissions

Scrapes submissions for each student on each assignment provided.

### scrape_solutions

Scrapes solutions for each assignment. Solutions from hackerrank will not be obtained if the solution editorial is not unlocked (this can be done by completing the problem).

### submissions_against_submissions

Check submissions against submissions. For checking for students copying from each other.

### submissions_against_solutions

Check submissions against solutions. 

### cheating_checker

Run all of the above functions in order.

## scrape_utils

These are scraping utility functions that are shared across both of the scraping files. Note that the scraping is backed by Selenium, and a Chrome browser should be available for use. 

### init_browser

Initializes a Selenium browser with some useful settings. Set headless to OFF for debugging.

### wait_for_load

A useful function to have the browser wait for loading until a given command no longer raises an exception.

### attempt_to_send_keys_to_all_elements_with_xpath

Useful for signing in to websites that use weird tricks to try to disallow bots to sign in (such as HackerRank). Sends keys to all elements with a given xpath.

### hackerrank_login

Simply log in to HackerRank.