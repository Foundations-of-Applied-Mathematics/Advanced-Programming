import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# The slugs below are from the Fall 2018 semester. Though many of them may be
# repeated in later iterations of the course, a new list of slugs should be
# created for each semester. This list serves as an example of what a slug is,
# and how the list should be constructed.
SLUGS = [
    # Assignments
    #'math-495r-09-data-structures',
    #'math-495r-09-strings',
    #'math-495r-09-brute-force',
    #'math-495r-09-greedy',
    #'math-495r-09-recursion',
    #'math-495r-09-graph',
    #'math-495r-09-dynamic-programming'
    #'math-495r-09-mixed-1',
    # 'math-495r-09-mixed-problem-set-2'

    # 'math-495r-math'
    # 'math-495r-data-structures',
    # 'math-495r-strings',
    # 'math-495r-dynamic-programming',
    # 'math-495r-greedydynamic',
    # 'math-495r-divide-and-conquer'
    # 'math-495r-graphs'
    # 'math-495r-graphs-2'
    'math-495r-number-theory'
]

def init_browser(headless=True):
    """Initialize a Selenium Chrome web browser. Initializing through this
    function allows for uniform initialization, allowing for setting browser
    preferences uniformly across all initializations.

    Be sure to close the browser after it has been used.

    Parameters:
        headless (bool) : Whether or not the browser will run in 'headless'
                          mode. If set to True, the browser will not be visible
                          as it is running. Default value is True."""
    chrome_options = webdriver.ChromeOptions()
    # Disable notifications.
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    # Set the log level to avoid javascript error messages being displayed.
    chrome_options.add_argument('log-level=3')
    # Set headless.
    chrome_options.headless = headless
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

def wait_for_load(browser, statement, refresh_period=5, timeout=None):
    """Wait for the selenium browser to load, using the given code string as
    the condition upon which to wait. The code should be a statement that
    raises an error when the page is not loaded (for example, a call to find an
    element on the page. The element not being present will raise a value
    error).

    The loader will attempt to run the given code at 1-second intervals, and if
    after the refresh period the code still raises an error, the page is
    refreshed and the loading loop is continued. This is to prevent issues with
    endless loops when a page doesn't load correctly.

    An example of usage of this function would be:
    wait_for_load(browser, "browser.find_element_by_xpath(\"//div[@class='table-wrap']\")")

    Alternatively, if a desired condition does not raise an error, an
    if-statement can be used to generate errors. For example:
    wait_for_load(browser, "if len(browser.find_elements_by_xpath(\"//input[@type='checkbox']\") < 10): raise NoSuchElementException(\"Error\")
    This condition checks how many elements are found with the given condition,
    and waits for at least 10 of them to be loaded.

    Ultimately, this function calls exec() on the given code, so any valid
    python code can be used (if more complex statements are desired). The only
    caveat is that the function must raise an error of some sort when the
    condition is not met.

    Parameters:
        browser (WebDriver)  : A Selenium webdriver, preferably a
                               selenium.webdriver.chrome.webdriver.WebDriver
                               object, but others should be usable. The
                               function has only been tested with a chrome
                               driver.
        statement (str)      : A string of python code containing a statement
                               to be evaluated. This estatement must raise a
                               value error upon failing in order to function as
                               a condition upon which to wait.
        refresh_period (int) : How many seconds to wait before the browser is
                               refreshed. This is to prevent stale pages from
                               trapping us in an endless loop. Set to None to
                               never refresh. Default value is 5.
        timeout (int)        : How many seconds to wait before the wait
                               request will timeout. Upon timeout, a
                               RuntimeError will be raised. If no timeout is
                               desired, set to None. Default is None."""
    loading = True
    load_refresh_count = 0
    timeout_count = 0
    while loading:
        try:
            # Execute the given statement. If the statement raises an error,
            # the try-except block here will catch it, wait one second, and
            # attempt to execute the statement again.
            # Any statement passed in here should eventually resolve, or else
            # an endless loop will occur.
            exec(statement)
            loading=False
        except:
            load_refresh_count += 1
            timeout_count += 1
            # Refresh.
            if refresh_period is not None and load_refresh_count >= refresh_period:
                browser.refresh()
                load_refresh_count = 0
            # Timeout.
            if timeout is not None and timeout_count >= timeout:
                raise RuntimeError(f"wait_for_load timed out with timeout value {timeout}. The statement {statement} could not execute within the given timeout. (If no timeout is desired, timeout can be set to None to avoid this error in the future)")
            time.sleep(1)

def attempt_to_send_keys_to_all_elements_with_xpath(browser, xpath, keys, cont=False):
    """Attempt to send the desired keys to all elements with the desired xpath.
    Each element with the xpath will receive the desired keys. If continue is
    set to false, the sending will stop when one of the sends succeeds.

    This is useful because certain websites (such as hackerrank) will sometimes
    mask elements with other 'dummy' elements with the same type, id, etc. to
    prevent bots from using services such as login pages. The number of dummy
    elements can change, sometimes every day, causing this method to be
    necessary.

    An example usage is:
    attempt_to_send_keys_to_all_elements_with_xpath(browser, "//input[@type='password']", "hunter2")

    Parameters:
        browser (WebDriver) : A Selenium webdriver, preferably a
                              selenium.webdriver.chrome.webdriver.WebDriver
                              object, but others should be usable. The
                              function has only been tested with a chrome
                              driver.
        xpath (str)         : The xpath to find the elements by.
        keys (str)          : The keys to send to the element. This can either
                              be a full string or something obtained from
                              Selenium's Keys library, such as, for example,
                              Keys.RETURN.
        cont (bool)         : Whether or not to continue after the keys have
                              been sent successfully once. The default is
                              False, meaning it will return after one
                              success."""
    elements = browser.find_elements_by_xpath(xpath)
    for i in range(len(elements)):
        try:
            elements[i].send_keys(keys)
            # If we don't want to continue, then we return from this function,
            # because the sending executed properly.
            if not cont:
                return
        except:
            pass

def hackerrank_login(browser, username, password):
    """Login to HackerRank with the given username and password on a selenium
    driver. The driver is pointed to the sign-in page, the sign-in is
    conducted, and the function returns when the browser is pointed to the
    dashboard page (www.hackerrank.com/dashboard).

    Paramters:
        browser (WebDriver) : A Selenium webdriver, preferably a
                              selenium.webdriver.chrome.webdriver.WebDriver
                              object, but others should be usable. The
                              function has only been tested with a chrome
                              driver.
        username(str)       : The username associated with a hackerrank
                              account. The username and password will be used
                              to sign in to hackerrank on a selenium browser.
        password(str)       : The password associated with a hackerrank
                              account."""
    # URLs for quick navigation.
    sign_in_url = "https://www.hackerrank.com/login?h_r=login&h_l=body_middle_left_button"
    main_url = "https://www.hackerrank.com/dashboard"

    browser.get(sign_in_url)
    # Send username.
    attempt_to_send_keys_to_all_elements_with_xpath(browser, "//input[@type='text']", username)

    # Send password.
    # Note that we find all elements with the type 'password' and type
    # 'submit, because these fields are masked with "dummy" elements that
    # are not interactable. Just get all elements and index to the second
    # one in both cases.
    attempt_to_send_keys_to_all_elements_with_xpath(browser, "//input[@type='password']", password)

    # Submit.
    attempt_to_send_keys_to_all_elements_with_xpath(browser, "//button[@type='submit']", Keys.RETURN)

    # Wait for the login to process.
    # The statement passed in to wait_for_load checks two things:
    #   1. If the browswer's current url is the dashboard url.
    #   2. If the page has finished loading.
    # If one of those conditions is not met, a NoSuchElementException is
    # raised, causing the function to wait and try again.
    wait_for_load(browser, f"if browser.current_url != '{main_url}' or browser.execute_script('return document.readyState;') != 'complete': raise NoSuchElementException('Page not yet loaded')")
