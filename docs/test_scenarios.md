# 📋 Matriz de Escenarios de Prueba (Test Scenarios Matrix)

Este documento centraliza el inventario completo de los escenarios de prueba automatizados para la aplicación móvil **Hymnal Mobile App**. Sirve como punto único de consulta y seguimiento sin necesidad de inspeccionar el código fuente de cada archivo.

---

## 📊 Resumen de Cobertura

- **Total de Escenarios Registrados**: 38
- **Estructura BDD**: Allure BDD (`@allure.epic`, `@allure.feature`, `@allure.title` con ID normalizado, `allure.step`)

---

## 📑 Índice por Módulos (Features)

1. [Home y Accesos Rápidos](#1-home-y-accesos-rápidos) (7 escenarios)
2. [Lista General de Himnos](#2-lista-general-de-himnos) (2 escenarios)
3. [Detalle del Himno y Reproductor de Audio](#3-detalle-del-himno-y-reproductor-de-audio) (7 escenarios)
4. [Favoritos](#4-favoritos) (3 escenarios)
5. [Himnos Conocidos](#5-himnos-conocidos) (3 escenarios)
6. [Búsqueda de Himnos](#6-búsqueda-de-himnos) (6 escenarios)
7. [Listas Personalizadas](#7-listas-personalizadas) (7 escenarios)
8. [Clasificación Temática](#8-clasificación-temática) (2 escenarios)
9. [Configuración](#9-configuración) (1 escenario)

---

## 1. Home y Accesos Rápidos

**Archivos**: `tests/test_home.py` | `tests/test_home_actions.py`  
**Feature**: `Home`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-HOM-001` | Abrir lista de himnos desde el botón principal del Home | **Dado** Home $\rightarrow$ **Cuando** clic en 'Himnario' $\rightarrow$ **Entonces** se muestra la lista de himnos | `tests/test_home.py` |
| `SCN-HOM-002` | Navegar desde Home a la lista y abrir un himno por título | **Dado** Home $\rightarrow$ **Cuando** selecciona himno por título $\rightarrow$ **Entonces** se abre el detalle del himno | `tests/test_home.py` |
| `SCN-HOM-003` | Acceso directo a la pantalla de Búsqueda | **Dado** Home $\rightarrow$ **Cuando** clic en botón de búsqueda $\rightarrow$ **Entonces** se muestra SearchPage | `tests/test_home_actions.py` |
| `SCN-HOM-004` | Acceso directo a la pantalla de Favoritos | **Dado** Home $\rightarrow$ **Cuando** clic en botón de favoritos $\rightarrow$ **Entonces** se muestra sección Favoritos | `tests/test_home_actions.py` |
| `SCN-HOM-005` | Acceso directo a la pantalla de Conocidos | **Dado** Home $\rightarrow$ **Cuando** clic en botón de conocidos $\rightarrow$ **Entonces** se muestra sección Conocidos | `tests/test_home_actions.py` |
| `SCN-HOM-006` | Acceso directo a Listas Personalizadas | **Dado** Home $\rightarrow$ **Cuando** clic en botón listas personalizadas $\rightarrow$ **Entonces** se muestra ListPersonalityPage | `tests/test_home_actions.py` |
| `SCN-HOM-007` | Abrir menú lateral y retornar al Home | **Dado** Home $\rightarrow$ **Cuando** abre drawer y presiona Home $\rightarrow$ **Entonces** permanece/retorna a vista principal | `tests/test_home_actions.py` |

---

## 2. Lista General de Himnos

**Archivo**: `tests/test_hymn_list.py`  
**Feature**: `Lista de Himnos`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-LIS-001` | Abrir lista de himnos y seleccionar un himno por su título | **Dado** lista de himnos $\rightarrow$ **Cuando** pulsa por texto "Ven , ¡oh Todopoderoso!" $\rightarrow$ **Entonces** título coincide | `tests/test_hymn_list.py` |
| `SCN-LIS-002` | Abrir lista de himnos y seleccionar el himno #1 por su número | **Dado** lista de himnos $\rightarrow$ **Cuando** pulsa por número 1 $\rightarrow$ **Entonces** título es "1. Ven , ¡oh Todopoderoso!" | `tests/test_hymn_list.py` |

---

## 3. Detalle del Himno y Reproductor de Audio

**Archivo**: `tests/test_hymn_page.py`  
**Feature**: `Detalle del Himno`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-DET-001` | Verificar presencia del título en la pantalla de detalle | **Dado** detalle de himno $\rightarrow$ **Entonces** el título no debe estar vacío | `tests/test_hymn_page.py` |
| `SCN-DET-002` | Verificar que las estrofas del himno se carguen correctamente | **Dado** detalle de himno $\rightarrow$ **Cuando** obtiene estrofas $\rightarrow$ **Entonces** contiene al menos un elemento | `tests/test_hymn_page.py` |
| `SCN-DET-003` | Visualización del reproductor al reproducir el himno | **Dado** detalle de himno $\rightarrow$ **Cuando** pulsa Play $\rightarrow$ **Entonces** contenedor de reproductor visible | `tests/test_hymn_page.py` |
| `SCN-DET-004` | Alternar reproducción y pausa en el reproductor | **Dado** reproductor activo $\rightarrow$ **Cuando** pulsa Play/Pausa $\rightarrow$ **Entonces** reproductor permanece visible | `tests/test_hymn_page.py` |
| `SCN-DET-005` | Alternar estado de favorito en el himno | **Dado** detalle de himno $\rightarrow$ **Cuando** pulsa botón favorito $\rightarrow$ **Entonces** acción se completa con éxito | `tests/test_hymn_page.py` |
| `SCN-DET-006` | Marcar himno como conocido desde el detalle | **Dado** detalle de himno $\rightarrow$ **Cuando** pulsa marcar conocido $\rightarrow$ **Entonces** acción se completa con éxito | `tests/test_hymn_page.py` |
| `SCN-DET-007` | Navegación entre himnos anterior/siguiente y controles de rebobinado/avance | **Dado** detalle de himno $\rightarrow$ **Cuando** navega prev/next y controla audio $\rightarrow$ **Entonces** controles responden | `tests/test_hymn_page.py` |

---

## 4. Favoritos

**Archivo**: `tests/test_favoritos.py`  
**Feature**: `Favoritos`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-FAV-001` | Abrir pantalla de Favoritos desde Home y verificar título | **Dado** Home $\rightarrow$ **Cuando** entra a Favoritos $\rightarrow$ **Entonces** título es "Favoritos" | `tests/test_favoritos.py` |
| `SCN-FAV-002` | Agregar himno a favoritos y verificar su apertura desde la lista de Favoritos | **Dado** himno marcado como favorito $\rightarrow$ **Cuando** abre en Favoritos $\rightarrow$ **Entonces** abre el detalle esperado | `tests/test_favoritos.py` |
| `SCN-FAV-003` | Regresar al Home desde la pantalla de Favoritos | **Dado** pantalla Favoritos $\rightarrow$ **Cuando** pulsa Home $\rightarrow$ **Entonces** retorna a la vista principal | `tests/test_favoritos.py` |

---

## 5. Himnos Conocidos

**Archivo**: `tests/test_conocidos.py`  
**Feature**: `Himnos Conocidos`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-CON-001` | Abrir pantalla de Conocidos desde Home y verificar título | **Dado** Home $\rightarrow$ **Cuando** entra a Conocidos $\rightarrow$ **Entonces** título es "Conocidos" | `tests/test_conocidos.py` |
| `SCN-CON-002` | Marcar himno como conocido y verificar su acceso en la lista de Conocidos | **Dado** himno #12 marcado conocido $\rightarrow$ **Cuando** entra a Conocidos y abre #12 $\rightarrow$ **Entonces** detalle coincide | `tests/test_conocidos.py` |
| `SCN-CON-003` | Regresar al Home desde la pantalla de Conocidos | **Dado** pantalla Conocidos $\rightarrow$ **Cuando** pulsa Home $\rightarrow$ **Entonces** retorna a la vista principal | `tests/test_conocidos.py` |

---

## 6. Búsqueda de Himnos

**Archivo**: `tests/test_search_page.py`  
**Feature**: `Búsqueda de Himnos`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-BUS-001` | Verificar presencia de elementos en la pantalla de búsqueda | **Dado** pantalla búsqueda $\rightarrow$ **Entonces** campo de búsqueda y botón visibles | `tests/test_search_page.py` |
| `SCN-BUS-002` | Validar mensaje al ingresar texto menor a 5 caracteres | **Dado** búsqueda $\rightarrow$ **Cuando** busca "des" $\rightarrow$ **Entonces** Toast: "El texto debe tener más de 5 caracteres" | `tests/test_search_page.py` |
| `SCN-BUS-003` | Validar mensaje al ingresar número fuera de rango | **Dado** búsqueda $\rightarrow$ **Cuando** busca "9999" $\rightarrow$ **Entonces** Toast: "El número debe estar entre 1 al..." | `tests/test_search_page.py` |
| `SCN-BUS-004` | Validar mensaje al ingresar combinación alfanumérica no permitida | **Dado** búsqueda $\rightarrow$ **Cuando** busca "12abc" $\rightarrow$ **Entonces** Toast: "No se permite mezclar texto y números" | `tests/test_search_page.py` |
| `SCN-BUS-005` | Validar mensaje al ingresar caracteres especiales inválidos | **Dado** búsqueda $\rightarrow$ **Cuando** busca "@@@" $\rightarrow$ **Entonces** Toast: "Solo se permite texto o números..." | `tests/test_search_page.py` |
| `SCN-BUS-006` | Buscar himno por número y abrir resultado | **Dado** búsqueda $\rightarrow$ **Cuando** busca "1" $\rightarrow$ **Entonces** obtiene resultados y abre el himno en detalle | `tests/test_search_page.py` |

---

## 7. Listas Personalizadas

**Archivo**: `tests/test_list_personality.py`  
**Feature**: `Listas Personalizadas`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-LST-001` | Abrir pantalla de Listas Personalizadas y verificar título | **Dado** Home $\rightarrow$ **Cuando** abre Listas $\rightarrow$ **Entonces** título es "Listas Personalizadas" | `tests/test_list_personality.py` |
| `SCN-LST-002` | Verificar componentes principales de la pantalla | **Dado** Listas $\rightarrow$ **Entonces** input de nombre y botón crear visibles | `tests/test_list_personality.py` |
| `SCN-LST-003` | Verificar el texto de sugerencia (hint) del campo de nombre | **Dado** Listas $\rightarrow$ **Entonces** hint es "Escriba el nombre de Lista a Crear" | `tests/test_list_personality.py` |
| `SCN-LST-004` | Limpiar el campo de texto de nombre de lista | **Dado** texto escrito $\rightarrow$ **Cuando** limpia input $\rightarrow$ **Entonces** vuelve al estado inicial | `tests/test_list_personality.py` |
| `SCN-LST-005` | Crear una nueva lista personalizada exitosamente | **Dado** nombre dinámico $\rightarrow$ **Cuando** pulsa crear $\rightarrow$ **Entonces** Toast: "...creada exitosamente" | `tests/test_list_personality.py` |
| `SCN-LST-006` | Eliminar una lista personalizada existente | **Dado** lista creada $\rightarrow$ **Cuando** elimina por nombre $\rightarrow$ **Entonces** no aparece más en pantalla | `tests/test_list_personality.py` |
| `SCN-LST-007` | Agregar un himno a una lista personalizada y verificar su presencia | **Dado** lista creada $\rightarrow$ **Cuando** asocia himno desde detalle $\rightarrow$ **Entonces** aparece en la lista | `tests/test_list_personality.py` |

---

## 8. Clasificación Temática

**Archivo**: `tests/test_classification.py`  
**Feature**: `Clasificación`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-CLA-001` | Verificar apertura de la pantalla de Clasificación y su título | **Dado** datos esperados $\rightarrow$ **Cuando** entra a Clasificación $\rightarrow$ **Entonces** título coincide | `tests/test_classification.py` |
| `SCN-CLA-002` | Abrir y verificar la visualización de una categoría específica | **Dado** categoría de JSON $\rightarrow$ **Cuando** entra a categoría $\rightarrow$ **Entonces** está desplegada | `tests/test_classification.py` |

---

## 9. Configuración

**Archivo**: `tests/test_settings.py`  
**Feature**: `Configuración`

| ID | Título del Escenario | Resumen BDD | Archivo |
|---|---|---|---|
| `SCN-SET-001` | Interacción con los elementos de Configuración | **Dado** Settings $\rightarrow$ **Cuando** conmuta tema, fuente y audio $\rightarrow$ **Entonces** controles responden | `tests/test_settings.py` |

---

## 🛠️ Comandos de Ejecución Rápida

- **Ejecutar todos los escenarios**:
  ```bash
  .\venv\Scripts\pytest.exe -v
  ```

- **Ejecutar un módulo específico (ej. Búsqueda)**:
  ```bash
  .\venv\Scripts\pytest.exe tests/test_search_page.py -v
  ```

- **Ejecutar generando reporte Allure**:
  ```bash
  .\venv\Scripts\pytest.exe --alluredir=reports/allure-results
  allure serve reports/allure-results
  ```
