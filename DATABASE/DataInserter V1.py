from psycopg2 import connect, DatabaseError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from time import time
from DatabaseConfig import config
import csv

def Connect(csvfile):
    connection = None
    try:  
        params = config()
        print("Connecting to the postgreSQL database ...")
        connection = connect(**params)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        print("Connected to the Database")

        print("Connecting the cursor ...")
        cursor = connection.cursor()
        print("Cursor connected")
        
        next(csvfile)
        print("Ejecutando comandos ...")

        startTime = time()
        for rows in csvfile:
            cursor.execute(f"INSERT INTO clientess (nombre, email, direccion, texto) VALUES ('{rows[0]}', '{rows[1]}', '{rows[2]}', '{rows[3]}');")
        stopTime = time()

        print("Todos los elementos añadidos")
        
        print("Datos añadidos a la base de datos en " + str(stopTime-startTime) + "s")

        cursor.fetchall()
        cursor.close()
    except(Exception, DatabaseError) as error:
        print(error)
    finally:
        if connect is not None:
            connection.close()
            print("Database connection terminated.")

if __name__ == "__main__":
    with open("C:/Users/Cristian/Documents/py/DATOS/datosprue.csv", 'r') as csvf:
        csvr = csv.reader(csvf)
        Connect(csvr)