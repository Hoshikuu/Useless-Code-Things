#10000 lines in 2.5 seconds
#It can be more optimized
#May generate wrong lines among the data, cause the multiprocesing thing
#Faster generation but may have error generating the data
#Use this for generate larger CSV files

from faker import Faker
from time import time
import csv
from multiprocessing import Pool
from Clear import clear

fake = Faker()
filePath = "C:/Users/Cristian/Documents/py/DATOS/datos.csv" #Ruta del archivo que contendra los datos

def GenerateLine(i):
    with open(filePath, 'a', newline="") as csvf:
        csvw = csv.writer(csvf)
        csvw.writerow([fake.name(),fake.email(),fake.address().replace("\n", " "),fake.text().replace("\n", " ")])
        csvf.close()

if __name__ == "__main__":
    head = ["Nombre","Email", "Direccion", "Texto"]
    registros = int(input("Cantidad de datos a generar: "))
    clear()
    with open(filePath, 'a', newline="") as csvf:
        print("[!]      Escribiendo cabeceras")
        csvw = csv.DictWriter(csvf, head)
        csvw.writeheader()
        del csvw
        csvf.close()
        clear()

    print("[!]      Creando Pool de objetos")
    pool = Pool()
    clear()

    print("[...]    Generando Lineas de registros")
    startTime = time()
    pool.map(GenerateLine, range(registros))
    stopTime = time()
    clear()

    print("Se ha generado " + str(registros) + " en " + str(stopTime-startTime) + "s")
    
