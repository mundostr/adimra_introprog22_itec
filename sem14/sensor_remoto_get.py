from time import sleep

import requests

ID_SENSOR = 33
PERIODO_CTRL = 5 # segs
LIMITE_TEMP = 20.0
API_SENSOR_REMOTO = "http://pad19.com:3030/sensor33"


temperatura = 0.0
alarma_activada = False # flag


def main():
	global temperatura, alarma_activada
	
	# while(alarma_activada == False)
	while(not alarma_activada):
		conexion = requests.get(API_SENSOR_REMOTO)
		if (conexion.status_code == 200):
			contenido = conexion.json()
			
			if (contenido["estado"] == "ok"):	
				temperatura = contenido["valor"]
				if (temperatura < LIMITE_TEMP):
					alarma_activada = True
					print(f"Sensor #{ID_SENSOR}-> temperatura baja!: {temperatura:.1f} °C")
				else:
					print(f"Sensor #{ID_SENSOR}-> temperatura normal: {temperatura:.1f} °C")
					sleep(PERIODO_CTRL)
		
	# Alarma activada
	print(f"Alarma activada por sensor #{ID_SENSOR}, temperatura {temperatura}")
	alarma_activada = False
	main()


if (__name__ == "__main__"):
	main()
