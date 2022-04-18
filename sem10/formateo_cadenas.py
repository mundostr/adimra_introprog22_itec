def main():
	apellido = "Pompin"
	nombre = "Pepe"
	edad = 40
	saldo = 15480.815

	# Opción 1: la propia función print concatena los argumentos que le paso separados por comas
	print("Cadena de ejemplo", apellido, ":", nombre, edad)

	# Opción 2: concatenar la cadena previamente.
	cadena = "Cadena de ejemplo: " + apellido + ", " + nombre + ", edad: " + str(edad) + ", saldo: $ " + str(saldo) + " AR"
	print(cadena)

	# Opción 3: emplear las utilidades formar o la macro f
	cadena_formateada = f"Cadena de ejemplo: {apellido.upper()}, {nombre}, edad: {edad}, saldo: $ {saldo:.2f} AR"
	print(cadena_formateada)


# Flujo principal
if (__name__ == "__main__"):
	main()
