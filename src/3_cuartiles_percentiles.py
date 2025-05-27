from funciones_comunes import cargar_datos, guardar_resultado

def calcular_distribucion():
    datos = cargar_datos()
    resultados = {
        'Primer cuartil (Q1)': datos['mag'].quantile(0.25),
        'Mediana (Q2)': datos['mag'].quantile(0.5),
        'Tercer cuartil (Q3)': datos['mag'].quantile(0.75),
        'Percentil 10 (P10)': datos['mag'].quantile(0.1),
        'Percentil 90 (P90)': datos['mag'].quantile(0.9)
    }
    guardar_resultado(resultados, 'cuantiles')
    print("Cuartiles y percentiles guardados")

if __name__ == "__main__":
    calcular_distribucion()