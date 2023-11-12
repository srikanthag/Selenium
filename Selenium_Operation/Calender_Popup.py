# from selenium import webdriver
# from time import sleep
# import re
#
# from selenium.common.exceptions import NoSuchElementException
#
# driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")
# driver.get("https://www.goibibo.com/")
# sleep(5)
# driver.find_element_by_xpath("//span[text()='Departure']").click()
# sleep(2)
# _month ='August 2022'
# _date = 22
# for _ in range(12):
#     try:
#         driver.find_element_by_xpath(f"//div[text()='{_month}']")
#         break
#     except NoSuchElementException:
#         driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
#         sleep(1)
#         continue
# #select day
# try:
#     driver.find_element_by_xpath(f"//div[text()='22']").click()
# except NoSuchElementException:
#     print('no such date present')
