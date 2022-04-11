"""
Objetivos:
# 1) permitir que el usuario pueda ingresar una clave
# 2) verificar ciertos criterios sobre ella utilizando una función
3) mostrar un mensaje de error si la clave no cumple con los criterios

Criterios:
# 1) La clave debe tener al menos 8 caracteres de longitud.
2) La clave debe tener al menos una letra mayúscula.
3) La clave debe tener al menos una letra minúscula.
4) La clave debe tener al menos un caracter especial.
5) La clave debe tener al menos un dígito.
"""


# Constantes y variables
CARACTERES_MINIMOS = 8

clave = "" # variable global
clave_valida = False


# Funciones
def solicitar_clave():
    global clave
    clave = input("Ingrese nueva clave: ")


def verificar_clave():
    global clave, clave_valida
    
    clave_valida = False

    if (len(clave) >= CARACTERES_MINIMOS):
        clave_valida = True


# Procesos, flujo principal, salidas
print("SISTEMA INICIADO")
solicitar_clave()
verificar_clave()

if (clave_valida == True):
    print("La clave ingresada es válida")
else:
    print("La clave ingresada no es válida")
