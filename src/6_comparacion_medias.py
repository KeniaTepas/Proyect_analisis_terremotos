from funciones_comunes import cargar_datos, guardar_resultado
from scipy import stats

#Inferencias sobre medias de DOS muestras comparadas. 
# Muestras son (1900-1999) y (2000-2013)
def comparar_medias():
    datos = cargar_datos()
    antes = datos[datos['año'] < 2000]['mag']
    despues = datos[datos['año'] >= 2000]['mag']
    
    t_stat, p_valor = stats.ttest_ind(antes, despues, equal_var=False)
    
    guardar_resultado({
        'Media (1900-1999)': antes.mean(),
        'Media (2000-2013)': despues.mean(),
        'Diferencia': antes.mean() - despues.mean(),
        'Estadístico t': t_stat,
        'Valor p': f"{p_valor:.4e}",
        'Significativa? (α=0.05)': 'SÍ' if p_valor < 0.05 else 'NO'
    }, 'comparacion_medias_latam')
    print("Comparación de medias guardada")

if __name__ == "__main__":
    comparar_medias()