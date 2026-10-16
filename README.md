# Hymnal Mobile Automation Framework

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Appium](https://img.shields.io/badge/Appium-UiAutomator2-EA5906?logo=appium&logoColor=white)](https://appium.io/)
[![Pytest](https://img.shields.io/badge/Pytest-9.1-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure Report](https://img.shields.io/badge/Allure-BDD_Reporting-6C3483?logo=qameta&logoColor=white)](https://qameta.io/allure-report/)
[![Android](https://img.shields.io/badge/Platform-Android_Native-3DDC84?logo=android&logoColor=white)](https://developer.android.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

An enterprise-grade, scalable mobile test automation framework designed for native Android applications (Kotlin & XML layouts). Built with **Python**, **Appium (UiAutomator2)**, **Pytest**, **Page Object Model (POM)**, and **Allure BDD**, integrated with **Maestro MCP** for live UI exploration.

---

## 🌟 Key Architecture Highlights

- **Page Object Model (POM)**: Strict separation of concerns across `locators/`, `pages/`, and `tests/`. Locators are completely decoupled as immutable tuples.
- **Allure BDD Living Documentation**: Test execution is organized by `Epic`, `Feature`, normalized Scenario IDs (`SCN-xxx`), and granular `allure.step` blocks (Given / When / Then).
- **Automated Failure Artifacts**: Automatic full-resolution screenshots and screen video recordings captured and attached upon test failure via [conftest.py](conftest.py).
- **Robust Synchronization**: 100% explicit wait strategy using `WebDriverWait` and expected conditions, eliminating static sleeps (`time.sleep`) and flakiness.
- **Interactive UI Inspection with Maestro MCP**: Rapid view hierarchy inspection and selector validation on live devices and emulators.
- **Multi-Environment Configuration**: Centralized environment and capabilities loading via `.env` and configuration management.
- **Bilingual Context Handling**: Test logic, architecture, and code are written in English, while target UI assertion values (hymn titles, toast validations) cleanly preserve the Spanish Android application locale.
- **Autonomous Agent Skills**: Equipped with 5 modular skills under `.agents/skills/` orchestrating test design, locator mapping, page object modeling, and execution verification.

---

## 📁 Repository Structure

```text
hymnal-automation-testing-apk-py/
├── .agents/skills/            # Agentic skills for automated test lifecycle
├── assets/                    # Presentation assets and stylesheets
├── config/                    # Driver capabilities and environment settings
├── drivers/                   # Appium Server and Driver Factory management
├── locators/                  # Decoupled UI selectors by screen/component
│   └── components/            # Reusable component locators (e.g., navigation bar)
├── pages/                     # Page Object Model classes (inherit from BasePage)
│   └── components/            # Reusable UI components (MenuComponent, TopBar)
├── tests/                     # Declarative Pytest test suites (Allure BDD)
├── utils/                     # Logger, screenshot, video recorder, gestures, waits
├── data/                      # Test data, fixtures, and JSON mocks
├── docs/                      # Technical documentation and test scenarios matrix
│   ├── test_scenarios.md      # Master Test Scenarios Matrix (38 scenarios)
│   ├── flujo.md               # End-to-end application flows & Mermaid diagrams
│   └── maestro_mcp_integration.md # Maestro MCP setup & inspection guide
├── resources/app/             # Target APK binaries and test artifacts
├── conftest.py                # Pytest session hooks, driver fixture & Allure attachments
├── pytest.ini                 # Pytest runner configuration
└── requirements.txt           # Framework dependencies
```

---

## 📋 Master Test Coverage Matrix

The suite covers **38 automated BDD scenarios** across 9 application modules:

| Module | Feature | Scenarios | Primary Scenarios Covered |
|---|---|:---:|---|
| **Home** | `Home` | 7 | Navigation to all main sections, Drawer menu toggle, Home bar return |
| **Hymn List** | `Lista de Himnos` | 2 | Open hymn by exact title, open hymn by index number |
| **Hymn Detail** | `Detalle del Himno` | 7 | Title rendering, lyrics verification, audio player controls, favorite/known toggles |
| **Favorites** | `Favoritos` | 3 | Add to favorites, open favorite hymn from list, return to Home |
| **Known Hymns** | `Himnos Conocidos` | 3 | Mark as known, access from repertoire list, return to Home |
| **Search** | `Búsqueda de Himnos` | 6 | Negative input validation (short text, range, alphanumeric, symbols) & search execution |
| **Custom Playlists** | `Listas Personalizadas` | 7 | Create playlist, name input validation, delete playlist, associate hymns via modal |
| **Classification** | `Clasificación` | 2 | Thematic category verification from JSON dataset, scrollable list rendering |
| **Settings** | `Configuración` | 1 | Theme toggle, font size increment/decrement, audio visibility toggle |

> For the complete scenario inventory, see the [**Master Test Scenarios Matrix (docs/test_scenarios.md)**](docs/test_scenarios.md).

---

## 🚀 Getting Started

### Prerequisites

- **Python**: 3.10+ (tested on Python 3.12)
- **Node.js & Appium**: `npm install -g appium`
- **UiAutomator2 Driver**: `appium driver install uiautomator2`
- **Android SDK & ADB**: Configured with `ANDROID_HOME` in system PATH
- **Java JDK**: JDK 11 or JDK 17 with `JAVA_HOME` set
- **Allure CLI**: `npm install -g allure-commandline` or via Scoop/Homebrew

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GustavoZHA/hymnal-automation-testing-apk-py.git
   cd hymnal-automation-testing-apk-py
   ```

2. **Create and activate a virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**:
   Copy `.env.example` to `.env` and adjust variables as necessary:
   ```bash
   cp .env.example .env
   ```

---

## 🧪 Test Execution

### 1. Verify Connected Android Device / Emulator
```bash
adb devices
```

### 2. Start Appium Server
```bash
appium
```

### 3. Dry Run / Test Collection
Verify syntax and test discovery without launching device sessions:
```bash
pytest --collect-only
```

### 4. Run Full Test Suite
```bash
pytest -v
```

### 5. Run Targeted Module Tests
```bash
# Run Hymn Search suite
pytest tests/test_search_page.py -v

# Run single test by scenario ID or function name
pytest -k "SCN-BUS-002" -v
```

### 6. Parallel Execution
Leverage `pytest-xdist` across multiple connected devices:
```bash
pytest -n 2 -v
```

---

## 📊 Allure Reporting

Generate rich, interactive HTML reports with step-by-step BDD timelines, execution logs, failure screenshots, and MP4 screen recordings:

```bash
# 1. Execute tests generating Allure raw data
pytest --alluredir=reports/allure-results

# 2. Serve the interactive Allure report in default browser
allure serve reports/allure-results
```

---

## 🔍 Interactive UI Exploration with Maestro MCP

This framework supports live inspection using **Maestro MCP** to explore native Android view hierarchies (`ViewBinding`, `RecyclerView`, `TextView`) directly:

```bash
maestro mcp
```

For complete integration and usage instructions, refer to the [**Maestro MCP Integration Guide**](docs/maestro_mcp_integration.md).

---

## 📚 Technical Documentation

- [**Master Test Scenarios Matrix**](docs/test_scenarios.md): Comprehensive 38-scenario inventory with Given/When/Then steps.
- [**Application Architecture & Flowcharts**](docs/flujo.md): Interactive Mermaid diagrams illustrating navigation, search validations, and player controls.
- [**Maestro MCP Integration**](docs/maestro_mcp_integration.md): Setup and command reference for UI exploration.
- [**Automation Skills Catalog**](skills/README.md): AI Agent skills designed for seamless test creation and maintenance.

---

## 👤 Author

**Gustavo Zepeda** — *Mobile Test Automation Engineer & SDET*  
- GitHub: [@GustavoZHA](https://github.com/GustavoZHA)
