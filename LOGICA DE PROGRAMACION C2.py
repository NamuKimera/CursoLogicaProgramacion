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