from appium.webdriver.common.appiumby import AppiumBy


class Gestures:
    """Helper class for common mobile gestures (scroll, swipe, drag)."""

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, duration_ms: int = 800):
        """Scroll down the screen using percentage-based coordinates."""
        size = self.driver.get_window_size()
        start_x = int(size["width"] * 0.5)
        start_y = int(size["height"] * 0.75)
        end_y = int(size["height"] * 0.25)
        self.driver.swipe(start_x, start_y, start_x, end_y, duration_ms)

    def scroll_up(self, duration_ms: int = 800):
        """Scroll up the screen using percentage-based coordinates."""
        size = self.driver.get_window_size()
        start_x = int(size["width"] * 0.5)
        start_y = int(size["height"] * 0.25)
        end_y = int(size["height"] * 0.75)
        self.driver.swipe(start_x, start_y, start_x, end_y, duration_ms)

    def scroll_to_text(self, text: str):
        """Scroll until element containing the specified text is visible (Android UiScrollable)."""
        selector = (
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            f'.scrollIntoView(new UiSelector().textContains("{text}").instance(0));'
        )
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
