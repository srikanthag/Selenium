from requests import request
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(r"/_pytest/chromedriver.exe")
sleep(2)
driver.get("file:///C:/Users/srikanth/Downloads/links.html")
sleep(4)

links = driver.find_elements_by_xpath("//a")
urls = [link.get_attribute("href") for link in links]
for item in urls[:15]:
    response = request("GET", url=item)
    if response.status_code == 200:
        print("got correct respomse")
    else:
        print(f"something went wrong::{item}")




