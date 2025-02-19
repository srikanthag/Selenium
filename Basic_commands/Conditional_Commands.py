from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"D:\IT\Selenium\Chromedriver\chromedriver.exe")
sleep(3)
driver.maximize_window()

driver.get("https://demowebshop.tricentis.com/")

ele = driver.find_element_by_xpath("//a[text()='Register']")

print(ele.is_displayed())
print(ele.is_enabled())


