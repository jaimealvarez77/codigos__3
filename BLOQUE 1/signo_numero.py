'''
ALGORITMO: signo_numero
    ENTRADA: numero
    SALIDA: signo 
    INICIO
        SI numero > 0 :
            signo = "positivo"
        SINO SI numero == 0 :
            signo = "cero"
        SINO
            signo = "negativo"
        FIN SI
        DEVOLVER signo
    LLAMADAS:
    signo_numero(-2) #Imprime: negativo
    signo_numero(2) #Imprime: positivo
FIN
'''
def signo_numero(numero):
    """Devuelve si un número es positivo, negativo o cero."""
    if numero>0 :
        signo = "positivo"
    elif numero==0 :
        signo = "cero"
    else :
        signo = "negativo"
    return signo
print(signo_numero(-2)) #Imprime: negativo
print(signo_numero(2)) #Imprime: positivo
