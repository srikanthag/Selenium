from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")
driver.get("file:///C:/Users/srikanth/Downloads/demo.html")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located(('name', 'fname')))          #wait untill 'fname' visible
driver.find_element_by_name('fname').send_keys('srikanth')

