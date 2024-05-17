
import math

diccionario_contador = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,
'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0, 'ä':0, 'ö':0, 'ü':0, 'ß':0}

diccionario_probabilidades = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,
'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0, 'ä':0, 'ö':0, 'ü':0, 'ß':0}


def contar(diccionario_contador):
    cantidadLetras = 0
    with open('entropia.txt', 'r') as archivo:
        for linea in archivo:
            palabras = linea.split()
            for palabra in palabras:
                for letra in palabra:
                    cantidadLetras += 1
                    letra = letra.lower()
                    for dicc in diccionario_contador:
                        if letra == dicc:
                            x = diccionario_contador[dicc]
                            x += 1
                            diccionario_contador[dicc] = x
    
    return cantidadLetras


def calcular_probabilidades(diccionario_contador, diccionario_probabilidades, cantidad_letras):
    for dicc in diccionario_contador:
        for diccprob in diccionario_probabilidades:
            if dicc == diccprob:
                diccionario_probabilidades[diccprob] = diccionario_contador[dicc]/cantidad_letras
                break


def calcular_entropia(diccionario_probabilidades):
    for dicc in diccionario_probabilidades:
        x = diccionario_probabilidades[dicc]
        x = x*(math.log(1/x)/math.log(2))
        diccionario_probabilidades[dicc] = x


def mostrar_entropia(diccionario_probabilidades):
    entropia = 0
    for dicc in diccionario_probabilidades:
        entropia = entropia + diccionario_probabilidades[dicc]
        print('La entropia de la {} es: {}'.format(dicc, diccionario_probabilidades[dicc]))
    print('La entropia total del texto es: {}'.format(entropia))




cantidad_letras = contar(diccionario_contador)
calcular_probabilidades(diccionario_contador, diccionario_probabilidades, cantidad_letras)
calcular_entropia(diccionario_probabilidades)
mostrar_entropia(diccionario_probabilidades)

