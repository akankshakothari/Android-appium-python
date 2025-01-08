import pytest
from appium import webdriver
from Config.config import CONFIG

@pytest.fixture(scope="module")
def appium_driver():
    desired_caps = CONFIG
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

def test_app_launch(appium_driver):
    # Example: Verify if the app launches successfully
    assert appium_driver.is_app_installed("com.example.yourapp"), "App is not installed"