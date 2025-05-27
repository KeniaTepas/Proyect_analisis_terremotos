from funciones_comunes import cargar_datos
import subprocess

scripts = [
    '1_medidas_tendencia_central.py',
    '2_medidas_dispersion.py',
    '3_cuartiles_percentiles.py',
    '4_correlacion.py',
    '5_prueba_normalidad.py',
    '6_comparacion_medias.py',
    '7_probabilidades.py',
    '8_intervalos_confianza.py'
]

print("INICIANDO ANÁLISIS SÍSMICO LATINOAMÉRICA\n")
for script in scripts:
    print(f"\nEjecutando {script}...")
    subprocess.run(['python', f'src/{script}'])
print("\nTodos los análisis completados!")