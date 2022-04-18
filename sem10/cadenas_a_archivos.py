"""
Modo w = write = escritura (si el archivo no existe, lo crea, y si existe lo trunca, es decir, lo limpia y luego graba)
Modo r = read = lectura (abre para solo lectura)
Modo a = append = añadir (si el archivo no existe, lo crea, y si existe lo añade al final)
"""


def guardar_cadena(cadena):
	archivo = open("sem10/cadena_formateada.txt", "w") # modo w = write = escritura
	archivo.write(cadena)
	archivo.close()
	print("Se ha guardado la cadena en el archivo")


def recuperar_cadena():
	archivo = open("sem10/cadena_formateada.txt", "r") # modo r = read = lectura
	lectura = archivo.read()
	archivo.close()
	print(lectura)


# Flujo principal
if (__name__ == "__main__"):
	apellido = "Perez"
	nombre = "Jose"
	edad = 20
	saldo = 358220.1
	activa = True
	
	cadena_formateada = f"Cadena de ejemplo: {apellido.upper()}, {nombre}, edad: {edad}, saldo: $ {saldo:.2f} AR\nEsta es otra linea"
	
	# guardar_cadena(cadena_formateada)
	recuperar_cadena()
