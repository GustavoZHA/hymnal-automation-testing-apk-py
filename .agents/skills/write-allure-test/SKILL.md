---
name: write-allure-test
description: Author test cases in tests/ with Pytest and Allure BDD, integrating normalized scenario ID (SCN-xxx) in the title and step blocks.
---

# Skill: Write Tests with Allure BDD

This skill defines the technical standards, decorators, and best practices for writing clean, declarative test cases in the `tests/` directory using **Pytest** and **Allure BDD**.

---

## 🎯 Mandatory Rule: Scenario ID in the Title

The normalized identifier (`SCN-<MODULE>-<NUM>`) defined during `define-bdd-scenario` **must be placed at the start of `@allure.title`**:

```python
@allure.title("<SCN_ID>: <Self-explanatory title in English>")
```

### Title Nomenclature Examples:
- `@allure.title("SCN-HOM-001: Open hymn list from the Home main button")`
- `@allure.title("SCN-BUS-002: Validate warning Toast when search text has fewer than 5 characters")`
- `@allure.title("SCN-FAV-002: Add hymn to favorites and verify it opens from the Favorites list")`

> **Benefit**: In Allure Report, every test case maps 1:1 with the Master Test Scenarios Matrix in [**`docs/test_scenarios.md`**](file:///f:/Programming/GitHubCode-GutavoZHA/hymnal-automation-testing-apk-py/docs/test_scenarios.md).

---

## 🧩 Implementing BDD Steps (`allure.step`)

The test body must implement the Given/When/Then steps using `with allure.step(...)` blocks:

1. **Given**: Initial context, page instantiations, or preconditions.
2. **When**: User action triggering the workflow (click, type, scroll).
3. **And**: Complementary intermediate actions (optional).
4. **Then**: Concrete assertions verifying expected UI state.

---

## 🏗️ Complete Test Function Structure

```python
import allure
import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage

@allure.epic("Hymnal Mobile App")
@allure.feature("Hymn Search")
class TestSearchPage:

    @allure.title("SCN-BUS-002: Validate warning Toast when search text has fewer than 5 characters")
    def test_search_hymn_by_short_text_shows_validation_toast(self, driver):
        search_query = "des"

        with allure.step("Given the user navigates to the search screen"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"When searching with short query '{search_query}'"):
            search_page.search_hymn(search_query)

        with allure.step("Then a validation Toast alerting minimum character length is displayed"):
            toast_text = search_page.get_toast_message()
            assert toast_text == "El texto debe tener más de 5 caracteres", (
                f"Expected Toast 'El texto debe tener más de 5 caracteres', but got '{toast_text}'"
            )
```

---

## ⚠️ Assertion & Code Quality Standards

1. **Deterministic Assertions with Failure Messages**:
   - **Forbidden**: `assert True`.
   - **Required**: Explicit comparisons with clear bilingual context:
     ```python
     assert actual_title == expected_title, (
         f"Expected screen title to be '{expected_title}', but got '{actual_title}'"
     )
     ```
2. **Spanish Target Strings Handling**:
   - Because the target Android APK is localized in Spanish, UI assertions (titles, toast messages, hymn lyrics) must match the application's actual strings (e.g., `"Favoritos"`, `"Conocidos"`, `"Ven , ¡oh Todopoderoso!"`).
3. **Clean Imports**:
   - Only import from `pages/`, `locators/`, `utils/`, `allure`, and `pytest`.
4. **No Redundant Descriptions**:
   - `@allure.description` is omitted because the title and steps provide self-documenting clarity.

---

## 📋 Validation Checklist

- [ ] Does `@allure.title(...)` start with the normalized ID (`SCN-MOD-xxx: Title`)?
- [ ] Does the scenario ID match [**`docs/test_scenarios.md`**](file:///f:/Programming/GitHubCode-GutavoZHA/hymnal-automation-testing-apk-py/docs/test_scenarios.md)?
- [ ] Are all user actions and assertions wrapped in `with allure.step(...)` blocks?
- [ ] Does the test accept the `driver` fixture?
- [ ] Are all assertions deterministic with descriptive failure messages?
