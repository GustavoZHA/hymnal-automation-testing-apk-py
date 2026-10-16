# 📋 Master Test Scenarios Matrix

This document centralizes the full inventory of automated test scenarios for the **Hymnal Mobile App**. It serves as a single source of truth for test coverage without inspecting individual test implementation files.

> **Localization Note**: While all scenario titles, steps, and documentation are written in English, target UI values from the Android APK (hymn titles, toast validations, and section headers) retain their exact Spanish strings to guarantee assertion fidelity.

---

## 📊 Coverage Summary

- **Total Automated Scenarios**: 38
- **BDD Framework**: Allure BDD (`@allure.epic`, `@allure.feature`, `@allure.title` with normalized ID, and `allure.step` blocks)

---

## 📑 Module Index (Features)

1. [Home & Quick Actions](#1-home--quick-actions) (7 scenarios)
2. [General Hymn List](#2-general-hymn-list) (2 scenarios)
3. [Hymn Detail & Audio Player](#3-hymn-detail--audio-player) (7 scenarios)
4. [Favorites](#4-favorites) (3 scenarios)
5. [Known Hymns](#5-known-hymns) (3 scenarios)
6. [Hymn Search](#6-hymn-search) (6 scenarios)
7. [Custom Playlists](#7-custom-playlists) (7 scenarios)
8. [Thematic Classification](#8-thematic-classification) (2 scenarios)
9. [Settings](#9-settings) (1 scenario)

---

## 1. Home & Quick Actions

**Files**: `tests/test_home.py` | `tests/test_home_actions.py`  
**Feature**: `Home`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-HOM-001` | Open hymn list from the Home main button | **Given** Home $\rightarrow$ **When** click on 'Himnario' $\rightarrow$ **Then** hymn list is displayed | `tests/test_home.py` |
| `SCN-HOM-002` | Navigate from Home to list and open hymn by title | **Given** Home $\rightarrow$ **When** select hymn by title $\rightarrow$ **Then** hymn detail is opened | `tests/test_home.py` |
| `SCN-HOM-003` | Quick access to Search screen | **Given** Home $\rightarrow$ **When** click on search button $\rightarrow$ **Then** SearchPage is displayed | `tests/test_home_actions.py` |
| `SCN-HOM-004` | Quick access to Favorites screen | **Given** Home $\rightarrow$ **When** click on favorites button $\rightarrow$ **Then** 'Favoritos' section is displayed | `tests/test_home_actions.py` |
| `SCN-HOM-005` | Quick access to Known Hymns screen | **Given** Home $\rightarrow$ **When** click on known hymns button $\rightarrow$ **Then** 'Conocidos' section is displayed | `tests/test_home_actions.py` |
| `SCN-HOM-006` | Quick access to Custom Playlists screen | **Given** Home $\rightarrow$ **When** click on custom playlists button $\rightarrow$ **Then** ListPersonalityPage is displayed | `tests/test_home_actions.py` |
| `SCN-HOM-007` | Open navigation drawer and return to Home | **Given** Home $\rightarrow$ **When** open drawer and click Home $\rightarrow$ **Then** stays/returns to main view | `tests/test_home_actions.py` |

---

## 2. General Hymn List

**File**: `tests/test_hymn_list.py`  
**Feature**: `Lista de Himnos`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-LIS-001` | Open hymn list and select hymn by title | **Given** hymn list $\rightarrow$ **When** select "Ven , ¡oh Todopoderoso!" $\rightarrow$ **Then** title matches | `tests/test_hymn_list.py` |
| `SCN-LIS-002` | Open hymn list and select hymn #1 by number | **Given** hymn list $\rightarrow$ **When** select hymn number 1 $\rightarrow$ **Then** title is "1. Ven , ¡oh Todopoderoso!" | `tests/test_hymn_list.py` |

---

## 3. Hymn Detail & Audio Player

**File**: `tests/test_hymn_page.py`  
**Feature**: `Detalle del Himno`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-DET-001` | Verify hymn title is present on detail screen | **Given** hymn detail $\rightarrow$ **Then** title must not be empty | `tests/test_hymn_page.py` |
| `SCN-DET-002` | Verify hymn verses load properly | **Given** hymn detail $\rightarrow$ **When** retrieve verses $\rightarrow$ **Then** contains at least one verse element | `tests/test_hymn_page.py` |
| `SCN-DET-003` | Audio player layout is displayed upon playback | **Given** hymn detail $\rightarrow$ **When** click Play $\rightarrow$ **Then** player container becomes visible | `tests/test_hymn_page.py` |
| `SCN-DET-004` | Toggle play and pause on audio player | **Given** player active $\rightarrow$ **When** click Play/Pause $\rightarrow$ **Then** player remains visible | `tests/test_hymn_page.py` |
| `SCN-DET-005` | Toggle favorite status on hymn | **Given** hymn detail $\rightarrow$ **When** click favorite button $\rightarrow$ **Then** action completes successfully | `tests/test_hymn_page.py` |
| `SCN-DET-006` | Mark hymn as known from detail screen | **Given** hymn detail $\rightarrow$ **When** click mark known button $\rightarrow$ **Then** action completes successfully | `tests/test_hymn_page.py` |
| `SCN-DET-007` | Navigate previous/next hymns and control audio seek/rewind | **Given** hymn detail $\rightarrow$ **When** click prev/next and seek controls $\rightarrow$ **Then** controls respond | `tests/test_hymn_page.py` |

---

## 4. Favorites

**File**: `tests/test_favoritos.py`  
**Feature**: `Favoritos`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-FAV-001` | Open Favorites screen from Home and verify title | **Given** Home $\rightarrow$ **When** open Favorites $\rightarrow$ **Then** title is 'Favoritos' | `tests/test_favoritos.py` |
| `SCN-FAV-002` | Add hymn to favorites and verify opening from Favorites list | **Given** hymn marked as favorite $\rightarrow$ **When** open from Favorites $\rightarrow$ **Then** opens expected hymn detail | `tests/test_favoritos.py` |
| `SCN-FAV-003` | Return to Home from Favorites screen | **Given** Favorites screen $\rightarrow$ **When** click Home $\rightarrow$ **Then** returns to Home page | `tests/test_favoritos.py` |

---

## 5. Known Hymns

**File**: `tests/test_conocidos.py`  
**Feature**: `Himnos Conocidos`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-CON-001` | Open Known Hymns screen from Home and verify title | **Given** Home $\rightarrow$ **When** open Known Hymns $\rightarrow$ **Then** title is 'Conocidos' | `tests/test_conocidos.py` |
| `SCN-CON-002` | Mark hymn as known and verify access from Known list | **Given** hymn #12 marked as known $\rightarrow$ **When** open #12 in Known $\rightarrow$ **Then** detail matches | `tests/test_conocidos.py` |
| `SCN-CON-003` | Return to Home from Known Hymns screen | **Given** Known screen $\rightarrow$ **When** click Home $\rightarrow$ **Then** returns to Home page | `tests/test_conocidos.py` |

---

## 6. Hymn Search

**File**: `tests/test_search_page.py`  
**Feature**: `Búsqueda de Himnos`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-BUS-001` | Verify search screen elements presence | **Given** search screen $\rightarrow$ **Then** search input and button are visible | `tests/test_search_page.py` |
| `SCN-BUS-002` | Validate warning Toast when search text has fewer than 5 characters | **Given** search screen $\rightarrow$ **When** query "des" $\rightarrow$ **Then** Toast: 'El texto debe tener más de 5 caracteres' | `tests/test_search_page.py` |
| `SCN-BUS-003` | Validate warning Toast when hymn number is out of range | **Given** search screen $\rightarrow$ **When** query "9999" $\rightarrow$ **Then** Toast: 'El número debe estar entre 1 al...' | `tests/test_search_page.py` |
| `SCN-BUS-004` | Validate warning Toast on invalid alphanumeric input | **Given** search screen $\rightarrow$ **When** query "12abc" $\rightarrow$ **Then** Toast: 'No se permite mezclar texto y números' | `tests/test_search_page.py` |
| `SCN-BUS-005` | Validate warning Toast on invalid special characters | **Given** search screen $\rightarrow$ **When** query "@@@" $\rightarrow$ **Then** Toast: 'Solo se permite texto o números...' | `tests/test_search_page.py` |
| `SCN-BUS-006` | Search hymn by number and open result | **Given** search screen $\rightarrow$ **When** query "1" $\rightarrow$ **Then** retrieves results and opens hymn detail | `tests/test_search_page.py` |

---

## 7. Custom Playlists

**File**: `tests/test_list_personality.py`  
**Feature**: `Listas Personalizadas`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-LST-001` | Open Custom Playlists screen and verify title | **Given** Home $\rightarrow$ **When** open Playlists $\rightarrow$ **Then** title is 'Listas Personalizadas' | `tests/test_list_personality.py` |
| `SCN-LST-002` | Verify main components on Custom Playlists screen | **Given** Playlists $\rightarrow$ **Then** name input and create button are visible | `tests/test_list_personality.py` |
| `SCN-LST-003` | Verify hint text in playlist name input | **Given** Playlists $\rightarrow$ **Then** hint is 'Escriba el nombre de Lista a Crear' | `tests/test_list_personality.py` |
| `SCN-LST-004` | Clear text in playlist name input | **Given** input with text $\rightarrow$ **When** clear input $\rightarrow$ **Then** reverts to default state | `tests/test_list_personality.py` |
| `SCN-LST-005` | Create a new custom playlist successfully | **Given** dynamic list name $\rightarrow$ **When** click create $\rightarrow$ **Then** Toast confirms creation | `tests/test_list_personality.py` |
| `SCN-LST-006` | Delete an existing custom playlist | **Given** existing playlist $\rightarrow$ **When** delete by name $\rightarrow$ **Then** no longer visible in list | `tests/test_list_personality.py` |
| `SCN-LST-007` | Add a hymn to a custom playlist and verify presence | **Given** playlist created $\rightarrow$ **When** assign hymn via popup $\rightarrow$ **Then** hymn appears in playlist | `tests/test_list_personality.py` |

---

## 8. Thematic Classification

**File**: `tests/test_classification.py`  
**Feature**: `Clasificación`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-CLA-001` | Open Thematic Classification screen and verify title | **Given** expected JSON data $\rightarrow$ **When** open Classification $\rightarrow$ **Then** title matches | `tests/test_classification.py` |
| `SCN-CLA-002` | Open and verify display of a specific thematic category | **Given** category from JSON $\rightarrow$ **When** click category $\rightarrow$ **Then** category is displayed | `tests/test_classification.py` |

---

## 9. Settings

**File**: `tests/test_settings.py`  
**Feature**: `Configuración`

| ID | Scenario Title | BDD Summary | File |
|---|---|---|---|
| `SCN-SET-001` | Interaction with Settings configuration toggles | **Given** Settings $\rightarrow$ **When** toggle theme, font, and audio $\rightarrow$ **Then** controls respond | `tests/test_settings.py` |

---

## 🛠️ Quick Execution Commands

- **Run all automated scenarios**:
  ```bash
  pytest -v
  ```

- **Run specific module (e.g., Search)**:
  ```bash
  pytest tests/test_search_page.py -v
  ```

- **Run with Allure reporting**:
  ```bash
  pytest --alluredir=reports/allure-results
  allure serve reports/allure-results
  ```
