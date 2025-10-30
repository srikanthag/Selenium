from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r"D:\IT\Selenium\Chromedriver\chromedriver.exe")

time.sleep(10)

driver.maximize_window()

driver.get("https://www.google.co.in/")
time.sleep(5)

driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys('ROhit sharma', Keys.ENTER)
time.sleep(5)

print("Title:", driver.title)
print("URL:", driver.current_url)

# Close the current browser window
driver.close()

# Close all browser windows
driver.quit()