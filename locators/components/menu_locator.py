from appium.webdriver.common.appiumby import AppiumBy


class MenuLocators:
    DRAWER_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Open navigation drawer"
    )

    HOME_BUTTON_BAR = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btn_home_button_bar"
    )