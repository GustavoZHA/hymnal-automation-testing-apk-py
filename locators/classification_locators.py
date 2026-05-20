from appium.webdriver.common.appiumby import AppiumBy


class ClassificationLocators:

    TITLE = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/title"
    )

    SCROLL_VIEW = (
        AppiumBy.ID,
        "com.pentecostal.himnarioprincipal:id/scrollCustom"
    )

    @staticmethod
    def category_item(category_text):
        return (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@text='{category_text}']"
        )

    @staticmethod
    def category_item_scrollable(category_text):
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().resourceId("com.pentecostal.himnarioprincipal:id/scrollCustom")).scrollIntoView(new UiSelector().text("{category_text}"))'
        )
