from appium.webdriver.common.appiumby import AppiumBy


class ConocidosLocators:

    TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/titleList"
    )

    HYMNS_LIST = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/listHymnos"
    )

    HYMN_RECORD = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/recordList"
    )

    HYMN_NUMBER = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/number_record"
    )

    HYMN_TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/tittle_record"
    )

    HOME_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/btn_home_button_bar"
    )

    NAVIGATION_DRAWER = (
        AppiumBy.ACCESSIBILITY_ID,
        "Open navigation drawer"
    )
