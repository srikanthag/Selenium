from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")
driver.get("https://ide.geeksforgeeks.org / tryit.php / WXYeMD9tD4")

# create alert object
alert = Alert(driver)

# get alert text
print(alert.text)

# accept the alert
alert.accept()

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\drivers\chromedriver.exe")
sleep(3)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element_by_xpath("//*[@id='OKTab']/button").click()

driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()

driver.close()
