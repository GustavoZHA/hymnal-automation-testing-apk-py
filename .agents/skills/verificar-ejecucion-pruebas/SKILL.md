---
name: verificar-ejecucion-pruebas
description: Verificación de sintaxis, recolección con pytest --collect-only, ejecución individual y generación de reporte Allure.
---

# Skill: Verificar Ejecución de Pruebas

Este skill define el protocolo de **validación técnica, ejecución en dispositivo/emulador y diagnóstico de resultados** antes de dar por completado un test.

---

## 🎯 Protocolo de Verificación en 3 Fases

### Fase 1: Verificación de Recolección (Dry Run)
Comprueba que el archivo no contenga errores de sintaxis, imports rotos o incompatibilidades con Pytest:

```powershell
.\venv\Scripts\pytest.exe --collect-only
```
- **Criterio de Aceptación**: Debe listar el nuevo test bajo su módulo sin advertencias rojas ni `CollectionErrors`.

---

### Fase 2: Ejecución del Test Específico
Ejecuta únicamente el nuevo test para validar su estabilidad sin sobrecargar la suite completa:

```powershell
.\venv\Scripts\pytest.exe tests/test_<modulo>.py -k "test_<nombre_del_caso>" -v
```

Si se requiere imprimir salida de logs en consola en tiempo real:
```powershell
.\venv\Scripts\pytest.exe tests/test_<modulo>.py -k "test_<nombre_del_caso>" -v -s
```

---

### Fase 3: Generación del Reporte Allure y Diagnóstico
Generar los artefactos de Allure para comprobar la renderización de pasos y adjuntos:

```powershell
# 1. Ejecutar guardando resultados en reports/allure-results
.\venv\Scripts\pytest.exe tests/test_<modulo>.py -k "test_<nombre_del_caso>" --alluredir=reports/allure-results

# 2. Levantar el visualizador web de Allure
allure serve reports/allure-results
```

---

## 🔍 Diagnóstico de Fallos Comunes

| Síntoma | Causa Frecuente | Solución |
|---|---|---|
| `NoSuchElementException` | El elemento tarda en renderizar o el ID cambió en el XML. | Verificar con Maestro / ADB dump y asegurar que se use `wait_for_element`. |
| `TimeoutException` | La animación no ha terminado o la vista está oculta bajo scroll. | Usar `UiScrollable` o verificar visibilidad con `is_displayed`. |
| `StaleElementReferenceException` | La pantalla se redibujó mientras se interactuaba. | Relocalizar el elemento o refrescar la instancia del Page Object. |
| `AssertionError` | El texto, Toast o título devuelto no coincide. | Revisar si es un cambio funcional legítimo o un bug en la app. |

---

## 📋 Checklist de Validación

- [ ] ¿El test pasó exitosamente en ejecución individual (`PASSED`)?
- [ ] ¿La recolección general `pytest --collect-only` sigue limpia?
- [ ] ¿En Allure se despliegan los pasos BDD desplegables bajo el Epic y Feature correctos?
- [ ] En caso de fallo forzado, ¿se adjuntan el screenshot y el video automáticamente?
