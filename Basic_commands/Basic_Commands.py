from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")
sleep(3)
driver.maximize_window()
driver.get("https://www.google.co.in")
sleep(10)
driver.find_element_by_xpath("//textarea[@class='gLFyf']").send_keys('Rohit sharma', Keys.ENTER)

print(driver.title)
print(driver.current_url)

driver.close()      # close current browser
driver.quit()       # close all browser





