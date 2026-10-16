---
name: inspeccionar-locators
description: Inspección de UI en Android (XML/Maestro) y definición desacoplada de Locators en la carpeta locators/.
---

# Skill: Inspeccionar Locators

Este skill guía la **detección, extracción y organización de selectores de interfaz de usuario** para componentes de Android desarrollados en Kotlin y XML.

---

## 🎯 Jerarquía de Prioridad de Selectores

Para evitar pruebas frágiles o lentas, aplicar siempre este orden de precedencia:

1. **Prioridad 1: Accesibilidad (`AppiumBy.ACCESSIBILITY_ID`)**
   - Utiliza `android:contentDescription`.
   - Ejemplo: `(AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer")`
2. **Prioridad 2: ID de Recurso (`AppiumBy.ID`)**
   - Utiliza el `android:id` definido en los layouts XML.
   - En este proyecto siempre incluye el paquete completo:
     `com.pentecostal.himnarioprincipal:id/<nombre_id>`
   - Ejemplo: `(AppiumBy.ID, "com.pentecostal.himnarioprincipal:id/bBuscar")`
3. **Prioridad 3: UiAutomator Nativo (`AppiumBy.ANDROID_UIAUTOMATOR`)**
   - Ideal para scrolls dinámicos en listas o selección por texto exacto.
   - Ejemplo de scroll:
     ```python
     (AppiumBy.ANDROID_UIAUTOMATOR,
      'new UiScrollable(new UiSelector().resourceId("com.pentecostal.himnarioprincipal:id/scrollCustom")).scrollIntoView(new UiSelector().text("Himnos para Niños"))')
     ```
4. **Prioridad 4: XPath Relativo Directo (`AppiumBy.XPATH`)**
   - **Nunca** usar rutas absolutas tipo `/hierarchy/android.widget.FrameLayout/...`.
   - Usar solo con atributos directos o relaciones padre/hijo cortas:
     ```python
     (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.pentecostal.himnarioprincipal:id/tittle_record' and @text='Ven']")
     ```

---

## 🛠️ Herramientas de Inspección Recomendadas

- **Maestro MCP**: Ejecuta `maestro mcp` para inspección interactiva y extracción de la jerarquía de vistas en tiempo real.
- **ADB Shell Dump**:
  ```bash
  adb shell uiautomator dump /sdcard/view.xml
  adb pull /sdcard/view.xml .
  ```

---

## 📁 Convención de Código en `locators/<modulo>_locators.py`

1. Toda pantalla o componente tiene su archivo en `locators/`.
2. Los selectores fijos son tuplas constantes de clase en mayúsculas.
3. Los selectores dinámicos (que reciben texto o número por parámetro) se implementan como `@staticmethod`:

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

## 📋 Checklist de Validación

- [ ] ¿El locator pertenece al archivo correcto en `locators/`?
- [ ] ¿Se prefirió `ACCESSIBILITY_ID` o `ID` antes que `XPATH`?
- [ ] Si se usó `XPATH`, ¿es estrictamente relativo y específico?
- [ ] ¿Los nombres de las constantes son representativos y en `MAYUSCULAS_SNAKE_CASE`?
