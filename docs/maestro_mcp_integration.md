# Integración de Maestro MCP con el Framework Appium + Python

## ¿Qué es Maestro MCP?

**Maestro MCP (Model Context Protocol)** permite a los asistentes de IA interactuar directamente con emuladores o dispositivos físicos Android/iOS en tiempo real. Ejecuta el servidor MCP integrado en Maestro mediante:

```bash
maestro mcp
```

## Beneficios para Aplicaciones Android (Kotlin + XML)

Las aplicaciones desarrolladas con **Kotlin y vistas XML clásicas** tienen características clave:
- Elementos identificables mediante `android:id` (por ejemplo: `@+id/btn_save`, `@+id/rv_hymns`, `@+id/toolbar`).
- Atributos de accesibilidad como `android:contentDescription`.
- Componentes clásicos como `RecyclerView`, `ViewPager2`, `FloatingActionButton`, `MaterialToolbar`, `TextView`.

Con **Maestro MCP**:
1. **Inspección rápida del árbol de vistas (View Hierarchy):** El agente puede consultar directamente la jerarquía de la pantalla activa del emulador sin tener que abrir herramientas pesadas como Appium Inspector manualmente.
2. **Detección de IDs y selectores:** Identifica con precisión los `resource-id` de los layouts XML y `contentDescription`.
3. **Validación interactiva:** Permite probar taps, scrolls e inputs de forma interactiva con el dispositivo antes de codificar la prueba definitiva en Appium.

## Configuración de Maestro MCP en Antigravity / Clientes MCP

### 1. Requisitos previos
- Tener instalado Maestro CLI:
  ```powershell
  # Windows (vía curl / bash o instalador oficial)
  curl -fsSL "https://get.maestro.mobile.dev" | bash
  ```
- Java 17 o superior.
- Emulador Android iniciado o dispositivo físico conectado por ADB (`adb devices`).

### 2. Configurar en `mcp_config.json` o configuración de Antigravity
Para habilitar el servidor MCP Maestro:
```json
{
  "mcpServers": {
    "maestro": {
      "command": "maestro",
      "args": ["mcp"]
    }
  }
}
```

## Flujo de Trabajo Híbrido: Maestro MCP + Appium Python

```text
+-------------------------+
|  Dispositivo / Emulador |
|  APK (Kotlin + XML)     |
+------------+------------+
             |
             +------------------------------+
             |                              |
             v                              v
    [ Maestro MCP Server ]         [ Appium Server 2.x ]
             |                              |
   - Inspección en vivo           - Ejecución de pruebas Pytest
   - Extracción de XML IDs        - Page Object Model (POM)
   - Pruebas exploratorias        - Reportes Allure y videos
             |                              |
             +--------------+---------------+
                            |
                            v
               [ Código de Automatización ]
               - locators/*.py
               - pages/*.py
               - tests/test_*.py
```

1. **Explorar con Maestro**: Se analiza la pantalla de la app en ejecución y se capturan los identificadores XML (`resource-id`, `content-desc`, `text`).
2. **Codificar en Appium**: Se añaden los locators en `locators/` y las acciones en `pages/` (Page Object Model).
3. **Ejecutar con Pytest**: Se corre la suite de pruebas oficial con generación de reportes Allure y grabación de videos automáticos.
