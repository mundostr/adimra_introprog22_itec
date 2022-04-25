import json


RUTA = "sem11/config_alt.json"


def guardarConfigJson(direccion, contenido):
	archivo = open(direccion, "w") # w = write = modo escritura
	archivo.write(json.dumps(contenido))
	archivo.close()
	print("Config actualizada")


def main():
	datos = {
		"id": "12345678",
		"ciudad": "Rafaela",
		"pais": "Argentina",
		"interconectada": True
	}
	guardarConfigJson(RUTA, datos)


if (__name__ == "__main__"):
	main()