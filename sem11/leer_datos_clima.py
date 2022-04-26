"""
https://api.openweathermap.org/data/2.5/weather?q=rafaela&units=metric&appid=b07cceb706b36724ddaa2614cdb76af4
"""


import json


RUTA = "sem11/clima_rafaela.json" # path en inglés


def recuperarConfigJson(direccion):
	archivo = open(direccion, "r") # r = read = modo solo lectura
	config = json.load(archivo)
	archivo.close()
	return config


def main():
	CONFIG = recuperarConfigJson(RUTA)
	print(CONFIG["weather"][0]["description"])
	print(CONFIG["main"]["temp_min"])
	print(CONFIG["main"]["humidity"])
	print(CONFIG["main"]["pressure"])


if (__name__ == "__main__"):
	main()