from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:\Users\Asus\Desktop\Test\chromedriver.exe")
sleep(2)
driver.get("https://www.google.com/")
sleep(3)
driver.find_element(By.ID, "APjFqb").send_keys("srikanth", Keys.ENTER)

print(driver.title)
driver.quit()