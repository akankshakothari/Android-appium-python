import unittest
from utils.driver_setup import init_driver
from Pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = init_driver()
        cls.login_page = LoginPage(cls.driver)

    def test_login(self):
        self.login_page.enter_username("test_user")
        self.login_page.enter_password("test_password")
        self.login_page.click_login()
        # Add assertion here

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()