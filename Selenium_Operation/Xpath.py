from selenium import webdriver
from time import sleep
import re
driver = webdriver.Chrome(r"/_pytest/chromedriver.exe")
# driver.get("http://demowebshop.tricentis.com/")
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=58075519359&hvpone=&hvptwo=&hvadid=486462756374&hvpos=&hvnetw=g&hvrand=17528145648604735166&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007768&hvtargid=kwd-64107830&hydadcr=14452_2154371&gclid=EAIaIQobChMIldOa7bHq9gIViHwrCh03EQ7REAAYASAAEgLsrPD_BwE")

#driver = Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")

#driver.get("http://demowebshop.tricentis.com/")
#driver.find_element_by_xpath("//a[text()='Fiction']/../..//input[@value='Add to cart']").click()
# books = ['Fiction', 'Computing and Interne', 'Science']


#lauunches chrome driver
# driver = Chrome(r"C:\Users\srikanth\Desktop\Selenium_project\chromedriver_win32\chromedriver.exe")

#Absalute xpath

#driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys('srikanth')
#driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys('ag')
#driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys('testyanthra')
#driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys('bangalore')


#Related xpath
# driver.find_element_by_xpath("//a[@class='ico-register']").click()
# driver.find_element_by_xpath("//input[@id='gender-male']").click()
# driver.find_element_by_xpath("//input[@id='FirstName']").send_keys('srikanth')
# driver.find_element_by_xpath("//input[@id='LastName']").send_keys('ag')
# driver.find_element_by_xpath("//input[@id='Email']").send_keys('srikanth@gmail.com')
# driver.find_element_by_xpath("//input[@id='Password']").send_keys('12345677')
# driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys('12345677')
# driver.find_element_by_xpath("//input[@id='register-button']").click()

#text match
# driver.find_element_by_xpath("//a[text()='Books']").click()

#indexing
# driver.find_element_by_xpath("//input[@name='Gender'][1]").click()

#add to cart(single book)
# driver.get("http://demowebshop.tricentis.com/books")
# sleep(3)
# driver.find_element_by_xpath("//a[text()='Fiction']/../..//input[@value='Add to cart']").click()

#multiple books
# books = ['Fiction', 'Computing and Internet', 'Health Book']
# for book in books:
#    _xpath = f"//a[text()='{book}']/../..//input[@value='Add to cart']"
#    print(_xpath)
#    driver.find_elements_by_xpath(_xpath).click()

#XPATH OF RADIO BUTTON CORRESPONDING TO RATING “GOOD”, “EXCELLENT”, “POOR”, “VERY BAD” IN DEMOWEBSHOP
# ratings = ['Excellent', 'Good', 'Poor', 'Very bad']
# for rating in ratings:
#     _xpath = f"//label[text()='{rating}']/..//input[@type='radio']"
#     print(_xpath)
#     driver.find_element_by_xpath(_xpath).click()
#
# driver.close()

#VALIDATE THE ACTUAL PRICES OF ALL THE sunglass
# driver = Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")
# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")
# sunglass = {'Sunglasses Aero':139.00, 'ORIGINAL COLLECTION':149.00, 'Custom Sunglasses':179.0}
# for glass,expected_price in sunglass.items():
#    _xpath = f"//span[text()='{glass}']/../../..//span[@class='art-price']"
#    actual_price = driver.find_element_by_xpath(_xpath).text
#    actual_price = re.findall(r"[\d+\.\d+]", actual_price)
#    _temp = float(''.join(actual_price))
#    if _temp == expected_price:
#        print('PASS')
#    else:
#        print('FAIL')


#GET THE LINK TEXT OF ALL LINKS PRESENT IN LEFT NAVIGATION BAR IN DEMOWEBSHOP WEBPAGE
# _xpath = "//div[@class='block block-category-navigation']//a"
# links = driver.find_elements_by_xpath(_xpath)
# for li in links:
#    print(li.text)
    

#GET LINK TEXT OF ALL FOOTER LINKS IN DEMOWEBSHOP WEBPAGE
#_xpath = "//div[@class='footer-menu-wrapper']//a"
#footer_links = driver.find_elements_by_xpath(_xpath)
#for item in footer_links:
#    print(item.text)

#GET THE SHARE PRICE DYNAMICALLY
# driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
# sleep(3)
# companies = ['BPCL', 'IOC', 'TCS']
# #to get header
# for company in companies:
#     print(f"{company:>15}", end='')
#
# while True:
#     for company in companies:
#         share_price = driver.find_element(f"//a[text()='{company}']/../..//td[7]").text
#         print(f"{company:>15}", end='')
#     print()
#     sleep(3)


#GET LINK TEXT OF ALL THE JOB TITLES IN SEARCH RESULTS OF MONSTER.COM
# driver.get("https://www.monsterindia.com/")
# sleep(3)
# driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys('Python')
# sleep(3)
# # driver.find_element_by_xpath("//strong[text()='Python']").click()
# # sleep(3)
# driver.find_element_by_xpath("//button[@class='No thanks']").click()
# sleep(1)
# driver.find_element_by_xpath("//input[@value='Search']").click()
#
# job_titles = driver.find_elements_by_xpath("//h3[@class='medium']")
# for job_title in job_titles:
#     print(job_title.text)
#
# driver.close()


















