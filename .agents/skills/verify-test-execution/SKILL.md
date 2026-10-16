---
name: verify-test-execution
description: Technical test verification, dry collection with pytest --collect-only, single test execution, and Allure report diagnostics.
---

# Skill: Verify Test Execution

This skill establishes the standard protocol for **technical validation, targeted device/emulator execution, and test report diagnostics** before completing a test story.

---

## 🎯 3-Phase Verification Protocol

### Phase 1: Dry Collection Verification (Syntax & Imports)
Ensures the test file does not introduce syntax errors, broken imports, or Pytest collection issues:

```powershell
.\venv\Scripts\pytest.exe --collect-only
```
- **Acceptance Criteria**: The test suite collects cleanly with no red warnings or `CollectionErrors`.

---

### Phase 2: Isolated Test Execution
Run only the specific test to evaluate stability without running the entire suite:

```powershell
.\venv\Scripts\pytest.exe tests/test_<module>.py -k "test_<case_name>" -v
```

To stream live logs and console outputs in real time:
```powershell
.\venv\Scripts\pytest.exe tests/test_<module>.py -k "test_<case_name>" -v -s
```

---

### Phase 3: Allure Report Generation & Diagnostics
Generate and view Allure test artifacts to verify BDD steps and visual attachments:

```powershell
# 1. Execute tests and store results
.\venv\Scripts\pytest.exe tests/test_<module>.py -k "test_<case_name>" --alluredir=reports/allure-results

# 2. Serve the web report locally
allure serve reports/allure-results
```

---

## 🔍 Diagnostic Reference for Common Failures

| Symptom | Probable Cause | Recommended Fix |
|---|---|---|
| `NoSuchElementException` | Element takes time to render or XML resource ID changed. | Verify using Maestro MCP or ADB dump; ensure BasePage explicit wait is used. |
| `TimeoutException` | Animation in progress or element is below current scroll viewport. | Utilize `UiScrollable` or re-check element visibility with `is_displayed`. |
| `StaleElementReferenceException` | View layout was redrawn during interaction. | Re-locate the element or re-instantiate the Page Object. |
| `AssertionError` | Text, Toast, or screen title does not match. | Verify whether the failure indicates an actual bug or a modified requirement. |

---

## 📋 Validation Checklist

- [ ] Did the individual test run pass cleanly (`PASSED`)?
- [ ] Is global test collection (`pytest --collect-only`) completely clean?
- [ ] Do Allure steps display properly under the designated Epic and Feature?
- [ ] On forced failure testing, are screenshots and video recordings automatically attached?
