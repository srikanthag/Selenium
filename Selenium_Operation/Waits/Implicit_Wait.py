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





