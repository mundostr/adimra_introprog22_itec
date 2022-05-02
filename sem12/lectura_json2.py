import json

RUTA = "sem12/clasificacion.json"  # path en inglés


def recuperarClasificacion(direccion):
    archivo = open(direccion, "r")  # r = read = modo solo lectura
    config = json.load(archivo)
    archivo.close()
    return config


def main():
    CLASIFICACION = recuperarClasificacion(RUTA)
    
    puntos = CLASIFICACION["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["points"]
    apellido = CLASIFICACION["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["familyName"]
    nombre = CLASIFICACION["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["givenName"]
    
    print(f"{apellido}, {nombre}: {puntos}")


if __name__ == "__main__":
    main()
