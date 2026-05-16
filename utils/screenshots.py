import os
from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def capture(driver, name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join("reports", "screenshots")
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, f"{name}_{timestamp}.png")
        driver.save_screenshot(file_path)
        return file_path
