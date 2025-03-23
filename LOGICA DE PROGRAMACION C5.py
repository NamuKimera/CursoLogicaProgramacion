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