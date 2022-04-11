# Librerías
import random, string


# Constantes y variables
CTD_CLAVES = 5
CTD_CARACTERES = 8

apellido = "Perren"
nombre = "Carlos"
completo = apellido + ", " + nombre
clave = ""


# Procesos
for i in range(CTD_CLAVES):
    clave = ""
    
    for c in range(CTD_CARACTERES):
        # caracter_al_azar = random.choice("abcdefghijklmnopqrstuvwxyz")
        caracter_al_azar = random.choice(string.ascii_letters + string.digits)
        clave = clave + caracter_al_azar
    
    print(clave)
