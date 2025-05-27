# Proyect_analisis_terremotos
Análisis Estadístico de Terremotos de magnitud 6 o superior en Latinoamérica (1900-2013). Este proyecto tiene como objetivo realizar un análisis estadístico exhaustivo de lo dicho anteriormente, a través del lenguaje Python. 

# Instrucciones de Uso
-Coloca tu archivo Excel en la carpeta data/
-Instala las dependencias: pip install -r requirements.txt 
  O instala las dependencias de manera conjunta en la carpeta del proyecto: pip install pandas numpy matplotlib seaborn scipy openpyxl python-dateutil
-Ejecuta los scripts individualmente desde la carpeta src/:

  python src/1_medidas_tendencia_central.py
  python src/2_medidas_dispersion.py
  python src/3_cuartiles_percentiles.py
  python src/4_correlacion.py
  python src/5_prueba_normalidad.py
  python src/6_comparacion_medias.py
  python src/7_probabilidades.py
  python src/8_intervalos_confianza.py

  O ejecuta todos los análisis por completo con: python main.py

-Los resultados se guardarán en resultados/
-Los datos estan data\Mag6PlusEarthquakes_1900-2013.xlsx