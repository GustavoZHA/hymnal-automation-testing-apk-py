from appium.webdriver.common.appiumby import AppiumBy


class HomeLocators:

    TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/title"
    )

    HYMNAL_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/bHimnario"
    )

    SEARCH_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/bBuscar"
    )

    FAVORITES_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/bFavoritos"
    )

    KNOWN_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/bConocidos"
    )

    CLASSIFICATION_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/bHPredicacion"
    )

    PERSONALIZED_LISTS_BUTTON = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/bCreateList"
    )
