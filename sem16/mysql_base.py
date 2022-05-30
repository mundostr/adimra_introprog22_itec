""" Ejemplo conexión a servidor de bases de datos relacionales (Mysql) """


import mysql.connector

credenciales = mysql.connector.connect(
    host="idyd.ar", # localhost
    user="adimra",
    password="adm1727",
    database="adimra"
)


def consultar_bbdd():
    conexion = credenciales.cursor()
    conexion.execute("SELECT lecturas.id, lecturas.media, sensores.nombre FROM lecturas, sensores WHERE lecturas.id_sensor = 32 AND lecturas.id_sensor = sensores.id") # lenguage SQL
    resultado = conexion.fetchall()
    print(resultado)



if (__name__ == "__main__"):
    consultar_bbdd()
