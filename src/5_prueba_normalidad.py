from funciones_comunes import cargar_datos, guardar_resultado, guardar_grafico
from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def test_normalidad():
    datos = cargar_datos()
    magnitudes = datos['mag']
    
    # 1. Prueba de normalidad
    stat, p_valor = stats.normaltest(magnitudes)
    
    # 2. Resultados
    resultados = {
        'Estadístico (D\'Agostino-Pearson)': stat,
        'Valor p': p_valor,
        'Distribución normal? (α=0.05)': 'NO' if p_valor < 0.05 else 'SÍ'
    }
    guardar_resultado(resultados, 'normalidad_latam')
    
    # 3. Gráfico comparativo
    plt.figure(figsize=(10, 6))
    
    # Histograma de datos reales
    sns.histplot(magnitudes, bins=30, kde=False, stat='density', alpha=0.7, label='Datos reales')
    
    # Curva normal teórica
    x = np.linspace(magnitudes.min(), magnitudes.max(), 100)
    media, std = magnitudes.mean(), magnitudes.std()
    y = stats.norm.pdf(x, media, std)
    plt.plot(x, y, 'r-', linewidth=2, label='Distribución normal teórica')
    
    plt.title('Distribución de Magnitudes vs Normal Teórica\nLatinoamérica (1900-2013)')
    plt.xlabel('Magnitud (Richter)')
    plt.ylabel('Densidad')
    plt.legend()
    guardar_grafico('distribucion_magnitudes_latam')
    
    print("Prueba de normalidad completada")

if __name__ == "__main__":
    test_normalidad()