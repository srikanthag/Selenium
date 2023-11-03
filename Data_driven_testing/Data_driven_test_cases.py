from time import sleep
import XlUtils
from selenium import webdriver
from Data_driven_testing.Readning_data_from_Excel import r

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\drivers\chromedriver.exe")
sleep(3)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")

path = r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\Data_driven_testing\Login_data.xlsx"


rows = XlUtils.getRowCount(path, 'Sheet1')

for i in range(1,rows+1):
    username = XlUtils.ReadData(path, "sheet1", r, 1)
    password = XlUtils.ReadData(path,"Shtte1", r, 2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(username)

    # driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input").send_keys(username)
    # driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input").send_keys(password)























