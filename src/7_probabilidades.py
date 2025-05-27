from funciones_comunes import cargar_datos, guardar_resultado

def calcular_probabilidades():
    datos = cargar_datos()
    guardar_resultado({
        'P(Mag > 6.5)': (datos['mag'] > 6.5).mean(),
        'P(Mag ≥ 7.0)': (datos['mag'] >= 7.0).mean()
    }, 'probabilidades_latam')
    print("Probabilidades calculadas")

if __name__ == "__main__":
    calcular_probabilidades()