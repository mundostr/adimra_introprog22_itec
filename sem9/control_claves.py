"""
Objetivos:
# 1) permitir que el usuario pueda ingresar una clave
# 2) verificar ciertos criterios sobre ella utilizando una función
# 3) mostrar mensaje según la clave cumpla o no los criterios

Criterios:
# 1) La clave debe tener al menos 8 caracteres de longitud.
# 2) La clave debe tener al menos una letra mayúscula.
# 3) La clave debe tener al menos una letra minúscula.
# 4) La clave debe tener al menos un dígito.
# 5) La clave debe tener al menos un caracter especial.
"""


# Constantes y variables
CARACTERES_MINIMOS = 8
CADENA_MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CADENA_MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
DIGITOS = "0123456789"
CARACTERES_ESPECIALES = "@#$&_-"

clave = "" # variable global
clave_valida = False


# Funciones
def solicitar_clave():
    global clave
    
    print("La clave debe tener longitud mínima de 8 caracteres, mezclar mayúsculas, minúsculas, dígitos y caracteres especiales.")
    print("Caracteres especiales válidos: @#$&_-")

    clave = input("Ingrese nueva clave: ")


def verificar_clave():
    global clave_valida
    
    longitud_ok = False
    mayusculas_ok = False
    minusculas_ok = False
    digitos_ok = False
    especiales_ok = False
    
    clave_valida = False

    if (len(clave) >= CARACTERES_MINIMOS):
        longitud_ok = True
    
    for caracter in clave:
        if (caracter in CADENA_MAYUSCULAS):
            mayusculas_ok = True
        
        if (caracter in CADENA_MINUSCULAS):
            minusculas_ok = True
        
        if (caracter in DIGITOS):
            digitos_ok = True

        if (caracter in CARACTERES_ESPECIALES):
            especiales_ok = True

    if (longitud_ok and mayusculas_ok and minusculas_ok and digitos_ok and especiales_ok):
        clave_valida = True


# Procesos, flujo principal, salidas
print("SISTEMA INICIADO")
solicitar_clave()
verificar_clave()

if (clave_valida == True):
    print("La clave ingresada es válida")
else:
    print("La clave ingresada no es válida")
