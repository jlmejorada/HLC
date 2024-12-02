import random
from asyncio import Queue
from multiprocessing import Process


def temperaturaDia(dia):
    ent = 0
    dec=0
    res=0
    ruta=""
    if dia<10:
        ruta = "0"+str(dia)
    fich = "diciembre/" + ruta + "-12.txt"
    with open(fich, "w") as archivo:
        for i in range(24):
            ent = random.randint(0,90)
            dec=ent/100
            ent = random.randint(0,20)
            res=ent+dec
            archivo.write(str(res) +"\n")

def leeArchivo(cola : Queue, dia):
    ruta=""
    if dia<10:
        ruta = "0"+str(dia)
    fich = "diciembre/" + ruta + "-12.txt"
    with open(fich, "r") as archivo:
        for line in archivo:
            tem = line
            cola.put(tem, dia)

def maximas(cola : Queue, dia):
    maxTemp=0
    leeArchivo(cola, dia)
    with open("maximas.txt", "w") as archivo:
        temp, dia = cola.get()
        while temp != None:
            if (maxTemp < temp):
                maxTemp = temp
            temp, dia = cola.get()
        if dia < 10:
            dia = "0" + str(dia)
        archivo.write( str(dia) + "-12" + temp + "\n")


def minimas(cola : Queue):
    minTemp=20
    with open("minimas.txt", "w") as archivo:
        temp, dia = cola.get()
        while temp != None:
            if (minTemp > temp):
                minTemp = temp
            temp, dia = cola.get()
        if dia < 10:
            dia = "0" + str(dia)
        archivo.write( str(dia) + "-12" + temp + "\n")



if __name__ == '__main__':
    dias = []
    for i in range(31):
        if i>0:
            dias.append(i)

    queue = Queue()
    for dia in dias:
        p1 = Process(target=temperaturaDia, args=(dia,))
        p2 = Process(target=maximas, args=(queue, dia))
        p3 = Process(target=minimas, args=(queue,))
        p1.start()
        p1.join()
        p2.start()
        p3.start()
        p2.join()
        p3.join()
