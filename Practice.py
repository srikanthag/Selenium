from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\Chromedriver\chromedriver-win64\chromedriver.exe")
sleep(5)
driver.maximize_window()
sleep(5)
driver.get("https://demowebshop.tricentis.com/books")
books = driver.find_elements_by_xpath("//h2[@class='product-title']")
sleep(5)
for book in books:
    print(book.text)

