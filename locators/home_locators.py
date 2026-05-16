from appium.webdriver.common.appiumby import AppiumBy


class HomeLocators:

    HYMNAL_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Himnario"
    )

    SEARCH_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Buscar"
    )

    FAVORITES_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Favoritos"
    )

    CLASSIFICATION_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Clasificación de Himnos"
    )
