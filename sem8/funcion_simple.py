# Importamos librería random para generar elementos al azar
# y librería string para algunas funcionalidades cómodas en manejo de cadenas
import random
import string


LONGITUD_CODIGO = 16
CTD_CODIGOS = 3


def generar_codigo():
    pass


for i in range(CTD_CODIGOS):
    # Definimos una variable para ser usada como tipo cadena de texto, vacía
    codigo = ""
    
    for c in range(LONGITUD_CODIGO):
        caracter_al_azar = random.choice(string.ascii_letters + string.digits)
        codigo = codigo + caracter_al_azar

    # return codigo

    # print("Código ramdom:", generar_codigo())
    print("Código random:", codigo)
