'''
Algoritmo: Contar_vocales
Entrada: palabra
Salida: contador
Inicio:
    contador <- 0
    palabra_min <- minúscula de palabra
    Para cada caracter en palabra_min:
        Si caracter es 'a', 'e', 'i', 'o', 'u':
            contador <- contador + 1
        Fin si
    Fin para
    Devolver contador
FIN
'''
def contar_vocales(palabra):
    '''Cuenta las vocales de una palabra, sin distinguir mayúsculas'''
    contador = 0
    vocales = "a","e","i","o","u"
    for caracter in palabra.lower():
        if caracter in vocales:
            contador = contador + 1 #que es igual a contador+=1
    return contador
print(contar_vocales("programacion"))
print(contar_vocales("xyz"))