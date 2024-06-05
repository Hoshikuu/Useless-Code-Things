#10000 lines in 4 seconds
#It can be more optimized

from faker import Faker
from time import time
import csv
from multiprocessing import Pool
from Clear import clear

fake = Faker()

head = ["Nombre","Email", "Direccion", "Texto"]

def GenerateLine(i):
    csvf = open("C:/Users/Cristian/Documents/py/DATOS/datosprue.csv", 'a', newline="")
    csvw = csv.DictWriter(csvf, head)
    csvw.writerow({"Nombre" : fake.name(), "Email" : fake.email(),"Direccion" : fake.address().replace("\n", ", "), "Texto" : fake.text().replace("\n", ", ")})
    del csvw
    csvf.close()

if __name__ == "__main__":
    registros = int(input("Cantidad de datos a generar: "))
    clear()
    
    with open("C:/Users/Cristian/Documents/py/DATOS/datos.csv", 'a', newline="") as csvf:
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
    
