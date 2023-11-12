from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\drivers\chromedriver.exe")
sleep(3)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element_by_xpath("//*[@id='OKTab']/button").click()

driver.switch_to_alert().accept()
# driver.switch_to_alert().dismiss()

driver.close()
