from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\drivers\chromedriver.exe")
sleep(3)
driver.maximize_window()
driver.get("https://www.google.co.in")
sleep(3)
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys('Rohit sharma', Keys.ENTER)





