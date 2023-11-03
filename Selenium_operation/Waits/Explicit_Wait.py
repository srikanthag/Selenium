from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(r"/drivers/chromedriver.exe")
sleep(3)
driver.get("https://www.goibibo.com")

driver.find_element_by_xpath("//p[text()='Enter city or airport']").send_keys('Mysore',Keys.ENTER)
driver.implicitly_wait(10)


