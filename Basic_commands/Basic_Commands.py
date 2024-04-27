
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a WebDriver instance (in this example, Chrome)
driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")

# Wait for 10 seconds (optional)
time.sleep(10)

# Maximize the browser window
driver.maximize_window()

# Open Google
driver.get("https://www.google.co.in")

# Wait for 10 seconds (optional)
time.sleep(10)

# Find the search input element by name
search_input = driver.find_element("name", "q")

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





