from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")
sleep(2)
driver.get("http://demowebshop.tricentis.com/")
sleep(4)
# name = driver.find_element_by_link_text("Register").tag_name
# print(name)

# driver.find_element_by_xpath("//input[@value='Search store']").send_keys('srikanth')
# driver.find_element_by_xpath("//input[@value='Search store']").clear()
# driver.find_element_by_link_text("Register").click()
# sleep(3)
# print(driver.find_element_by_id("gender-male").is_selected())


# _size = driver.find_element_by_name("q").size
# print(_size)
#
# _size = driver.find_element_by_id("mob-menu-button").size
# print(_size)

# Location = driver.find_element_by_name("q").location
# print(Location)
#
# __rect__ = driver.find_element_by_name("q").rect
# print(__rect__)

# ele_colour = driver.find_element_by_xpath("//img[@src='/Themes/DefaultClean/Content/images/logo.png']").value_of_css_property('background-color')
# assert ele_colour == hex(#B80709)










