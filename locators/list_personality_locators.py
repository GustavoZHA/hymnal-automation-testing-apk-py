from appium.webdriver.common.appiumby import AppiumBy


class ListPersonalityLocators:

    TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/titleHymn"
    )

    NAME_INPUT = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/nameListsSearch"
    )

    CREATE_BUTTON = (
        AppiumBy.XPATH,
        "//android.widget.LinearLayout[@bounds='[1021,438][1111,528]']"
    )

    LISTS_CONTAINER = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/listHymns"
    )

    LIST_RECORD_ITEM = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/recordListHymns"
    )

    LIST_NAME_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/b_list_name"
    )

    LIST_NAME_TEXT = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/name_record"
    )

    DELETE_LIST_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/b_delete_list"
    )

    CONSTRAINT_LAYOUT = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/constraintLayoutSearchList"
    )

    TOAST_MESSAGE = (
        AppiumBy.XPATH,
        "//android.widget.Toast"
    )