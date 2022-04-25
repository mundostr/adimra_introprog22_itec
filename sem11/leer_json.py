import json


RUTA = "sem11/config.json"


def recuperarConfigJson(direccion):
	archivo = open(direccion, "r") # r = read = modo solo lectura
	config = json.load(archivo)
	archivo.close()
	return config


def main():
	CONFIG = recuperarConfigJson(RUTA)
	print(CONFIG["id"])


if (__name__ == "__main__"):
	main()