# Assert: Assert command checks if the given condition is true or false. If the condition is true, the program control
# will execute the next phase of testing, and if the condition is false, execution will stop, and nothing will be executed.

from selenium import webdriver

# Assuming you've set up your webdriver (e.g., ChromeDriver)
driver = webdriver.Chrome(r'C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe')

# Navigating to a webpage
driver.get('https://www.google.com/')

# Finding an element and asserting its presence
try:
    # For example, checking if the title contains 'Example Domain'
    assert 'Facebook' in driver.title
    print("Assertion passed: Title contains 'Facebook'")

except AssertionError:
    print("Assertion failed: Title doesn't contain 'Google'")

# Closing the browser window
driver.quit()

# =================================================================================================================

# Verify: Verify command also checks if the given condition is true or false. It doesn't halt program execution,
# i.e., any failure during verification would not stop the execution, and all the test phases would be executed.

from selenium import webdriver

# Assuming you've set up your webdriver (e.g., ChromeDriver)
driver = webdriver.Chrome(r'C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe')

# Navigating to a webpage
driver.get('https://www.google.com/')

# Verifying element presence by finding it with its ID
try:
    # Finding an element by its ID (you can use other locators like XPath, CSS selectors, etc.)
    element = driver.find_element_by_id('gdfhfgjh')

    # Check if the element is displayed on the page
    assert element.is_displayed(), "Element is not displayed"

    # Get the value of a specific attribute (e.g., 'href' attribute of a link)
    href_value = element.get_attribute('href')
    print(f"Element's href attribute value: {href_value}")
    print("Element is present and displayed")

except Exception as e:
    print(f"Element verification failed: {e}")

# Closing the browser window
driver.quit()
