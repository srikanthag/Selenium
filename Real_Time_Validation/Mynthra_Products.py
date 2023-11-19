from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\_pytest\chromedriver.exe")
driver.get("https://www.myntra.com/")
sleep(3)

# shirts_name = driver.find_elements_by_xpath("//h4[@class='product-product']")
# original_price = driver.find_elements_by_xpath("//span[@class='product-strike']")


# shirt = [item.text for item in shirts_name]
# prices = [item.text for item in original_price]


'''shirt and price'''

# ammount = []
# import re
# for price in prices:
#     match = re.findall(r'\d', price)
#     ammount.append(int(''.join(match)))
# print(ammount)
#
# pair = []
# for t_shirt, _price in zip(shirt, ammount):
#     pair.append({'name': t_shirt, 'price': _price})
# print(pair)
#
# max = sorted(pair, key=lambda item: item['price'])[-1]
# min = sorted(pair, key=lambda item: item['price'])[0]

'''filternig perticular brand'''
# shirt_brand = driver.find_element_by_xpath("//h3[@class='product-brand']").click()
# for brand in shirt_brand:
#     if brand.text != "HELLCAT":
#         print(f"other brands are getting displayed{brand.text}")
#     else:
#         print(brand.text)


# '''login'''
actions = ActionChains(driver)
profile = driver.find_element_by_xpath("//span[text()='Profile']")
actions.move_to_element(profile).perform()
sleep(1)
driver.find_element_by_xpath("//a[@class='desktop-linkButton']").click()







