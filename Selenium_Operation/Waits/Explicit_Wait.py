""" Explicit wait  """
# * Explicit Wait time is applied only to those elements which are intended by us
# * An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution.
# * 'visibility_of_element_located' checks if the web element is present on the DOM and also visible on the webpage.
# * "TimeoutException" will be raised if either the element is not loaded onto the DOM or the element is not visible on the web page within timeout period.
# * sleep() i.e. a static wait that will halt the test execution for some specified time and then perform the next step.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")
driver.get("file:///C:/Users/srikanth/Downloads/demo.html")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located(('name', 'fname')))          #wait untill 'fname' visible
driver.find_element_by_name('fname').send_keys('srikanth')
