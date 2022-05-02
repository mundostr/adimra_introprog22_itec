import requests

APPID = "b07cceb706b36724ddaa2614cdb76af4"
ID_CIUDAD = "rafaela"
IDIOMA = "en"
RUTA = f"https://api.openweathermap.org/data/2.5/weather?q={ID_CIUDAD}&units=metric&appid={APPID}&lang={IDIOMA}"


solicitud = requests.get(RUTA)
solicitud_json = solicitud.json()
print(type(solicitud_json))
print(solicitud_json["weather"][0]["description"])
