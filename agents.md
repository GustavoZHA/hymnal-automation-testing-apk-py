# AGENTS.md — Hymnal Mobile Automation Framework

Este documento define la arquitectura de agentes, roles, responsabilidades y reglas operativas para la automatización del proyecto **Hymnal Mobile App** (APK desarrollado en **Kotlin y XML**), utilizando **Maestro MCP** como herramienta de inspección interactiva y **Appium + Python** como framework de automatización final.

---

## 1. Perfil del Proyecto

- **Tipo de Aplicación**: Aplicación móvil Android (APK nativo).
- **Tecnología de la App**: Kotlin con vistas tradicionales en XML (`ViewBinding`, `RecyclerView`, `TextView`, etc.).
- **Herramienta de Exploración e Inspección**: **Maestro MCP** (inspección de jerarquía de vistas en vivo, validación de selectores e interacción rápida en dispositivo).
- **Framework de Automatización**: **Appium (UiAutomator2) + Python (Pytest)**.
- **Patrón de Diseño**: Page Object Model (POM).
- **Reportes y Trazabilidad**: Allure Reports, Logging estructurado, captura de pantalla y grabación de video en fallos.

---

## 2. Roles y Agentes

### Agente 1: Lead Automation Architect (Arquitecto de Pruebas)
- **Misión**: Garantizar la integridad arquitectónica del framework, la separación de responsabilidades y la consistencia del código.
- **Responsabilidades**:
  - Validar que ninguna prueba acceda directamente a los drivers ni contenga locators hardcodeados.
  - Mantener la estructura modular: `drivers/`, `config/`, `locators/`, `pages/`, `tests/`, `utils/`, `data/`.
  - Asegurar la compatibilidad con CI/CD (GitHub Actions) y paralelismo (`pytest-xdist`).

### Agente 2: Maestro Inspector Agent (Exploración & Detección de UI)
- **Misión**: Utilizar **Maestro MCP** y comandos de Maestro para interactuar con la app en el emulador/dispositivo, extraer la jerarquía de vistas y obtener los selectores precisos del layout XML.
- **Responsabilidades**:
  - Ejecutar consultas de jerarquía mediante Maestro MCP para identificar componentes visuales.
  - Extraer los `resource-id` generados por el layout XML de Kotlin (ej. `package.name:id/btn_siguiente`, `package.name:id/tv_title`).
  - Identificar atributos de accesibilidad (`contentDescription`, texto visible).
  - Probar flujos interactivos preliminares antes de codificarlos en el framework de Appium.

### Agente 3: Appium Python Automation Engineer (Desarrollador de Pruebas)
- **Misión**: Traducir los hallazgos de Maestro a código limpio, robusto y mantenible en Appium y Python.
- **Responsabilidades**:
  - Implementar o actualizar archivos en `locators/` utilizando tuplas `(AppiumBy.ID, ...)` o `(AppiumBy.ACCESSIBILITY_ID, ...)`.
  - Implementar métodos de acción y verificación en `pages/` heredando de `BasePage`.
  - Escribir tests declarativos y legibles en `tests/` con fixtures de Pytest y anotaciones de Allure (`@allure.feature`, `@allure.story`, `@allure.step`).

### Agente 4: QA Quality & Diagnostics Agent (Monitoreo y Reportes)
- **Misión**: Supervisar las ejecuciones de prueba, diagnosticar fallos e interpretar resultados de Allure.
- **Responsabilidades**:
  - Analizar screenshots y videos capturados automáticamente en `reports/`.
  - Diferenciar entre bugs funcionales de la aplicación y problemas de sincronización/flakiness.
  - Asegurar que los tiempos de espera sean explícitos (`WebDriverWait`) y nunca pausas estáticas (`time.sleep`).

---

## 3. Reglas de Automatización para Apps Kotlin + XML

1. **Estrategia de Selección de Locators (Jerarquía de Prioridad)**:
   - **Prioridad 1**: `AppiumBy.ACCESSIBILITY_ID` (`android:contentDescription`).
   - **Prioridad 2**: `AppiumBy.ID` (`android:id` en los XML, ej. `id/item_title` o nombre completo de recurso).
   - **Prioridad 3**: `AppiumBy.ANDROID_UIAUTOMATOR` (para búsquedas por texto o scroll en listas).
   - **Prioridad 4**: `AppiumBy.XPATH` (únicamente con atributos relativos directos, nunca XPaths absolutos).

2. **Mapeo de Componentes Comunes de Android XML**:
   - `RecyclerView`: Manejar scrolls dinámicos mediante `UiScrollable` o utilidades de gestos en `utils/gestures.py`.
   - `MaterialToolbar` y Menús laterales: Utilizar el componente centralizado `pages/components/menu_component.py`.
   - `EditText`: Limpiar el campo antes de escribir (`element.clear()`, luego `send_keys`).

3. **Flujo de Trabajo entre Maestro y Appium**:
   ```
   [Maestro MCP] -> Detecta IDs / Jerarquía XML -> [locators/*.py] -> [pages/*.py] -> [tests/*.py] (Pytest)
   ```

---

## 4. Estructura de Directorios del Proyecto

```text
hymnal-automation-testing-apk-py/
├── agents.md                      # Definición de agentes y roles del proyecto
├── README.md                      # Documentación principal de inicio y ejecución
├── requirements.txt               # Dependencias Python
├── pytest.ini                     # Configuración de Pytest
├── conftest.py                    # Fixtures de sesión, driver, Allure y video
├── .env.example                   # Variables de entorno de ejemplo
├── assets/                        # Recursos visuales y estilos de documentación
├── config/                        # Configuraciones de driver y capabilities
├── drivers/                       # Factory y gestión de Appium Server
├── locators/                      # Selectores desacoplados por pantalla / componente
├── pages/                         # Clases Page Object Model (heredan de BasePage)
│   └── components/                # Componentes reutilizables (ej. menú, barra superior)
├── tests/                         # Casos de prueba Pytest
├── utils/                         # Utilidades (logger, capturas, videos, gestos, esperas)
├── data/                          # Datos de prueba en JSON
├── docs/                          # Documentación detallada del proyecto y Maestro MCP
├── skills/                        # Habilidades (skills) personalizadas para el asistente
└── resources/
    └── app/                       # APK de la aplicación (hymnal.apk)
```

---

## 5. Comandos Clave de Ejecución

- **Verificar dispositivos conectados**:
  ```bash
  adb devices
  ```
- **Iniciar Appium Server**:
  ```bash
  appium
  ```
- **Iniciar Maestro MCP**:
  ```bash
  maestro mcp
  ```
- **Ejecutar suite completa de tests**:
  ```bash
  pytest -v
  ```
- **Ejecutar generando reporte Allure**:
  ```bash
  pytest --alluredir=reports/allure-results
  ```
- **Visualizar reporte Allure en el navegador**:
  ```bash
  allure serve reports/allure-results
  ```
