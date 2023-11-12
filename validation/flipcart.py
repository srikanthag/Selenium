from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")
driver.get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

mobile_ele = driver.find_elements_by_xpath("//div[@class='_4rR01T']")
price_ele = driver.find_elements_by_xpath("//div[@class='_30jeq3 _1_WHN1']")

_mobiles = [item.text for item in mobile_ele]
_prices = [item.text for item in price_ele]

prices = []
import re
for price in _prices:
    match = re.findall(r'\d', price)
    prices.append(int(''.join(match)))
# print(prices)

pair = []
for mobile, ammount in zip (_mobiles, prices):
    pair.append({'name':mobile, 'price':ammount})
# print(pair)

_3000_5000 = [i for i in prices if i > 3000 and i < 5000]
print(_3000_5000)







