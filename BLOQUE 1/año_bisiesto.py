'''
ALGORITMO : es_bisiesto
    ENTRADA: año
    SALIDA: VERDADERO O FALSO
    INICIO
        SI (año % 4 == 0 Y año % 100 != 0) O (año % 400 == 0) :
            DEVOLVER VERDADERO
        SINO
            DEVOLVER FALSO
        FIN SI
    LLAMADAS:
    es_bisiesto(2024) #Imprime: VERDADERO   
    es_bisiesto(2000) #Imprime: VERDADERO
    es_bisiesto(1900) #Imprime: FALSO
FIN
'''
def es_bisiesto(año):
    """Determina si un año es bisiesto."""
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
print (es_bisiesto(2032)) #Imprime: True
print(es_bisiesto(2000)) #Imprime: True
print(es_bisiesto(1900)) #Imprime: False