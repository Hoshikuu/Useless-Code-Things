#10000 lines in 6 seconds

from faker import Faker
from time import time
import csv

fake = Faker()

registros = 10000

startTime = time()
with open("C:/Users/Cristian/Documents/py/DATOS/datosprue.csv", 'a', newline="") as csvf:
    head = ["Nombre","Email", "Direccion", "Texto"]
    csvw = csv.DictWriter(csvf, head)
    csvw.writeheader() 
    for i in range(registros):
        csvw.writerow({"Nombre" : fake.name(), "Email" : fake.email(),"Direccion" : fake.address().replace("\n", ", "), "Texto" : fake.text().replace("\n", ", ")})
    del csvw
    csvf.close()
stopTime = time()

print("Se ha generado " + str(registros) + " en " + str(stopTime-startTime) + "s")
    
