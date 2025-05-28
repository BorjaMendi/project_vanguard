
# Proyecto Vanguard
Análisis de clientes basado en datos demográficos y de actividad en la web de inversión Vanguard, enfocado en comprender patrones de inversión y uso del sistema por parte de distintos grupos de usuarios.

## Objetivo
Realizar un análisis exploratorio para segmentar clientes según:
- Balance de cuentas
- Frecuencia de logins
- Participación en test A/B

El objetivo final es observar si el nuevo diseño de interface conduce a mayores tasas de finalización del proceso y mejor experiencia de usuario.

## Estructura del análisis

### 1. Carga y limpieza de datos
- Conversión de tipos de datos
- Reordenamiento de columnas
- Transformación de variables (antigüedad en semanas/años)

### 2. Análisis univariado y bivariado
- Distribuciones de tenure, balances y logins
- Visualizaciones con histogramas, boxplots y countplots

### 3. Segmentación por quintiles
- Creación de rangos de inversión (muy baja a muy alta)
- Análisis de comportamiento dentro de los clientes con muy alta inversión

### 4. Comparación grupos control vs test
- Tasa de finalización del proceso
- Tasa de abandono del proceso
- Tasa de error del proceso 
- Tiempo de finalización por step y total
- Logins y balances por grupo
- Pruebas de hipótesis (Chi², t-test)


## Requisitos
- Python 3.10+
- pandas, matplotlib, seaborn, scipy
- Jupyter Notebook
- Tableau 

## Ejecución
Abrir el archivo `project_vanguard.ipynb` en Jupyter y ejecutar celdas paso a paso para reproducir el análisis.

---

Este proyecto fue desarrollado en el contexto de un bootcamp de análisis de datos, enfocado en el trabajo práctico con datasets reales.

Analistas de datos: Borja Mendieta y Lucía Ruiz. 
