
# Proyecto Vanguard

Análisis de clientes basado en datos demográficos y de actividad, enfocado en comprender patrones de inversión y uso del sistema por parte de distintos grupos de usuarios.

## Objetivo
Realizar un análisis exploratorio para segmentar clientes según:
- Antigüedad (tenure)
- Balance de cuentas
- Frecuencia de logins
- Participación en test A/B

El objetivo final es obtener insights para orientar estrategias de fidelización y retención de clientes.

## Estructura del análisis

### 1. Carga y limpieza de datos
- Conversión de tipos de datos
- Reordenamiento de columnas
- Transformación de variables (e.g. antigüedad en semanas/años)

### 2. Análisis univariado
- Distribuciones de tenure, balances y logins
- Visualizaciones con histogramas, boxplots y countplots

### 3. Segmentación por quintiles
- Creación de rangos de inversión (muy baja a muy alta)
- Análisis de comportamiento dentro de cada segmento

### 4. Comparación grupos control vs test
- Tasa de finalización del proceso
- Logins y balances por grupo
- Pruebas de hipótesis (Chi², t-test)

### 5. Visualizaciones clave
- Barras, pastel, boxplots y scatterplots
- Segmentación por antigüedad, inversión y actividad

## Requisitos
- Python 3.10+
- pandas, matplotlib, seaborn, scipy
- Jupyter Notebook

## Ejecución
Abrir el archivo `project_vanguard.ipynb` en Jupyter y ejecutar celdas paso a paso para reproducir el análisis.

---

Este proyecto fue desarrollado en el contexto de un bootcamp de análisis de datos, enfocado en el trabajo práctico con datasets reales.
