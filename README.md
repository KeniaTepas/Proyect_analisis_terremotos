# Proyect_analisis_terremotos

**Análisis Estadístico de Terremotos de magnitud 6 o superior en Latinoamérica (1900-2013)**  
Este proyecto tiene como objetivo realizar un análisis estadístico exhaustivo de lo dicho anteriormente, a través del lenguaje Python.

---

## Instrucciones de Uso

1. Coloca tu archivo Excel en la carpeta `data/`.

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

   O instala las dependencias de manera conjunta en la carpeta del proyecto:

   ```bash
   pip install pandas numpy matplotlib seaborn scipy openpyxl python-dateutil
   ```

3. Ejecuta los scripts individualmente desde la carpeta `src/`:

   ```bash
   python src/1_medidas_tendencia_central.py
   python src/2_medidas_dispersion.py
   python src/3_cuartiles_percentiles.py
   python src/4_correlacion.py
   python src/5_prueba_normalidad.py
   python src/6_comparacion_medias.py
   python src/7_probabilidades.py
   python src/8_intervalos_confianza.py
   ```

   O ejecuta todos los análisis por completo con:

   ```bash
   python main.py
   ```

4. Los resultados se guardarán en la carpeta `resultados/`.

5. Los datos están en:

   ```
   data/Mag6PlusEarthquakes_1900-2013.xlsx
   ```
