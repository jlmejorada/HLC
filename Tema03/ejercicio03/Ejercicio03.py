def comprobarCodigo(codigo):
    esCorrecto  = False

    if len(codigo) <= 8 :
        esCorrecto=compruebaEan8(codigo)

    elif 8 < len(codigo) <= 13:
        esCorrecto = True

    return esCorrecto

def compruebaEan8(codigo):
    cont=0
    codNum=0
    res=0
    num=0
    esCorrecto = True
    codigoRelleno = codigo.zfill(8)
    codNum=int(codigoRelleno)
    cont=len(codigoRelleno)
    while cont>0 :
        if cont == 1:
            res+=codNum
        elif cont%2 == 1 :
            num= codNum%10
            codNum=codNum//10
            res+=3*num
        else :
            num = codNum % 10
            codNum = codNum // 10
            res += num
        if res == 90 :
            esCorrecto = True
        cont -= 1
        print(res)

    return esCorrecto