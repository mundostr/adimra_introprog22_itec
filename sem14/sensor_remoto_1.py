import requests

LIMITE_TEMP = 20.0
URL_SENSOR_REMOTO = "http://pad19.com:3030/sensor33"


def main():
	conexion = requests.get(URL_SENSOR_REMOTO)
	contenido = conexion.json()

	print(contenido)


if (__name__ == "__main__"):
	main()
