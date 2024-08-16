#CONEXION SQL SERVER
#instalar pip install pyodbc
# Copyright (c) 2024 Rafael Almentero
import pyodbc

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=nameservers\nameinstance;'#Nombre del servido en el caso de ser mas especifico si contiene varia instancia se coloca el nombre del servidor y \ seguido de la instancia
    r'DATABASE=database;' #Base de daros a trabajar
    r'UID=username;'# Nombre del Usuario
    r'PWD=password;'# Contraseña
    r'PORT=1433;'# Puerto para una conexión mas eficiente por defecto 1433
)


# se uso este referencial para la prueba de comunicación pero ya el criterio es personal para cualquier otra modalidad
try:
    with pyodbc.connect(conn_str) as cnxn:
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM dbo.nombre-de-la-tabla")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except pyodbc.Error as ex:
    print('Error:', ex)       
