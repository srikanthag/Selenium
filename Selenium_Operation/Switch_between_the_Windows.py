from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\drivers\chromedriver.exe")
sleep(3)
driver.get("https://demo.automationtesting.in/Windows.html")
sleep(3)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
sleep(3)
# print(driver.current_window_handle) #Parent window value
Handles = driver.current_window_handle   #return all the handle values
# print(Handles)

for Handle in Handles:
    driver.switch_to_window(Handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

driver.quit()

