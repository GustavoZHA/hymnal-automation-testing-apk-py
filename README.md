# Hymnal Mobile Automation Framework

A scalable Appium automation framework for the Hymnal mobile app.

## Purpose

This repository contains a Python-based Appium automation framework built with:

- Python
- Appium
- Pytest
- Page Object Model (POM)
- Allure reporting
- Logging
- Environment configuration

## Project Structure

```bash
hymnal-automation-testing-apk-py/
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── .env.example
├── config/
│   ├── config.py
│   └── desired_caps.py
├── drivers/
│   └── driver_factory.py
├── pages/
│   ├── base_page.py
│   └── home_page.py
├── locators/
│   └── home_locators.py
├── tests/
│   └── test_home.py
├── utils/
│   ├── logger.py
│   └── screenshots.py
└── conftest.py
```

## Requirements

- Python 3.9+
- Appium Server
- Android SDK / ADB

## Setup

1. Clone the repository.
2. Create a virtual environment.
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment.
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS / Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env` and update values as needed.
   - The framework reads values from the system environment first, then from `.env`.
   - Set `APP_PATH` to the APK location if you store the app under `resources/app/`.
6. Start Appium.
   ```bash
   appium
   ```
7. Verify device connectivity.
   ```bash
   adb devices
   ```

## Run tests

```bash
pytest -v
```

## Generate Allure results

```bash
pytest --alluredir=reports/allure-results
```

## Open Allure report

```bash
allure serve reports/allure-results
```

## Notes

- Keep tests independent and reusable.
- Do not hardcode locators in tests.
- Use explicit waits instead of sleeps.
- Place sensitive values in `.env`.
