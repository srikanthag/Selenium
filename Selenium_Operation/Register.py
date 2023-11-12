from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

#from pytest import fixture
driver = Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")

class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):       # args = (self, ("link text", "Register"))
        # args = (("name", "FirstName"), ) kwargs = {value="hello"}
        instance = args[0]
        locator = args[1]
        wait = WebDriverWait(instance.driver, 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        # click_element(("link text", "Register"))
        # enter_text(("name", "fname"), value="hello")
        return func(*args, **kwargs)        # actual generic func gets executed
    return wrapper

class Selenium_Wrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def test_click_element(self, locator):
        self.driver.find_element(*locator).click()       # find_element("link text", "register")

    @wait
    def test_enter_text(self, locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def test_select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise TypeError

s = Selenium_Wrapper(driver)
s.test_click_element(("link text", "Register"))
sleep(3)
s.test_click_element(("id", "gender-male"))
sleep(2)
s.test_enter_text(("id", "FirstName"), value='srikanth')
sleep(2)
s.test_enter_text(("id", "LastName"), value='ag')
sleep(2)
s.test_enter_text(("id", "Email"), value='srikanthag93@gmqil.com')
sleep(2)
s.test_enter_text(("id", "Password"), value='123456789')
sleep(2)
s.test_enter_text(("id", "ConfirmPassword"), value='123456789')
sleep(2)
s.test_click_element(("id", "register-button"))
sleep(3)
print('pass')
driver.close()









