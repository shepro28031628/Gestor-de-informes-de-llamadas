# 📊 Gestor de Informes de Llamadas - REN Consultores

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/es/docs/Web/JavaScript)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)

Una herramienta avanzada y ligera para el análisis y visualización de registros de llamadas (CDR). Diseñada específicamente para transformar archivos CSV/Excel en tableros de control interactivos y reportes ejecutivos listos para imprimir.

---

## ✨ Características Principales

- **📈 Dashboard Interactivo**: Visualización en tiempo real de KPIs críticos como llamadas únicas, efectividad de respuesta y promedio de charla.
- **🔍 Filtrado Inteligente**: Segmentación de datos por proyecto/cliente, estado de la llamada (Contestada, Ocupado, etc.), sentido (Entrante/Saliente) y rangos de fecha.
- **⚙️ Configuración Dinámica de Clientes**: Asocia números DID o destinos específicos a nombres de clientes mediante una interfaz intuitiva. Los ajustes se guardan localmente.
- **📊 Visualización de Datos**:
  - Tendencia diaria de volumen de llamadas.
  - Distribución por hora del día.
  - Análisis de productividad del Top 10 de extensiones/agentes.
  - Gráfico de pastel de estados de llamadas.
- **📄 Reportes PDF**: Vista optimizada para impresión (CSS Print) que genera documentos profesionales en formato horizontal.
- **🔌 Sincronización con la Planta**: trae las llamadas y encuestas directamente de la planta telefónica por API, para cualquier rango de fechas.
- **🛠️ Reconciliación de Datos**: Algoritmo que agrupa múltiples eventos de CDR (main_cdr y sub_cdr) bajo un mismo `uniqueid` para evitar duplicidad y mejorar la precisión.

---

## 🚀 Tecnologías Utilizadas

- **Frontend**: HTML5 Semántico, CSS3 (Gradients, Glassmorphism, Flexbox/Grid).
- **Librerías JS**:
  - [SheetJS (XLSX)](https://sheetjs.com/): Para el procesamiento de archivos Excel y CSV directamente en el navegador.
  - [Chart.js](https://www.chartjs.org/): Para la generación de gráficos dinámicos.
- **Fuentes**: [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) (vía Google Fonts).

---

## 🛠️ Cómo Utilizar

1.  **Abrir la Aplicación**: Simplemente abre el archivo `dashboard_llamadas_v3.html` en cualquier navegador moderno (Chrome, Edge, Firefox).
2.  **Cargar Datos**: 
    - Haz clic en "Seleccionar Archivo" o arrastra tu archivo CSV/XLSX directamente al navegador.
    - El sistema detectará automáticamente las columnas y procesará los datos.
3.  **Configurar Clientes**:
    - Ve a la sección de filtros y haz clic en "Ajustes".
    - Define los números telefónicos y el nombre del cliente correspondiente. Esto permite que el dashboard agrupe las llamadas correctamente.
4.  **Generar Reporte**:
    - Una vez cargados y filtrados los datos, haz clic en "Imprimir / PDF" para generar el informe final.

---

## 📁 Estructura del Proyecto

```text
Gestor de informes de Llamadas/
├── dashboard_llamadas_v3.html   # Aplicación principal (Single Page App)
├── logo.png                     # Identidad visual
├── script.ps1                   # Utilidad de análisis de color (Desarrollo)
└── README.md                    # Documentación del proyecto
```

---

## 🧠 Lógica de Procesamiento (CDR Reconciliación)

A diferencia de los visores de CSV convencionales, esta herramienta aplica una lógica de negocio específica para PBX:
- **Unique ID**: Se utiliza como clave primaria para agrupar todas las filas relacionadas a una misma llamada.
- **Criterio de Respuesta**: Una llamada se considera `ANSWERED` si al menos uno de sus eventos asociados tiene tiempo de conversación superior a 0 segundos.
- **Abandonadas en IVR**: Identifica automáticamente llamadas que no llegaron a una extensión interna (4 dígitos), clasificándolas como abandonadas para no penalizar el KPI de los agentes.

---

## 🔌 Sincronizar con la Planta (API)

Además de cargar el CSV a mano, el tablero puede traer las llamadas **directamente de la planta telefónica** a través de la *API de Reportes de Llamadas REN* (servidor MonitorRed).

1. Haz clic en **Conexión API** e ingresa:
   - **URL**: `http://181.49.161.210:3091` (fuera de la oficina) o `http://10.24.0.4:8091` (dentro de la red).
   - **API Key**: la clave entregada por Gestión de Tecnología (se guarda solo en tu navegador).
2. Elige el rango en **Desde / Hasta** y pulsa **Sincronizar Planta**.
3. Al cambiar las fechas se vuelve a consultar la planta automáticamente; los demás filtros (proyecto, estado, sentido) funcionan igual que con el archivo.

Con la API también se muestran las **Encuestas de Satisfacción** (IVR 7123: tecla 1 = Sí, tecla 2 = No) por pregunta y por proyecto, y los **Ajustes de Clientes** se guardan en el servidor para que todos usen los mismos números.

Documentación de la API (Swagger): `http://181.49.161.210:3091/docs`

> [!NOTE]
> Si publicas el tablero en un sitio **https** (por ejemplo GitHub Pages), el navegador bloqueará la API mientras esta use **http**. Abre el archivo localmente o publica la API con HTTPS.

---

## ✒️ Autor

Desarrollado para **REN Consultores**. 
*Transformando datos crudos en decisiones estratégicas.*

---
> [!TIP]
> Para mejores resultados al imprimir, asegúrate de habilitar la opción "Gráficos de fondo" en la configuración de impresión de tu navegador.
