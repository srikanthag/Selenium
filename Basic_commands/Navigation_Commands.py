from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\Chromedriver\chromedriver-win64\chromedriver.exe")
sleep(3)
driver.maximize_window()

driver.get("https://www.amazon.in")
print(driver.title)
sleep(3)

driver.get("https://www.flipkart.com")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)


driver.close()
