from selenium import webdriver
from time import sleep
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")

class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):
        #args = (("name", "FirstName"), ) and kwargs = {value = 'srikanth'}
        locator = args[0]
        wait = WebDriverWait(driver, 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        #click_element(("link_text", "Register"),)
        #enter_text(("name", "FirstName"),value='srikanth')
        return func(*args, **kwargs)        #aCTUAL GENERIC FUNCTION GETS EXECUTED
    return wrapper

@wait       #click on the element
def click_element(locator):
    driver.find_element(*locator).click()

@wait       #enter something inside text box
def enter_text(locator, *, value):
    driver.find_element(*locator).click()
    driver.find_element(*locator).send_keys(value)

@wait       #select item from some list box
def select_item(locator, *, item):
    element = driver.find_element(*locator)
    s = Select(element)
    if isinstance(item, str):
        s.select_by_visible_text(item)
    elif isinstance(item, int):
        s.select_by_index(item)
    else:
        raise TypeError

'''ADD TO CART'''
# click_element(("link text", "Books"))
# sleep(2)
# click_element(("link text", "Computing and Internet"))
# sleep(2)
# click_element(("id", "add-to-cart-button-13"))
# sleep(3)
# click_element(("link text", "Books"))
# sleep(2)
# click_element(("link text", "Fiction"))
# sleep(3)
# click_element(("id", "add-to-cart-button-45"))
# sleep(3)
# driver.close()

'''Register'''
# click_element(("link text", "Register"))
# sleep(3)
# click_element(("id", "gender-male"))
# sleep(2)
# enter_text(("id", "FirstName"), value='srikanth')
# sleep(2)
# enter_text(("id", "LastName"), value='ag')
# sleep(2)
# enter_text(("id", "Email"), value='srikanth123@wer')
# sleep(2)
# enter_text(("id", "Password"), value='123456789')
# sleep(2)
# enter_text(("id", "ConfirmPassword"), value='123456789')
# sleep(2)
# click_element(("id", "register-button"))
# sleep(3)





