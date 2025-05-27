import numpy as np
from funciones_comunes import cargar_datos, guardar_resultado
from scipy import stats

def calcular_intervalos():
    datos = cargar_datos()
    mag = datos['mag']
    n = len(mag)
    
    # Intervalo para la media
    media = mag.mean()
    sem = stats.sem(mag)
    ic_media = stats.t.interval(0.95, n-1, loc=media, scale=sem)
    
    # Intervalo para proporción (Mag ≥7.0)
    p = (mag >= 7.0).mean()
    se_p = np.sqrt(p*(1-p)/n)
    z = stats.norm.ppf(0.975)
    ic_prop = (p - z*se_p, p + z*se_p)
    
    guardar_resultado({
        'Media muestral': media,
        'IC 95% (media)': f"({ic_media[0]:.4f}, {ic_media[1]:.4f})",
        'Proporción (Mag≥7)': p,
        'IC 95% (proporción)': f"({ic_prop[0]:.4f}, {ic_prop[1]:.4f})"
    }, 'intervalos_confianza_latam')
    print("Intervalos de confianza calculados")

if __name__ == "__main__":
    calcular_intervalos()