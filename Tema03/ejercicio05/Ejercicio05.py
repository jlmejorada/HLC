from os.path import split

def ascensor(linea):
    #Inicializamos la respuesta a 0
    res = 0
    #Esto guardara el número siguiente al que recorramos
    des = 0
    #Guardamos la linea dividida entre espacios en una lista(?)
    numdiv = linea.split(" ")
    """
    num1 = 0
    num2 = 0
    num3 = 0
    if len(numdiv)==2 :
        num1 = int(numdiv[0])
        num2 = int(numdiv[1])
        res = abs(num2-num1)
    elif len(numdiv)==3:
        num1 = int(numdiv[0])
        num2 = int(numdiv[1])
        num3 = int(numdiv[2])
        res += abs(num2 - num1)
        res += abs(num3 - num2)
    else :
        res = int(linea)
    """
    #Si el hay mas de 1 número
    if len(numdiv) > 1:
        #Recorremos desde 0 y el mayor indice - 1
        for i in range(0,len(numdiv)-1):
            #Guardamos el numero correspondiente al siguiente que estamos recorriendo
            des = int(numdiv[i+1])
            #Y sumamos a la respuesta el valor absoluto de la resta entre el numero de despues y el recorrido
            res += abs(des-int(numdiv[i]))
    #Si no
    else:
        #El resto es igual al unico número
        res = int(linea)
    #Devolvemos la respuesta
    return res