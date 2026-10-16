# 🧠 Hymnal Automation Skills Catalog

This directory hosts the **modular automation skills** for mobile testing with Appium, Pytest, Page Object Model (POM), and Allure BDD.

---

## 🚀 Core Orchestrator Skill

- [**`create-automated-test`**](create-automated-test/SKILL.md): Master orchestrator coordinating the end-to-end mobile test lifecycle.

---

## 📦 Specialized Skills

1. [**`define-bdd-scenario`**](define-bdd-scenario/SKILL.md): Define BDD scenarios with normalized nomenclature (`SCN-xxx`), self-explanatory title, Given/When/Then structure, and immediate registration in `docs/test_scenarios.md`.
2. [**`inspect-locators`**](inspect-locators/SKILL.md): Inspect Android XML UI hierarchies (Maestro MCP / ADB) and declare decoupled locators under strict priority.
3. [**`implement-page-object`**](implement-page-object/SKILL.md): Implement Page Objects in `pages/` inheriting from `BasePage` or `MenuComponent` with explicit waits and no assertions.
4. [**`write-allure-test`**](write-allure-test/SKILL.md): Author declarative Pytest test functions with Allure BDD decorators, normalized SCN IDs in titles, and `allure.step` blocks.
5. [**`verify-test-execution`**](verify-test-execution/SKILL.md): 3-phase technical verification protocol (`--collect-only`, isolated test execution, and Allure report diagnostics).
