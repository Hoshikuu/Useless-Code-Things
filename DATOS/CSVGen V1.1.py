#10000 lines in 5.5 seconds
#Generate data slower but it's more consistent
#Use this for generate small CSV files

from faker import Faker
from time import time
import csv

fake = Faker()
filePath = "C:/Users/Cristian/Documents/py/DATOS/datos.csv" #Ruta del archivo que contendra los datos
registros = int(input("Cantidad de datos a generar: "))

startTime = time()
with open(filePath, 'a', newline="") as csvf:
    head = ["Nombre","Email", "Direccion", "Texto"]
    csvw = csv.DictWriter(csvf, head)
    csvw.writeheader() 
    for i in range(registros):
        csvw.writerow({"Nombre" : fake.name(), "Email" : fake.email(),"Direccion" : fake.address().replace("\n", ", "), "Texto" : fake.text().replace("\n", ", ")})
    del csvw
    csvf.close()
stopTime = time()

print("Se ha generado " + str(registros) + " en " + str(stopTime-startTime) + "s")
    
