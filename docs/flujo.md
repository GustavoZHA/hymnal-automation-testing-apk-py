# 🗺️ Arquitectura y Diagrama de Flujo de la Aplicación

Este documento detalla el **entendimiento funcional y de navegación** de la aplicación móvil **Himnario Pentecostal** (`com.pentecostal.himnarioprincipal`), basado en la inspección de vistas XML, Page Objects, locators y casos de prueba automatizados.

---

## 1. Visión General de la Aplicación

La aplicación es un himnario digital nativo para Android (Kotlin + XML) orientado a la congregación, directores de culto y músicos. Permite:
- Consultar himnos organizados por número y título.
- Leer letras y estrofas completas.
- Reproducir pistas de audio acompañadas de controles multimedia.
- Marcar himnos como **Favoritos** y **Conocidos**.
- Crear y gestionar **Listas Personalizadas** para reuniones o cultos específicos.
- Explorar himnos agrupados por **Clasificación Temática** (Devocionales, Juventud, Niños, Santa Cena, etc.).
- Buscar himnos mediante filtros de texto o número con validaciones de entrada.
- Ajustar configuración visual y tipográfica (tamaño de fuente, tema).

---

## 2. Diagrama de Navegación Principal (Flujo Global)

El siguiente diagrama muestra el mapa general de pantallas y cómo el **Detalle del Himno** actúa como el punto de convergencia funcional de la app:

```mermaid
flowchart TD
    Start(["Inicio / App Launch"]) --> Home["Pantalla Principal (Home)"]

    %% Menú Superior y Drawer
    Home --> Drawer["Navigation Drawer / Menú Lateral"]
    Drawer --> Settings["Configuración (Settings)"]
    Drawer --> Home

    %% Accesos Principales desde Home
    Home -->|Botón Himnario| HymnList["Lista General de Himnos"]
    Home -->|Botón Buscar| Search["Pantalla de Búsqueda"]
    Home -->|Botón Favoritos| FavList["Pantalla de Favoritos"]
    Home -->|Botón Conocidos| KnownList["Pantalla de Conocidos"]
    Home -->|Botón Clasificación| Classif["Clasificación Temática"]
    Home -->|Botón Listas| CustomLists["Listas Personalizadas"]

    %% Convergencia al Detalle del Himno
    HymnList -->|Seleccionar por Título o Número| HymnDetail["Detalle del Himno"]
    Search -->|Resultado de búsqueda válido| HymnDetail
    FavList -->|Seleccionar himno favorito| HymnDetail
    KnownList -->|Seleccionar himno conocido| HymnDetail
    Classif -->|Seleccionar categoría| CategoryList["Lista Filtrada por Categoría"]
    CategoryList -->|Seleccionar himno| HymnDetail
    CustomLists -->|Abrir lista guardada| CustomListDetail["Himnos en Lista Personalizada"]
    CustomListDetail -->|Seleccionar himno| HymnDetail

    %% Acciones dentro del Detalle del Himno
    HymnDetail -->|Botón Home Bar| Home
    HymnDetail -->|Anterior / Siguiente| HymnDetail
    HymnDetail -->|Toggle Favorito| StateFav["Actualiza Estado Favorito"]
    HymnDetail -->|Toggle Conocido| StateKnown["Actualiza Estado Conocido"]
    HymnDetail -->|Agregar a Lista| PopupList["Popup: Seleccionar Lista Personalizada"]
    PopupList -->|Seleccionar lista destino| CustomLists
    HymnDetail -->|Botón Play| PlayerBar["Reproductor de Audio (Play / Pause / Seek / Rewind / Forward)"]
```

---

## 3. Flujos Detallados por Módulo

### 3.1. Flujo de Búsqueda y Validaciones de Entrada

La pantalla de búsqueda cuenta con reglas estrictas de validación que se comunican al usuario mediante mensajes Toast del sistema:

```mermaid
flowchart TD
    S_Start(["Usuario entra a Búsqueda"]) --> S_Input["Ingresar consulta en EditText"]
    S_Input --> S_Click["Presionar botón 'Buscar'"]
    S_Click --> S_Eval{"Evaluar tipo de entrada"}

    %% Validaciones negativas
    S_Eval -->|Texto con menos de 5 caracteres| T_Short["Toast: 'El texto debe tener más de 5 caracteres'"]
    S_Eval -->|Número fuera del rango permitido| T_Range["Toast: 'El número debe estar entre 1 al ...'"]
    S_Eval -->|Mezcla de números y letras| T_Mixed["Toast: 'No se permite mezclar texto y números'"]
    S_Eval -->|Caracteres especiales o símbolos| T_Invalid["Toast: 'Solo se permite texto o números entre 1 al ...'"]

    T_Short --> S_Input
    T_Range --> S_Input
    T_Mixed --> S_Input
    T_Invalid --> S_Input

    %% Validación exitosa
    S_Eval -->|Búsqueda válida: Título o Número| S_Results["Despliega RecyclerView con resultados"]
    S_Results --> S_Pick["Usuario presiona un resultado"]
    S_Pick --> S_Detail(["Abre Detalle del Himno"])
```

---

### 3.2. Flujo del Detalle del Himno y Reproductor Multimedia

El detalle del himno es la vista más rica de la aplicación, ya que integra lectura, audio y categorización personal:

```mermaid
flowchart TD
    D_Start(["Detalle del Himno Cargado"]) --> D_Render["Renderiza Título y Estrofas (TextViews)"]

    %% Acciones independientes
    D_Render --> D_Audio{"Interacción con Audio"}
    D_Audio -->|Pulsar Play| D_ShowPlayer["Muestra contenedor 'musicPlayerLayout'"]
    D_ShowPlayer --> D_Controls["Controles activos: Play / Pause, Rewind 10s, Forward 10s, SeekBar"]

    D_Render --> D_Meta{"Metadatos y Listas"}
    D_Meta -->|Pulsar Estrella/Favorito| D_Fav["Alterna flag de Favorito"]
    D_Meta -->|Pulsar Marca/Conocido| D_Known["Alterna flag de Himno Conocido"]
    D_Meta -->|Pulsar 'Añadir a Lista'| D_Popup["Abre Popup modal con listas creadas"]
    D_Popup -->|Selecciona lista| D_Saved["Vincula himno a la lista seleccionada"]
    D_Popup -->|Pulsar cerrar (X)| D_Render

    D_Render --> D_Nav{"Navegación Secuencial"}
    D_Nav -->|Botón Anterior| D_Prev["Carga himno con número (N - 1)"]
    D_Nav -->|Botón Siguiente| D_Next["Carga himno con número (N + 1)"]
    D_Nav -->|Botón Home Bar| D_Home(["Retorna a Home"])
```

---

## 4. Flujo de Listas Personalizadas (Gestión CRUD)

Permite al usuario crear listas temáticas para servicios de alabanza y asociarles himnos:

```mermaid
flowchart TD
    L_Start(["Acceso a 'Listas Personalizadas'"]) --> L_Check["Carga formulario y contenedor de listas"]

    %% Creación
    L_Check --> L_Create["Escribir nombre en 'nameListsSearch'"]
    L_Create --> L_PressCreate["Presionar botón 'Crear'"]
    L_PressCreate --> L_ToastCreate["Toast: '...creada exitosamente'"]
    L_ToastCreate --> L_RefreshList["Lista agregada al listado visual"]

    %% Limpieza
    L_Create -->|Pulsar limpiar| L_Clear["Campo se restablece al hint inicial"]

    %% Eliminación
    L_RefreshList --> L_Delete["Presionar botón eliminar en item de lista"]
    L_Delete --> L_Remove["Lista removida del listado visual"]

    %% Consulta de himnos asignados
    L_RefreshList --> L_OpenList["Pulsar sobre el nombre de la lista"]
    L_OpenList --> L_ViewHymns["Abre vista de himnos asociados a esa lista"]
    L_ViewHymns --> L_OpenHymn(["Abrir himno en Detalle"])
```

---

## 5. Clasificación Temática

La aplicación incluye un índice temático basado en el contenido doctrinal o de ocasión de cada himno:

```mermaid
flowchart TD
    C_Start(["Acceso a 'Clasificación'"]) --> C_Scroll["Vista scrollable 'scrollCustom' con categorías"]

    C_Scroll --> C_Cat1["1. Himnos Congregacionales para Reuniones Generales"]
    C_Scroll --> C_Cat2["2. Himnos para Servicio de Oración"]
    C_Scroll --> C_Cat3["3. Himnos para Cultos Devocionales"]
    C_Scroll --> C_Cat4["4. Himnos para Predicación al Aire Libre"]
    C_Scroll --> C_Cat5["5. Himnos de Marcha para Soldados de Jesucristo"]
    C_Scroll --> C_Cat6["6. Himnos para Niños"]
    C_Scroll --> C_Cat7["7. Himnos para la Juventud"]
    C_Scroll --> C_Cat8["8. Himnos de Bienvenida"]
    C_Scroll --> C_Cat9["9. Himnos para Santa Cena"]
    C_Scroll --> C_Cat10["10. Himnos para Consagración de Templos"]
    C_Scroll --> C_Cat11["11. Himnos para Ceremonia de Matrimonio"]

    C_Cat1 & C_Cat2 & C_Cat3 & C_Cat4 & C_Cat5 & C_Cat6 & C_Cat7 & C_Cat8 & C_Cat9 & C_Cat10 & C_Cat11 --> C_Filter["Filtra y muestra los himnos de la categoría elegida"]
    C_Filter --> C_Detail(["Abrir Detalle del Himno"])
```

---

## 6. Configuración (Ajustes de la App)

Accesible desde el menú lateral o actividad dedicada:

```mermaid
flowchart TD
    Set_Start(["Acceso a Configuración"]) --> Set_Options["Opciones disponibles"]

    Set_Options --> Set_Theme["Conmutador de Tema (Claro / Oscuro)"]
    Set_Options --> Set_FontInc["Aumentar tamaño de fuente (+FontSize)"]
    Set_Options --> Set_FontDec["Disminuir tamaño de fuente (-FontSize)"]
    Set_Options --> Set_MusicSwitch["Conmutador: Visibilidad de reproductor de música"]

    Set_Theme & Set_FontInc & Set_FontDec & Set_MusicSwitch --> Set_Persist["Ajustes guardados en preferencias de la app"]
```

---

## 7. Modelo Conceptual de Entidades y Estados

```mermaid
erDiagram
    HIMNO {
        int numero PK "Número del himno (ej. 1, 12)"
        string titulo "Título del himno"
        string contenido "Estrofas y coro"
        string audio_url "Pista o recurso musical"
        boolean es_favorito "Marcado en Favoritos"
        boolean es_conocido "Marcado en Conocidos"
    }

    CATEGORIA_CLASIFICACION {
        int id PK
        string nombre "Nombre de la categoría temática"
    }

    LISTA_PERSONALIZADA {
        string id PK
        string nombre "Nombre asignado por el usuario"
        datetime fecha_creacion
    }

    AJUSTES {
        boolean tema_oscuro
        int tamano_fuente
        boolean musica_visible
    }

    CATEGORIA_CLASIFICACION ||--o{ HIMNO : clasifica
    LISTA_PERSONALIZADA }o--o{ HIMNO : contiene
```

---

## 8. Sección de Notas y Correcciones del Usuario

> [!NOTE]
> Esta sección está reservada para tus observaciones, correcciones de flujos no evidentes en los XML/PageObjects, o detalles de lógica de negocio adicional que desees afinar.
