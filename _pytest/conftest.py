from selenium.webdriver import Chrome
from time import sleep
from _pytest.config import Config
from pytest import fixture

# Fixture
@fixture        #Fixtures are used for dependency injection or to pass the data to the test functions
def _driver():
    # Launches a new chrome browser
    driver = Chrome(r"C:\Users\hp\Desktop\IT\Testing\_selenium_files\_pytest\chromedriver.exe")
    driver.maximize_window()
    driver.get(Config.URL)
    sleep(3)
    yield driver        # passes the driver instance to all the test methods
    driver.quit()


