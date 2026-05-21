import os

import allure
import pytest
from drivers.driver_factory import DriverFactory
from utils.screenshots import ScreenshotUtil
from utils.video_recorder import VideoRecorder


def attach_file_to_allure(path, name, attachment_type):
    if path and os.path.exists(path):
        try:
            allure.attach.file(path, name=name, attachment_type=attachment_type)
        except Exception:
            pass


@pytest.fixture(scope="function")
def driver(request):
    driver = DriverFactory.create_driver()
    # start screen recording for the test
    try:
        VideoRecorder.start(driver)
    except Exception:
        pass
    # attach to the test node so hooks can access it
    request.node._driver = driver
    yield driver
    # ensure video is stopped and saved after the test
    try:
        VideoRecorder.stop_and_save(driver, request.node.name)
    except Exception:
        pass
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = None
        # prefer funcarg driver
        try:
            driver = item.funcargs.get("driver")
        except Exception:
            driver = getattr(item, "_driver", None)

        if driver:
            try:
                screenshot_path = ScreenshotUtil.capture(driver, item.name)
                attach_file_to_allure(
                    screenshot_path,
                    f"Screenshot - {item.name}",
                    allure.attachment_type.PNG,
                )
            except Exception:
                pass
            try:
                video_path = VideoRecorder.stop_and_save(driver, item.name)
                attach_file_to_allure(
                    video_path,
                    f"Video - {item.name}",
                    allure.attachment_type.MP4,
                )
            except Exception:
                pass
