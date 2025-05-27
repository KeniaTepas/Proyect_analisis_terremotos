from funciones_comunes import cargar_datos, guardar_resultado, guardar_grafico
import seaborn as sns
import matplotlib.pyplot as plt

def analizar_correlacion():
    datos = cargar_datos()
    
    # 1. Cálculos para toda Latinoamérica (1900-2013)
    corr_total = datos['mag'].corr(datos['depth'])
    cov_total = datos[['mag', 'depth']].cov().iloc[0,1]
    
    # 2. Cálculos específicos para 2013
    datos_2013 = datos[datos['año'] == 2013]
    cov_2013 = datos_2013[['mag', 'depth']].cov().iloc[0,1] if not datos_2013.empty else None
    
    # Resultados
    resultados = {
        'Correlación (1900-2013)': corr_total,
        'Covarianza (1900-2013)': cov_total,
        'Covarianza (2013)': cov_2013 if cov_2013 is not None else 'No hay datos'
    }
    
    guardar_resultado(resultados, 'correlacion_latam')
    
    # Gráfico comparativo
    plt.figure(figsize=(12,6))
    
    # Gráfico 1900-2013
    plt.subplot(1,2,1)
    sns.scatterplot(x='depth', y='mag', data=datos, alpha=0.5)
    plt.title('Todos los terremotos (1900-2013)\n' + 
              f"Cov: {cov_total:.2f} | Corr: {corr_total:.2f}")
    
    # Gráfico 2013
    plt.subplot(1,2,2)
    if not datos_2013.empty:
        sns.scatterplot(x='depth', y='mag', data=datos_2013, color='red')
        plt.title(f"Terremotos de 2013\nCov: {cov_2013:.2f}")
    else:
        plt.text(0.5, 0.5, 'No hay datos para 2013', ha='center')
    
    plt.suptitle('Análisis de Correlación en Latinoamérica')
    guardar_grafico('correlacion_comparativa_latam')
    print("Análisis de correlación completo guardado")

if __name__ == "__main__":
    analizar_correlacion()