from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\hp\Desktop\Chromedriver\chromedriver-win64\chromedriver.exe")
sleep(3)
driver.maximize_window()

driver.get("https://www.amazon.in")

ele = driver.find_element_by_xpath("//a[text()='Mobiles']")


print(ele.is_displayed())
print(ele.is_enabled())


