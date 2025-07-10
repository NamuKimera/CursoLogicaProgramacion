# Logica de Programacion

# Clase 1 (PRIMEROS PASOS)

' HOLA SOY UN COMENTARIO '

' Hola soy Namu '

"""
Hola soy un comentario
No soy Inuyasha, soy una imitación
Yo soy Namu Kimera

"""

def hayVRAMSuficienteAca() :
    """
        PROP.: Indica si en el PC Actual hay VRAM suficiente
        PREC.: Ninguna
        TIPO.: Booleano
        OBS: Si hay VRAM Suficiente en el PC, devuelve valor booleano TRUE, caso contrario, 
        devuelve el numero de VRAM que falta.
    """
    MoverAlMotherboardDelPCActual
    return(
        
    )

def MoverAlMotherboardDelPCActual(dirPrincipal, dirSecundaria) :
    """
        PROP.: Mueve el Cabezal a la Motherboard del PC Actual en un recorrido 
               al *dirPrincipal* y *dirSecundaria*
        PREC.: *dirPrincipal* y *dirSecundaria* no pueden ser iguales ni opuestas
        PARAM.: *dirPrincipal* dirección: es una dirección
                *dirSecundaria* dirección: es una dirección
        OBS: Si no hay mas recorrido hacia "dirPrincipal" y "dirSecundaria", hace BOOM.
    """


run = True
vidas = 100
dinero = 25

puntuacionPartida = vidas * dinero

print (puntuacionPartida)

if vidas <= 0:
    print ("Goku ha caido")
elif vidas == 0:
    print("Goku ha caido")
else:
    print("Infernape puede seguir")

while run:
    print("El combate ha comenzado")
    run = False

for i in range(7):
    print(f"faltan {i} minutos")


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


#Parametros en Python
# Funciones
def tablaDel_EnUnRangoDe_(numeroDeLaTabla, rangoADescribir):
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
        OBS: Si no se define un String como argumento del parametro, no da error
    """
    print(f'Hola {nombre}')

#Llenamos el Parametro con el Tipo de Dato correspondiente 

print(tablaDel_EnUnRangoDe_(3, 5))

print(saludo('Namu'))

# Tipos Personalizados

diccionario = {
    'nombre' : "Namu Kimera",
    'canal' : "KimeraInc. By NamuVT",
    'edad' : 20,
}

print(diccionario['nombre'])

if 'nombre' == None:
    print(True)
else:
    print(False)

if "edad" in diccionario:
    print(True)
    
class Auto:
    def __init__(self, marca, modelo, km) -> None:
        self.marca = marca
        self.modelo = modelo
        self.km = km

miAuto = Auto("Peugeot", "Cassan", 2000)

print(miAuto.km)