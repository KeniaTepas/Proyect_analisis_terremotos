from funciones_comunes import cargar_datos, guardar_resultado

def analizar_dispersion():
    datos = cargar_datos()
    resultados = {
        'Varianza muestral': datos['mag'].var(),
        'Desviación estándar': datos['mag'].std()
    }
    guardar_resultado(resultados, 'dispersion')
    print("Medidas de dispersión guardadas")

if __name__ == "__main__":
    analizar_dispersion()