from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")

time.sleep(10)
driver.maximize_window()

# Open Google
driver.get("https://www.google.co.in")

# Wait for 10 seconds (optional)
time.sleep(10)

# Find the search input element by name
search_input = driver.find_element("id", "APjFqb")

# Enter the search query
search_input.send_keys('Rohit Sharma', Keys.ENTER)

# Wait for the page to load (optional)
time.sleep(5)

# Print the title and current URL
print("Title:", driver.title)
print("URL:", driver.current_url)

# Close the browser
driver.close()      # close current browser
driver.quit()       # close all browser





