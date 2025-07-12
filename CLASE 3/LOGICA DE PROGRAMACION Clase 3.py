# Logica de Programacion

# Clase 3 (COLECCIONES)

# Lista
mi_lista = [1, 2, "hola", 3.14]
print(mi_lista[0])  # Salida: 1
mi_lista.append(5)
print(mi_lista)  # Salida: [1, 2, 'hola', 3.14, 5]

# Tupla
mi_tupla = (1, 2, "hola", 3.14)
print(mi_tupla[1])  # Salida: 2

#creamos un array en Python de 3 posiciones [0, 1, 2]
colores = ["Rojo", "Negro", "Blanco"]

#definimos una variable con la posición que queremos visualizar
x = colores [1]

print(colores)

# Set
mi_set = {1, 2, 2, 3, 3, 3}
print(mi_set)  # Salida: {1, 2, 3}

# Diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario["nombre"])  # Salida: Juan

# Agregar un nuevo par clave-valor
mi_diccionario["profesion"] = "Ingeniero"

# Eliminar un par clave-valor
del mi_diccionario["edad"]

print(mi_diccionario)

# Iterar sobre las claves
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave])

import numpy as np

# Crear una matriz NumPy
matriz_np = np.array([])

# Acceder a un elemento
elemento_np = matriz_np  # Devuelve 2