import numpy as np

# Definir nombres de ciudades
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]

# Definir días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Definir el número de semanas
num_semanas = 4

# Crear una matriz 3D con temperaturas aleatorias
temperaturas = np.random.randint(20, 35, size=(len(ciudades), len(dias_semana), num_semanas))

# Mostrar la matriz de temperaturas
print("Matriz de temperaturas:")
print(temperaturas)
print()

# Calcular el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for j, dia in enumerate(dias_semana):
        promedio_semana = np.mean(temperaturas[i, j, :])
        print(f"{dia}: {promedio_semana:.2f} °C")
    print()