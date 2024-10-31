from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")

time.sleep(10)
driver.maximize_window()

# Open Google
driver.get("https://www.google.co.in")
time.sleep(5)
driver.find_element_by_xpath("//textarea[@id='APjFqb']").send_keys('ROhit sharma', Keys.ENTER)

# Print the title and current URL
print("Title:", driver.title)
print("URL:", driver.current_url)

# Close the browser
driver.close()      # close current browser
driver.quit()       # close all browser