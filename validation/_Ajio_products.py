from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")
driver.get("https://www.ajio.com/search/?text=mens%20shoes")
sleep(3)
shoe_ele = driver.find_elements_by_xpath("//div[@class='nameCls']")
price_ele = driver.find_elements_by_xpath("//span[@class='price  ']")

shoe_names = [ item.text for item in shoe_ele ]
price_name = [ item.text for item in price_ele ]

prices = []
import re
for price in price_name:
    match = re.findall(r'\d', price)
    prices.append(int(''.join(match)))
#print(prices)       #to remove special char and it converts str in to int

pair = []
for shoe, price in zip(shoe_names, prices):
    pair.append({'name': shoe, 'price': price})
#print(pair)        get price and shoe pair

max = sorted(pair, key=lambda item: item['price'])[-1]
min = sorted(pair, key=lambda item: item['price'])[0]

#range between two prices
betwee_1000_3000 = [item for item in pair if item['price'] > 1000 and item['price'] < 3000]
print(betwee_1000_3000)

driver.close()
