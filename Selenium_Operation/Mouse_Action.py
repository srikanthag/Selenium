from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\drivers\chromedriver.exe")
sleep(3)
driver.maximize_window()

''' Mouse Hover '''
# driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
# Company = driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[4]/a")
# About_us = driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[4]/div/div/div/div/ul/li[1]/a")
#
# actions = ActionChains(driver)
# actions.move_to_element(Company).move_to_element(About_us).click().perform()

'''Double click'''
# driver.get("https://testautomationpractice.blogspot.com/")
# Element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
#
# actions = ActionChains(driver)
# actions.double_click(Element).perform()

''' Right click'''
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# Button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
#
# actions = ActionChains(driver)
# actions.context_click(Button).perform()

''' Drag and drop'''
# driver.get("https://testautomationpractice.blogspot.com/")
# Source_element = driver.find_element_by_xpath("//*[@id='draggable']")
# Target_element = driver.find_element_by_xpath("//*[@id='droppable']")
# actions = ActionChains(driver)
# actions.drag_and_drop(Source_element, Target_element).perform()






