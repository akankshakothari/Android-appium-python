import os

# Define Android SDK and Appium paths
class Config:
    # Android-related configurations
    ANDROID_HOME = os.environ.get("ANDROID_HOME", "D:\\a\\1\\s\\android-sdk-windows")
    PLATFORM_VERSION = "11"
    DEVICE_NAME = "Android Emulator"
    PLATFORM_NAME = "Android"
    APP_PACKAGE = "com.example.app"
    APP_ACTIVITY = "com.example.app.MainActivity"
    
    # Appium-related configurations
    APPIUM_SERVER_URL = f"http://127.0.0.1:{os.environ.get('APPIUM_PORT', '4723')}/wd/hub"

    # Derived paths
    PLATFORM_TOOLS_PATH = os.path.join(ANDROID_HOME, "platform-tools")
    SDK_MANAGER_PATH = os.path.join(ANDROID_HOME, "cmdline-tools", "latest", "bin", "sdkmanager.bat")

# Sanity check for paths
print("ANDROID_HOME:", Config.ANDROID_HOME)
print("PLATFORM_TOOLS_PATH:", Config.PLATFORM_TOOLS_PATH)
print("SDK_MANAGER_PATH:", Config.SDK_MANAGER_PATH)
print("APPIUM_SERVER_URL:", Config.APPIUM_SERVER_URL)