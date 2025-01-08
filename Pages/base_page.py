from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_type, locator_value):
        return self.driver.find_element(getattr(AppiumBy, locator_type), locator_value)

    def click_element(self, locator_type, locator_value):
        self.find_element(locator_type, locator_value).click()