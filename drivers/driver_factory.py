from appium import webdriver
from config.config import Config
from config.desired_caps import get_android_options


class DriverFactory:

    @staticmethod
    def create_driver():
        driver = webdriver.Remote(
            command_executor=Config.APPIUM_SERVER,
            options=get_android_options()
        )
        driver.implicitly_wait(10)
        return driver
