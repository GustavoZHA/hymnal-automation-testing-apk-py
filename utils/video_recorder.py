import os
import base64
from datetime import datetime


class VideoRecorder:

    @staticmethod
    def start(driver):
        try:
            driver.start_recording_screen()
            return True
        except Exception:
            return False

    @staticmethod
    def stop_and_save(driver, name):
        try:
            raw = driver.stop_recording_screen()
            if not raw:
                return None
            video_data = base64.b64decode(raw)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join("reports", "videos")
            os.makedirs(path, exist_ok=True)
            file_path = os.path.join(path, f"{name}_{timestamp}.mp4")
            with open(file_path, "wb") as f:
                f.write(video_data)
            return file_path
        except Exception:
            return None
