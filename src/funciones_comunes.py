import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def cargar_datos():
    """Carga y filtra datos para Latinoamérica"""
    try:
        ruta = Path(__file__).parent.parent / 'data' / 'Mag6PlusEarthquakes_1900-2013.xlsx'
        datos = pd.read_excel(ruta)
        
        # Filtro para Latinoamérica (Centroamérica + Sudamérica)
        lat_min, lat_max = -56, 23  # Desde Tierra del Fuego hasta sur de México
        lon_min, lon_max = -118, -35  # Desde Pacífico hasta Atlántico
        
        latam = datos[
            (datos['latitude'].between(lat_min, lat_max)) & 
            (datos['longitude'].between(lon_min, lon_max))
        ].copy()
        
        latam['fecha'] = pd.to_datetime(latam['Date'])
        latam['año'] = latam['fecha'].dt.year
        
        print(f"Datos cargados: {len(latam)} terremotos en Latinoamérica (de {len(datos)} globales)")
        return latam
        
    except Exception as e:
        raise Exception(f"Error al cargar datos: {str(e)}")

def guardar_resultado(resultado, nombre_archivo):
    """Guarda resultados en .txt con formato profesional"""
    output_dir = Path(__file__).parent.parent / 'resultados' / 'tablas'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_dir / f"{nombre_archivo}.txt", 'w', encoding='utf-8') as f:
        if isinstance(resultado, dict):
            # Encabezado
            f.write("ANÁLISIS SÍSMICO LATINOAMÉRICA (1900-2013)\n")
            f.write("="*50 + "\n")
            # Contenido
            for k, v in resultado.items():
                if isinstance(v, float):
                    linea = f"{k.upper():<25}: {v:>10.4f}"
                else:
                    linea = f"{k.upper():<25}: {v:>10}"
                f.write(linea + "\n")
        else:
            f.write(str(resultado))

def guardar_grafico(nombre):
    """Guarda gráficos en la carpeta resultados/figuras"""
    fig_dir = Path(__file__).parent.parent / 'resultados' / 'figuras'
    fig_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(fig_dir / f"{nombre}.png", dpi=300, bbox_inches='tight')
    plt.close()