from psycopg2 import connect, DatabaseError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from time import time, sleep
from DatabaseConfig import config
from os import system
from multiprocessing import Pool
from csv import reader

def clear():
     sleep(1)
     system("cls")

#########################################################

#print("[INFO] Conectandose al servidor de forma Global ...") #Eliminar luego
params = config()
connection = connect(**params)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

#Añadir datos a la base de datos de forma multinucleo
def Multiprocessor(csvfile):
    cursor.execute(f"INSERT INTO clientes (nombre, email, direccion, texto) VALUES ('{csvfile[0]}', '{csvfile[1]}', '{csvfile[2]}', '{csvfile[3]}');")

#Conectar a la base de datos
def Connect(csvfile):
    try:
        print("[...]    Conectandose a la base de datos PostgreSQL")
        connection = connect(**params)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) #Permiso para ejecutar comandos
        print("[!]      Conectado a la base de datos")
        clear()

        print("[...]    Conectando el cursor")
        cursor = connection.cursor()
        print("[!]      Cursor conectado")
        clear()

        next(csvfile)
        print("[...]    Inicializando comandos")
        clear()

        print("[!]      Creando Pool de objetos")
        pool = Pool()

        print("[...]    Agregando elementos a la base de datos")
        startTime = time()
        pool.map(Multiprocessor, csvr)
        stopTime = time()
        clear()
        print("[!]      Todos los elementos añadidos")
        pool.close()

        print("[!]      Datos añadidos a la base de datos en " + str(stopTime-startTime) + "s")

        cursor.close()
    except(Exception, DatabaseError) as error:
        print(error)
    finally:
        if connect is not None:
            connection.close()
            print("[!]      Cerrando conexion con la base de datos")

if __name__ == "__main__":
    with open("C:/Users/Cristian/Documents/py/DATOS/datoss.csv", 'r') as csvf:
        print("[!]      Leyendo fichero csv")
        csvr = reader(csvf)
        clear()
        print("[!]      Inicializando conexion con la base de datos")
        Connect(csvr)
        csvf.close()

    cursor.close()
    connection.close()