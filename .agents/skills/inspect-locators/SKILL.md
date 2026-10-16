---
name: inspect-locators
description: Android UI hierarchy inspection (XML/Maestro) and decoupled locator definition in locators/.
---

# Skill: Inspect UI & Define Locators

This skill provides guidelines for **detecting, extracting, and organizing UI selectors** for native Android components developed with Kotlin and XML layouts.

---

## 🎯 Selector Priority Hierarchy

To avoid flaky or slow tests, always enforce this selector precedence:

1. **Priority 1: Accessibility ID (`AppiumBy.ACCESSIBILITY_ID`)**
   - Targets `android:contentDescription`.
   - Example: `(AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer")`
2. **Priority 2: Resource ID (`AppiumBy.ID`)**
   - Targets the `android:id` defined in XML layout files.
   - In this project, include the full package resource identifier:
     `com.pentecostal.himnarioprincipal:id/<element_id>`
   - Example: `(AppiumBy.ID, "com.pentecostal.himnarioprincipal:id/bBuscar")`
3. **Priority 3: Native UiAutomator (`AppiumBy.ANDROID_UIAUTOMATOR`)**
   - Ideal for dynamic scrolling within `RecyclerView` / `ScrollView` or exact text matches.
   - Scroll example:
     ```python
     (AppiumBy.ANDROID_UIAUTOMATOR,
      'new UiScrollable(new UiSelector().resourceId("com.pentecostal.himnarioprincipal:id/scrollCustom")).scrollIntoView(new UiSelector().text("Himnos para Niños"))')
     ```
4. **Priority 4: Direct Relative XPath (`AppiumBy.XPATH`)**
   - **Never** use absolute paths like `/hierarchy/android.widget.FrameLayout/...`.
   - Use only direct relative attributes or parent-child queries:
     ```python
     (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.pentecostal.himnarioprincipal:id/tittle_record' and @text='Ven']")
     ```

---

## 🛠️ Recommended Inspection Tools

- **Maestro MCP**: Run `maestro mcp` for interactive live UI hierarchy inspection and instant element validation.
- **ADB Shell Dump**:
  ```bash
  adb shell uiautomator dump /sdcard/view.xml
  adb pull /sdcard/view.xml .
  ```

---

## 📁 Code Conventions in `locators/<module>_locators.py`

1. Every screen or reusable component has its own file in `locators/`.
2. Static locators are defined as uppercase class tuple constants.
3. Dynamic locators (parametrized by title, number, or category) are implemented as `@staticmethod`:

```python
from appium.webdriver.common.appiumby import AppiumBy

class SearchLocators:
    SEARCH_INPUT = (AppiumBy.ID, "com.pentecostal.himnarioprincipal:id/editTextSearch")
    SEARCH_BUTTON = (AppiumBy.ID, "com.pentecostal.himnarioprincipal:id/buttonSearch")
    TOAST_MESSAGE = (AppiumBy.XPATH, "//android.widget.Toast")

    @staticmethod
    def result_item_by_text(title_text: str):
        return (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='com.pentecostal.himnarioprincipal:id/tittle_record' and @text='{title_text}']"
        )
```

---

## 📋 Validation Checklist

- [ ] Does the locator reside in the correct file in `locators/`?
- [ ] Was `ACCESSIBILITY_ID` or `ID` preferred over `XPATH`?
- [ ] If `XPATH` was used, is it strictly relative and scoped?
- [ ] Are constant names clear, descriptive, and in `UPPER_SNAKE_CASE`?
