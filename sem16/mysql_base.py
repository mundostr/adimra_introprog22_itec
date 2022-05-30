""" Ejemplo conexión a servidor de bases de datos relacionales (Mysql) """


import mysql.connector

credenciales = mysql.connector.connect(
    host="idyd.ar", # localhost
    user="adimra",
    password="adm1727",
    database="adimra"
)

ID_SENSOR = 33


def consultar_bbdd(consulta):
    conexion = credenciales.cursor()
    conexion.execute(consulta) # lenguage SQL
    resultado = conexion.fetchall()

    return resultado



if (__name__ == "__main__"):
    consulta = f"""
        SELECT lecturas.id, lecturas.media, sensores.nombre
        FROM lecturas, sensores
        WHERE lecturas.id_sensor = {ID_SENSOR}
        AND lecturas.id_sensor = sensores.id
    """

    resultado = consultar_bbdd(consulta)
    
    print(resultado)
