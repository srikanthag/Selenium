from selenium import webdriver
from time import sleep


#lauunches chrome driver
driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")

#navigate to demo
driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
# driver.refresh()
# driver.minimize_window()
#title
# current_title = driver.title
# url = driver.current_url
# print(current_title)
# print(url)

#close
# driver.close()




d = driver.find_element_by_link_text("Register").submit()
# sleep(2)
#
# d = driver.find_element_by_id("gender-male").click()
# sleep(2)
#
# d = driver.find_element_by_id("FirstName").send_keys('hello')
# sleep(2)
#
# d = driver.find_element_by_id("LastName").send_keys('world')
# sleep(2)
#
# d = driver.find_element_by_id("Email").send_keys('srikanthmanvi@gmail.com')
# sleep(2)
#
# d = driver.find_element_by_id("Password").send_keys('123456')
# sleep(2)
#
# d = driver.find_element_by_id("ConfirmPassword").send_keys('123456')
# sleep(2)
#
# d = driver.find_element_by_id("register-button").click()
# sleep(2)
