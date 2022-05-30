import requests

ID_SENSOR = 16
VALOR = 15.3
URL_API_POST = "http://pad19.com:3030/cargar_sensor"


def enviar_dato_sensor(params):
    solicitud = requests.post(URL_API_POST, json=params)
    
    if (solicitud.status_code == 200):
        return solicitud.json()
    return False


if (__name__ == "__main__"):
    parametros = { "sensor": ID_SENSOR, "valor": VALOR }
    proceso = enviar_dato_sensor(parametros)
    
    if (proceso == False):
        print("Error al conectar con el servidor de logs")
    else:
        print(proceso["mensaje"])
