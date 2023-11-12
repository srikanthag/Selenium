from selenium import webdriver
from time import sleep
import re
driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")

'''Twitter'''
driver.find_element_by_xpath("//a[text()='Twitter']").click()
sleep(5)
h = driver.window_handles
driver.switch_to.window(h[1])
sleep(5)

driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("srikanth")
driver.switch_to.window(h[0])
sleep(5)
driver.find_element_by_xpath("//a[text()='Log in']").click()

'''Facebook'''
driver.find_element_by_xpath("//a[text()='Facebook']").click()
sleep(5)
h = driver.window_handles
sleep(5)
driver.switch_to.window(h[1])
sleep(5)
driver.find_element_by_name("email").send_keys("srikanth@i234")
sleep(5)
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys('123456789')
sleep(5)
driver.find_element_by_xpath("//span[text()='Log In']").click()
sleep(5)













