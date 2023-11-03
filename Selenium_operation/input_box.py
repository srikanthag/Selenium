from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r"/drivers/chromedriver.exe")
sleep(3)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
sleep(3)

driver.find_element_by_xpath("//input[@id='RESULT_TextField-1']").send_keys("Srikanth")
sleep(3)

driver.find_element_by_xpath("//input[@id='RESULT_TextField-2']").send_keys("AG")
sleep(3)

driver.find_element_by_xpath("//input[@id='RESULT_TextField-3']").send_keys("12345")
sleep(3)

driver.find_element_by_xpath("//input[@id='RESULT_TextField-4']").send_keys("india")
sleep(3)

driver.find_element_by_xpath("//input[@id='RESULT_TextField-5']").send_keys("Mangalore")
sleep(3)

driver.find_element_by_xpath("//input[@id='RESULT_TextField-6']").send_keys("srikanth@1234.webmail.com")
sleep(3)

driver.find_element_by_xpath("//input[@id='RESULT_RadioButton-7_0']").click()
sleep(3)




























