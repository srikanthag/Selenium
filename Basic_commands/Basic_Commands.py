from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome(r"D:\IT\Selenium\Chromedriver\chromedriver.exe")

# Give the browser some time to load
time.sleep(10)

# Maximize the window
driver.maximize_window()

# Open Google
driver.get("https://www.google.co.in/")
time.sleep(5)

# Find the search box and enter 'ROhit sharma'
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys('ROhit sharma', Keys.ENTER)
time.sleep(5)

# Print the title and current URL after search
print("Title:", driver.title)
print("URL:", driver.current_url)

# Close the current browser window
driver.close()

# Close all browser windows
driver.quit()
