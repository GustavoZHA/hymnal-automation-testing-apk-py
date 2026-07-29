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
    def stop(driver):
        """Stop recording and return raw video data without saving."""
        try:
            raw = driver.stop_recording_screen()
            if not raw:
                return None
            return raw
        except Exception:
            return None

    @staticmethod
    def save_video(raw_data, name):
        """Save video data to file."""
        try:
            if not raw_data:
                return None
            video_data = base64.b64decode(raw_data)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join("reports", "videos")
            os.makedirs(path, exist_ok=True)
            file_path = os.path.join(path, f"{name}_{timestamp}.mp4")
            with open(file_path, "wb") as f:
                f.write(video_data)
            return file_path
        except Exception:
            return None

    @staticmethod
    def stop_and_save(driver, name):
        """Stop recording and save video (deprecated: use stop() and save_video() separately)."""
        try:
            raw = VideoRecorder.stop(driver)
            return VideoRecorder.save_video(raw, name)
        except Exception:
            return None
