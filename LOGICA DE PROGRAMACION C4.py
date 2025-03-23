#creamos un array en Python de 3 posiciones [0, 1, 2]
colores = ["Rojo", "Negro", "Blanco"]

#definimos una variable con la posición que queremos visualizar
x = colores [1]

#imprimimos el resultado en pantalla
print(x)

# Definición de una función
def tabla_del(numero):
    resultados = []
    for i in range(11):
         resultados.append(numero * i)
    return resultados
 
res = tabla_del(3)

print(res)

# Definición de un procedimiento
def saludo(nombre):
    print(f'Hola {nombre}')     

print(saludo('j2logo'))