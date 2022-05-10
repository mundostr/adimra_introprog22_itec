"""
Solicitud de datos remotos en formato json mediante librería requests
(si no se dispone de la librería, desde consola ejecutar pip install requests)
(para ver listado librerías oficiales: pypi.org)
Backup (copia de seguridad) local
Conceptos de peticiones, URLs y argumentos (parámetros)

"""


import json

import requests

APPID = str("b07cceb706b36724ddaa2614cdb76af4")
ID_CIUDAD = str("rafaela")
IDIOMA = str("en")
RUTA_CLIMA = str(f"https://api.openweathermap.org/data/2.5/weather?q={ID_CIUDAD}&units=metric&lang={IDIOMA}&appid={APPID}")
RUTA_CLIMA_LOCAL = "sem13/backup_clima.json"


def recuperar_remoto(ruta, formato):
	respuesta = requests.get(ruta)

	if (respuesta.status_code == 200): # 200 = todo OK
		if formato == "json":
			return respuesta.json()
	
	return False

def guardar_backup_local(ruta, modo, contenido):
	with open(ruta, modo, encoding="UTF-8") as archivo:
		archivo.write(json.dumps(contenido))
	print("Backup local guardado")


if (__name__ == "__main__"):
	datos_clima = recuperar_remoto(RUTA_CLIMA, "json")

	# if (datos_clima == False):
	if (datos_clima is False): # el uso de "is" en estos casos es más adecuado que "=="
		print("Error al recuperar info de clima")
	else:
		datos_clima_main = dict(datos_clima["main"])
		guardar_backup_local(RUTA_CLIMA_LOCAL, "w", datos_clima_main)
