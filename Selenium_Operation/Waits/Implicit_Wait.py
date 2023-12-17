"""  Implicitly wait """
# * Implicit Wait time is applied to all the elements in the script
# * An Implicitly wait is one of the ways to request selenium not throw any exception until provided time.
# * If the element is found before implicitly wait time, selenium moves to the next commands in the program without
#   waiting further, this wait is also called dynamic wait. If element not present it throws Nosuchelement exception


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\drivers\chromedriver.exe")
sleep(3)
driver.get("https://www.amazon.in/")

driver.implicitly_wait(10)  #applicable for all the elements in the page

driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('mens Fasttrack watch', Keys.ENTER)
driver.find_element_by_xpath("//span[@id='nav-cart-count']")
