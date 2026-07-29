import os
import shutil

import allure
import pytest
from drivers.driver_factory import DriverFactory
from utils.screenshots import ScreenshotUtil
from utils.video_recorder import VideoRecorder


@pytest.fixture(scope="session", autouse=True)
def cleanup_videos():
    """Clear videos directory at the start of the test session."""
    video_dir = os.path.join("reports", "videos")
    if os.path.exists(video_dir):
        shutil.rmtree(video_dir)
    os.makedirs(video_dir, exist_ok=True)
    yield


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
    request.node._video_data = None  # Initialize video data storage
    yield driver
    # stop video recording and store the raw data (will save only if test failed)
    try:
        request.node._video_data = VideoRecorder.stop(driver)
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
                # Save video only for failed tests using stored raw data
                video_data = getattr(item, "_video_data", None)
                if video_data:
                    video_path = VideoRecorder.save_video(video_data, item.name)
                    attach_file_to_allure(
                        video_path,
                        f"Video - {item.name}",
                        allure.attachment_type.MP4,
                    )
            except Exception:
                pass
