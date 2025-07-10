# Logica de Programacion

# Clase 2 (OPERADORES)


# Operadores Aritmeticos

suma = 12 + 3

print(suma)

resta = 12 - 3

print(resta)

multiplicación = 12 * 3

print(multiplicación)


división = 12 / 3

print(división)

modulo = 16 % 3

print(modulo)

potencia = 12 ** 3

print(potencia)

divisionEntera = 18 // 5

print(divisionEntera)


# Operadores Relacionales

print(12 > 3) #devuelve True

print(12 < 3) #devuelve False

print(12 == 3) #devuelve False

print(12 >= 3) #devuelve True

print(12 <= 3) #devuelve False

print(12 != 3) #devuelve True


#Operadores de Pertenencia

frutas = ["manzana", "banana", "cereza"]

# Verificar si "banana" está en la lista
if "banana" in frutas:
    print("La banana está en la lista.")

# Verificar si "naranja" no está en la lista
if "naranja" not in frutas:
    print("La naranja no está en la lista.")

# Ejemplo con cadenas
texto = "Hola mundo"
if "Hola" in texto:
    print("La palabra 'Hola' está en el texto.")

# Ejemplo con un diccionario (verifica claves)
diccionario = {"a": 1, "b": 2}
if "b" in diccionario:
    print("La clave 'b' está en el diccionario.")

#Operadores de Identidad

a = 3
b = 3  
c = 4
print (a) is b # muestra True
print (a) is not b # muestra False
print (a) is not c # muestra True

x = 1
y = x
z = y
print (z) is 1 # muestra True
print (z) is x # muestra True

str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"
print (str1) is str2 # muestra True
print ("Code") is str2 # muestra False





