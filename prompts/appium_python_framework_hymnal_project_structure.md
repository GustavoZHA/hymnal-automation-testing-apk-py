# Appium Python Automation Framework – Hymnal Mobile App

## Project Goal
Create a scalable and maintainable mobile automation framework using:

- Python
- Appium
- Pytest
- Page Object Model (POM)
- Allure Reports
- Logging
- CI/CD Ready Structure
- Android automation support

The framework will automate the Hymnal mobile application with features such as:

- Hymnal index
- Search
- Favorites
- Known hymns
- Hymn classification
- Personalized lists
- Settings
- Theme change
- Font size validation

---

# Recommended Tech Stack

| Tool | Purpose |
|---|---|
| Python | Programming language |
| Appium | Mobile automation |
| Pytest | Test runner |
| Selenium/Appium WebDriver | UI interaction |
| Allure | Reporting |
| Pytest-xdist | Parallel execution |
| Faker | Test data |
| Dotenv | Environment variables |
| Logging | Execution logs |
| GitHub Actions / Azure DevOps | CI/CD |

---

# Recommended Framework Structure

```bash
hymnal-app-automation/
│
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── .env
├── setup.py
│
├── config/
│   ├── config.py
│   ├── desired_caps.py
│   └── environments.json
│
├── drivers/
│   ├── driver_factory.py
│   └── appium_server.py
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── hymnal_page.py
│   ├── search_page.py
│   ├── favorites_page.py
│   ├── classification_page.py
│   ├── personalized_lists_page.py
│   └── settings_page.py
│
├── locators/
│   ├── home_locators.py
│   ├── hymnal_locators.py
│   ├── search_locators.py
│   ├── favorites_locators.py
│   ├── classification_locators.py
│   ├── personalized_lists_locators.py
│   └── settings_locators.py
│
├── tests/
│   ├── test_home.py
│   ├── test_hymnal.py
│   ├── test_search.py
│   ├── test_favorites.py
│   ├── test_classification.py
│   ├── test_personalized_lists.py
│   └── test_settings.py
│
├── utils/
│   ├── logger.py
│   ├── waits.py
│   ├── gestures.py
│   ├── screenshots.py
│   ├── test_data.py
│   └── helpers.py
│
├── data/
│   ├── hymns.json
│   └── users.json
│
├── reports/
│   ├── allure-results/
│   └── screenshots/
│
├── resources/
│   └── app/
│       └── hymnal.apk
│
└── .github/
    └── workflows/
        └── mobile-tests.yml
```

---

# Installation

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
Appium-Python-Client
pytest
pytest-html
allure-pytest
pytest-xdist
python-dotenv
faker
selenium
```

---

# Configure Appium

## Start Appium Server

```bash
appium
```

---

# Android Configuration

## Verify Devices

```bash
adb devices
```

---

# Desired Capabilities Example

## config/desired_caps.py

```python
from appium.options.android import UiAutomator2Options


def get_android_options():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.automation_name = "UiAutomator2"
    options.app = "resources/app/hymnal.apk"

    return options
```

---

# Driver Factory

## drivers/driver_factory.py

```python
from appium import webdriver
from config.desired_caps import get_android_options


class DriverFactory:

    @staticmethod
    def create_driver():
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            options=get_android_options()
        )

        driver.implicitly_wait(10)
        return driver
```

---

# Base Page

## pages/base_page.py

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text
```

---

# Example Locator File

## locators/home_locators.py

```python
from appium.webdriver.common.appiumby import AppiumBy


class HomeLocators:

    HYMNAL_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Himnario"
    )

    SEARCH_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Buscar"
    )

    FAVORITES_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Favoritos"
    )

    CLASSIFICATION_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Clasificación de Himnos"
    )
```

---

# Example Page Object

## pages/home_page.py

```python
from pages.base_page import BasePage
from locators.home_locators import HomeLocators


class HomePage(BasePage):

    def open_hymnal(self):
        self.click(HomeLocators.HYMNAL_BUTTON)

    def open_search(self):
        self.click(HomeLocators.SEARCH_BUTTON)

    def open_favorites(self):
        self.click(HomeLocators.FAVORITES_BUTTON)

    def open_classification(self):
        self.click(HomeLocators.CLASSIFICATION_BUTTON)
```

---

# Pytest Fixture

## conftest.py

```python
import pytest
from drivers.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver():
    driver = DriverFactory.create_driver()

    yield driver

    driver.quit()
```

---

# Example Test

## tests/test_home.py

```python
from pages.home_page import HomePage


class TestHome:

    def test_open_hymnal(self, driver):
        home = HomePage(driver)

        home.open_hymnal()

        assert True
```

---

# Suggested Test Scenarios

## Home Screen

- Validate home screen loads correctly
- Validate all menu buttons are visible
- Validate navigation to each section
- Validate side menu opens correctly

---

## Hymnal Index

Based on the screenshot:

- Validate hymn list is displayed
- Validate hymn numbers are visible
- Validate scroll functionality
- Validate hymn detail opens correctly
- Validate hymn content loads
- Validate back navigation

---

## Search Feature

- Search hymn by name
- Search hymn by number
- Validate invalid searches
- Validate empty search
- Validate search performance

---

## Favorites

- Add hymn to favorites
- Remove hymn from favorites
- Validate persistence after restart
- Validate duplicate prevention

---

## Classification Screen

Based on the image categories:

- Validate categories are displayed
- Validate category navigation
- Validate hymn list per category
- Validate scroll behavior

Example categories:

- Himnos Congregacionales para Reuniones Generales
- Himnos para Servicio de Oración
- Himnos para Cultos Devocionales
- Himnos para Predicación al Aire Libre
- Himnos para Niños
- Himnos para la Juventud

---

## Personalized Lists

Based on the screenshots:

- Create new list
- Delete list
- Validate duplicate names
- Add hymns to custom list
- Remove hymns from custom list
- Validate saved lists after app restart

---

## Settings Screen

Based on the settings image:

- Validate dark/light theme switch
- Validate text size increase
- Validate text size decrease
- Validate configuration persistence
- Validate visible music toggle

---

# Advanced Utilities

## Gesture Utility

## utils/gestures.py

```python
from appium.webdriver.common.appiumby import AppiumBy


class Gestures:

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        self.driver.swipe(500, 1500, 500, 500, 800)
```

---

# Logging

## utils/logger.py

```python
import logging


def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()
```

---

# Screenshot Utility

## utils/screenshots.py

```python
import os
from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def capture(driver, name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        path = f"reports/screenshots/{name}_{timestamp}.png"

        driver.save_screenshot(path)

        return path
```

---

# Allure Reports

## Execute Tests

```bash
pytest -v
```

## Generate Allure Results

```bash
pytest --alluredir=reports/allure-results
```

## Open Report

```bash
allure serve reports/allure-results
```

---

# Parallel Execution

```bash
pytest -n 2
```

---

# Pytest Configuration

## pytest.ini

```ini
[pytest]
addopts = -v --tb=short
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

---

# Recommended Improvements

## Add the following in future versions:

- Hybrid app support
- API testing integration
- Database validation
- Firebase validation
- OCR validation for lyrics
- AI-based visual validation
- Cloud execution with BrowserStack
- Docker support
- Jenkins integration
- Azure DevOps pipelines
- Retry mechanism for flaky tests
- Soft assertions
- Video recording on failures

---

# Recommended Design Pattern

## Page Object Model (POM)

Benefits:

- Better maintainability
- Reusable components
- Easy scalability
- Cleaner tests
- Better separation of concerns

---

# Naming Conventions

| Element | Convention |
|---|---|
| Test Files | test_feature.py |
| Page Files | feature_page.py |
| Locator Files | feature_locators.py |
| Classes | PascalCase |
| Methods | snake_case |
| Constants | UPPER_CASE |

---

# Best Practices

## Framework Best Practices

- Never hardcode locators inside tests
- Use explicit waits instead of sleep
- Keep tests independent
- Use reusable components
- Capture screenshots on failure
- Keep environment configuration externalized
- Use logging for debugging
- Keep test data separated

---

# Example Automation Roadmap

## Phase 1

- Setup framework
- Configure Appium
- Create base architecture
- Implement POM

## Phase 2

- Automate smoke tests
- Add reporting
- Add screenshots

## Phase 3

- Add regression suite
- Add parallel execution
- Integrate CI/CD

## Phase 4

- Add AI validations
- Add cloud device execution
- Add performance metrics

---

# Suggested Git Branch Strategy

```bash
main
 develop
  feature/home-tests
  feature/search-tests
  feature/settings-tests
```

---

# Suggested .gitignore

```gitignore
venv/
__pycache__/
.pytest_cache/
reports/
allure-results/
allure-report/
.env
.idea/
.vscode/
*.log
*.apk
```

---

# Final Recommendation

This project is ideal for implementing:

- Mobile automation best practices
- CI/CD pipelines
- Scalable Page Object Model architecture
- Advanced reporting
- AI-assisted testing strategies

The application screens already provide a strong foundation for:

- Functional testing
- UI validation
- Navigation testing
- Theme validation
- Personalized data testing
- Persistence testing
- Accessibility validation

