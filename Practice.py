
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:\Users\Asus\Desktop\Test\chromedriver.exe")
driver.get("https://www.google.com/")
sleep(2)
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("srikanth",Keys.ENTER)
sleep(2)