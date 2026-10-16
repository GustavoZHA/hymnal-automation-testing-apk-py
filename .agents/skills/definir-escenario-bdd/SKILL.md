---
name: definir-escenario-bdd
description: Definición y diseño de escenarios de prueba BDD con nomenclatura normalizada (SCN-xxx) y registro inmediato en docs/test_scenarios.md.
---

# Skill: Definir Escenario BDD

Este skill guía la **concepción, estructuración y registro documental** de un nuevo escenario de prueba antes de la implementación técnica.

---

## 🎯 Entregables del Escenario

### 1. Nomenclatura Normalizada (ID Obligatorio)
Todo caso de prueba debe iniciar con un identificador único consecutivo según el módulo:

- `SCN-HOM-xxx`: Home y Accesos Rápidos
- `SCN-LIS-xxx`: Lista General de Himnos
- `SCN-DET-xxx`: Detalle del Himno y Reproductor Multimedia
- `SCN-FAV-xxx`: Favoritos
- `SCN-CON-xxx`: Himnos Conocidos
- `SCN-BUS-xxx`: Búsqueda de Himnos
- `SCN-LST-xxx`: Listas Personalizadas
- `SCN-CLA-xxx`: Clasificación Temática
- `SCN-SET-xxx`: Configuración

> **Regla de asignación**: Consultar en `docs/test_scenarios.md` el último correlativo usado en el módulo (ej. si existe `SCN-BUS-006`, el siguiente será `SCN-BUS-007`).

---

### 2. Título Autoexplicativo
- Redacción directa, clara y concisa que exprese la acción y el resultado esperado (ej. *"Buscar himno con menos de 5 caracteres y validar Toast de advertencia"*).
- Al contar con un título autoexplicativo, **no es necesario añadir descripciones largas ni historias**.

---

### 3. Estructura de Pasos BDD
Redactar los pasos en formato declarativo:
- **Dado (Given)**: Estado inicial o pantalla de partida (ej. *"Dado que el usuario está en la pantalla de búsqueda"*).
- **Cuando (When)**: Interacción principal que desencadena la prueba (ej. *"Cuando ingresa 'des' en el campo y pulsa buscar"*).
- **Y (And)**: Pasos complementarios si se requieren.
- **Entonces (Then)**: Resultado esperado observable y medible (ej. *"Entonces se muestra el Toast 'El texto debe tener más de 5 caracteres'"*).

---

### 4. Feature (Opcional)
- La cláusula `Feature` es **opcional** (se asume directamente del módulo al que pertenece el archivo).
- La cláusula `Story` no se utiliza.

---

## 📝 Registro Inmediato en Documentación

Tan pronto como el escenario queda definido (antes de escribir código):

1. Abrir [**`docs/test_scenarios.md`**](file:///f:/Programming/GitHubCode-GutavoZHA/hymnal-automation-testing-apk-py/docs/test_scenarios.md).
2. Insertar la nueva fila en la tabla del módulo:
   ```markdown
   | `SCN-BUS-007` | Buscar himno con menos de 5 caracteres y validar Toast | **Dado** búsqueda $\rightarrow$ **Cuando** busca "des" $\rightarrow$ **Entonces** Toast alerta longitud mínima | `tests/test_search_page.py` |
   ```
3. Incrementar el contador general de escenarios en el encabezado de `docs/test_scenarios.md`.

---

## 📋 Checklist de Validación

- [ ] ¿El ID sigue la nomenclatura normalizada del módulo (`SCN-<MOD>-xxx`)?
- [ ] ¿El ID es el siguiente consecutivo disponible en `docs/test_scenarios.md`?
- [ ] ¿El título es claro y autoexplicativo por sí solo?
- [ ] ¿Los pasos Given/When/Then definen una verificación concreta en la app?
- [ ] ¿Se registró de inmediato la nueva fila en `docs/test_scenarios.md`?
