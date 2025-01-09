from appium import webdriver
from utils.config import Config

def init_driver():
    desired_caps = {
        "platformName": Config.PLATFORM_NAME,
        "platformVersion": Config.PLATFORM_VERSION,
        "deviceName": Config.DEVICE_NAME,
        "appPackage": Config.APP_PACKAGE,
        "appActivity": Config.APP_ACTIVITY,
    }
    return webdriver.Remote(Config.APPIUM_SERVER_URL, desired_caps)