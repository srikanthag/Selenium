from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")
driver.get("https://ide.geeksforgeeks.org / tryit.php / WXYeMD9tD4")

# create alert object
alert = Alert(driver)

# get alert text
print(alert.text)

# accept the alert
alert.accept()
