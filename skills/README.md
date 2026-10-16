# 🧠 Catálogo de Skills del Proyecto Hymnal Automation

Esta carpeta contiene los **skills modulares** para la automatización de pruebas móviles con Appium, Pytest, Page Object Model y Allure BDD.

---

## 🚀 Skill Principal (Orquestador)

- [**`create-automated-test`**](create-automated-test/SKILL.md): Orquestador del flujo integral de pruebas automatizadas en Hymnal Mobile App.

---

## 📦 Skills Especializados

1. [**`definir-escenario-bdd`**](definir-escenario-bdd/SKILL.md): Definición del escenario BDD con nomenclatura normalizada (`SCN-xxx`), título autoexplicativo, estructura Given/When/Then, y registro inmediato en `docs/test_scenarios.md`.
2. [**`inspeccionar-locators`**](inspeccionar-locators/SKILL.md): Inspección de UI en Android (XML/Maestro) y definición de tuplas de locators desacoplados bajo jerarquía estricta de prioridad.
3. [**`implementar-page-object`**](implementar-page-object/SKILL.md): Implementación de métodos en Page Objects (`BasePage` / `MenuComponent`) con esperas explícitas y sin aserciones.
4. [**`escribir-test-allure`**](escribir-test-allure/SKILL.md): Codificación del test en Pytest con decoradores Allure BDD, código SCN en `@allure.title` y bloques `allure.step`.
5. [**`verificar-ejecucion-pruebas`**](verificar-ejecucion-pruebas/SKILL.md): Protocolo de verificación técnica (`--collect-only`), ejecución individual y validación visual con Allure Report.
