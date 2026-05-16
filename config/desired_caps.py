from appium.options.android import UiAutomator2Options
from config.config import Config


def get_android_options():
    options = UiAutomator2Options()
    options.platform_name = Config.PLATFORM_NAME
    options.device_name = Config.DEVICE_NAME
    options.automation_name = Config.AUTOMATION_NAME
    options.app = Config.APP_PATH
    return options
