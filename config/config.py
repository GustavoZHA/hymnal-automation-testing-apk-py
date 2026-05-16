import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env if present, otherwise use OS environment variables.
dotenv_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=dotenv_path)

class Config:
    APPIUM_SERVER = os.getenv("APPIUM_SERVER", "http://127.0.0.1:4723")
    PLATFORM_NAME = os.getenv("PLATFORM_NAME", "Android")
    DEVICE_NAME = os.getenv("DEVICE_NAME", "Android Emulator")
    AUTOMATION_NAME = os.getenv("AUTOMATION_NAME", "UiAutomator2")
    APP_PATH = os.getenv("APP_PATH", "resources/app/hymnal.apk")
