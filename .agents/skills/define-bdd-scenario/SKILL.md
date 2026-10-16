---
name: define-bdd-scenario
description: Design and define BDD test scenarios with normalized nomenclature (SCN-xxx) and immediate registration in docs/test_scenarios.md.
---

# Skill: Define BDD Scenario

This skill guides the **conception, structuring, and documentation** of a new test scenario before technical implementation.

---

## 🎯 Scenario Deliverables

### 1. Normalized Nomenclature (Mandatory ID)
Every test scenario must start with a unique, sequential identifier based on the target module:

- `SCN-HOM-xxx`: Home & Quick Actions
- `SCN-LIS-xxx`: General Hymn List
- `SCN-DET-xxx`: Hymn Detail & Audio Player
- `SCN-FAV-xxx`: Favorites
- `SCN-CON-xxx`: Known Hymns
- `SCN-BUS-xxx`: Hymn Search
- `SCN-LST-xxx`: Custom Playlists
- `SCN-CLA-xxx`: Thematic Classification
- `SCN-SET-xxx`: Settings

> **Assignment Rule**: Check [**`docs/test_scenarios.md`**](file:///f:/Programming/GitHubCode-GutavoZHA/hymnal-automation-testing-apk-py/docs/test_scenarios.md) for the latest ID used in the module (e.g., if `SCN-BUS-006` exists, the next one is `SCN-BUS-007`).

---

### 2. Self-Explanatory Title
- Clear, concise, and declarative title expressing the action and expected outcome (e.g., *"SCN-BUS-002: Validate warning Toast when search query has fewer than 5 characters"*).
- A well-crafted title eliminates the need for redundant description fields.

---

### 3. BDD Step Structure
Draft the steps in a clear declarative format:
- **Given**: Initial application state or screen (e.g., *"Given the user is on the Search screen"*).
- **When**: Primary user interaction triggering the test (e.g., *"When typing 'des' into the search input and pressing search"*).
- **And**: Intermediate navigation or action steps, if needed.
- **Then**: Observable and verifiable assertion (e.g., *"Then a Toast message displaying 'El texto debe tener más de 5 caracteres' is shown"*).

> **App Language Note**: While test logic, code, and documentation are written in English, target strings that exist in the Spanish Android APK (such as hymn titles, button labels, and system toasts) must retain their exact Spanish text to avoid test failures.

---

### 4. Feature (Optional)
- The `Feature` clause is **optional** (inferred directly from the module name).
- The `Story` clause is omitted for conciseness.

---

## 📝 Immediate Documentation Registration

As soon as the scenario is defined (before writing code):

1. Open [**`docs/test_scenarios.md`**](file:///f:/Programming/GitHubCode-GutavoZHA/hymnal-automation-testing-apk-py/docs/test_scenarios.md).
2. Insert the new row into the corresponding module table:
   ```markdown
   | `SCN-BUS-007` | Search hymn with less than 5 characters and validate Toast | **Given** search screen $\rightarrow$ **When** search "des" $\rightarrow$ **Then** Toast alerts minimum length | `tests/test_search_page.py` |
   ```
3. Increment the total scenario counter in the summary header.

---

## 📋 Validation Checklist

- [ ] Does the ID follow the normalized convention (`SCN-<MOD>-xxx`)?
- [ ] Is the ID the next sequential number available in `docs/test_scenarios.md`?
- [ ] Is the title self-explanatory and declarative?
- [ ] Do the Given/When/Then steps define a concrete verification on the UI?
- [ ] Has the scenario been recorded in `docs/test_scenarios.md`?
