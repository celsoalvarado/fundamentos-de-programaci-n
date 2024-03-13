import numpy as np

# Definir el número de ciudades, días de la semana y semanas
num_ciudades = 3
dias_semana = 7
num_semanas = 4

# Generar datos aleatorios para las temperaturas (puedes reemplazarlo con datos reales)
temperaturas = np.random.randint(20, 35, size=(num_ciudades, dias_semana, num_semanas))

# Mostrar la matriz de temperaturas
print("Matriz de temperaturas:")
print(temperaturas)
print()

# Calcular el promedio de temperaturas por ciudad y semana
for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        promedio_temp = np.mean(temperaturas[ciudad, :, semana])
        print(f"Promedio de temperaturas para la Ciudad {ciudad + 1}, Semana {semana + 1}: {promedio_temp:.2f}°C")

