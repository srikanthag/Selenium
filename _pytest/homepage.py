from _pytest.selenium_wrapper import Selenium_Wrapper


class HomePage(Selenium_Wrapper):
    _lnk_register = ("link text", "Register")
    _lnk_login = ("link text", "Log in")
    _lnk_logout = ("link text", "Log out")

    def __init__(self, driver):
        super().__init__(driver)

    def home_click_register(self):
        self.click_element(HomePage._lnk_register)

    def home_click_login(self):
        self.click_element(HomePage._lnk_login)

    def home_click_logout(self):
        self.click_element(HomePage._lnk_logout)




