# Librerías
import random, string


# Constantes y variables
CTD_CLAVES = 3
CTD_CARACTERES = 8

apellido = "Perren"
nombre = "Carlos"
completo = apellido + ", " + nombre


def generar_clave():
    clave = ""
    
    for c in range(CTD_CARACTERES):
        # caracter_al_azar = random.choice("abcdefghijklmnopqrstuvwxyz")
        caracter_al_azar = random.choice(string.ascii_letters + string.digits)
        clave = clave + caracter_al_azar # concatenar
    
    print(clave)


# Procesos
print("Antes de la función")

for i in range(CTD_CLAVES):
    generar_clave()

print("Después de la función")
