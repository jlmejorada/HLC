abcdario = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def cifraTexto(frase, num):
    textoCifrado=""
    cont=0
    mov=num%27

    for letra in frase:
        if letra != " " :
            cont=abcdario.index(letra)
            textoCifrado+=abcdario[cont+mov]
            cont=cont+1

    return textoCifrado