import subprocess
import os


class AdbHelper:
    """Helper utilities for ADB operations during mobile test automation."""

    @staticmethod
    def push_file(local_path: str, remote_path: str = "/sdcard/Download/himnario_backup.json") -> bool:
        """Push a local file to the connected Android device/emulator."""
        if not os.path.isabs(local_path):
            local_path = os.path.abspath(local_path)
        result = subprocess.run(["adb", "push", local_path, remote_path], capture_output=True, text=True)
        return result.returncode == 0

    @staticmethod
    def get_shared_preference_value(key: str, pref_file: str = "sharedPrefs.xml") -> str:
        """Retrieve a specific preference string or boolean value from the app's shared preferences."""
        cmd = f"run-as com.pentecostal.himnarioprincipal cat /data/data/com.pentecostal.himnarioprincipal/shared_prefs/{pref_file}"
        result = subprocess.run(["adb", "shell", cmd], capture_output=True, text=True)
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if f'name="{key}"' in line:
                    return line.strip()
        return ""
