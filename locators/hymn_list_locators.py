from appium.webdriver.common.appiumby import AppiumBy


class HymnListLocators:

    HYMN_TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/tittle_record"
    )

    HYMN_NUMBER = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/number_record"
    )
