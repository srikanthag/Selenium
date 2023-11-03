from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\drivers\chromedriver.exe")
sleep(3)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

''' Scrolldown by pixcel '''
# driver.execute_script("window.scrollBy(0,5000","")

''' Scroll down the page till the element is visible '''
# flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
# driver.execute_script("arguments[0].scrollIntoView();",flag)

''' Scroll till end '''
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")





