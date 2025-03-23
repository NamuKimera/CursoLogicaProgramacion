# Logica de Programacion Codigos Default

# Capitulo 3

variableDemo = 100

if variableDemo <= 0:
    print ("Infernape ha caido")
else:
    print("Infernape puede seguir")


#creamos un array en Python de 3 posiciones [0, 1, 2]
colores = ["Rojo", "Negro", "Blanco"]

#definimos una variable con la posición que queremos visualizar
x = colores [1]

#imprimimos el resultado en pantalla
print(x)

# Capitulo 4

# Definición de una función
def hayLugarAca(parametro1, parametro2):
    # cuerpo de la función
    return hayLugarAca

# Definición de un procedimiento
def IrAUnLugar(parametro1, parametro2):
    print("Salga de Ahi")


# Capitulo 5

#Parametros en Python
# Funciones
def tabla_del(numeroDeLaTabla, rangoADescribir):
    """
        PROP: Devuelve una lista correspondiente a los multiplos del Número **numeroDeLaTabla** 
              en un rango **rangoADescribir**
        PREC: Ninguna
        PARAM: * numeroDeLaTabla: Número - El numero de la lista a retornar
               * rangoADescribir: Número - El numero del rango de los multiplos a retornar
        TIPO: Lista
        OBS: El rango es limitado por ser un for
    """
    resultados = []
    for i in range(rangoADescribir):
         resultados.append(numeroDeLaTabla * i)
    return resultados

# Procedimientos
def saludo(nombre):
    """
        PROP: Saluda a una persona por su nombre **nombre**
        PREC: Ninguna
        PARAM: * nombre: String - El nombre de la persona a saludar
        OBS:
    """
    print(f'Hola {nombre}')

#Llenamos el Parametro con el Tipo de Dato correspondiente 

print(tabla_del(3, 5))

print(saludo('j2logo'))

# Tipos Personalizados

# Registros

