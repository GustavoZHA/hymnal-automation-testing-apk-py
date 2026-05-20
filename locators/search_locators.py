from appium.webdriver.common.appiumby import AppiumBy


class SearchLocators:

    SEARCH_INPUT = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/editTextSearch"
    )

    SEARCH_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/buttonSearch"
    )

    RESULT_LIST = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/listResults"
    )

    RESULT_ITEM = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/recordList"
    )

    RESULT_NUMBER = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/number_record"
    )

    TOAST_MESSAGE = (
        AppiumBy.XPATH,
        "//android.widget.Toast"
    )

    RESULT_TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/tittle_record"
    )
