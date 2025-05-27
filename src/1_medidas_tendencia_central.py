from funciones_comunes import cargar_datos, guardar_resultado

def analizar_tendencia_central():
    datos = cargar_datos()
    resultados = {
        'Media de magnitud': datos['mag'].mean(),
        'Mediana': datos['mag'].median(),
        'Moda': float(datos['mag'].mode()[0])
    }
    guardar_resultado(resultados, 'tendencia_central_latam')
    print("Medidas de tendencia central guardadas")

if __name__ == "__main__":
    analizar_tendencia_central()