'''
ALGORITMO : mayor_de_tres_numeros
    ENTRADA: numero1, numero2, numero3
    SALIDA: mayor
    INICIO
        SI numero1 >= numero2 Y numero1 >= numero3 :
            mayor = numero1
        SINO SI numero2 >= numero1 Y numero2 >= numero3 :
            mayor = numero2
        SINO:
            mayor = numero3
        FIN SI 
        DEVOLVER mayor
    LLAMADAS:
    mayor_de_tres_numeros(4,9,2) #Imprime: 9
    mayor_de_tres_numeros(7,7,2) #Imprime: 7
FIN
'''
def mayor_de_tres_numeros(numero1,numero2,numero3):
    if numero1>=numero2 and numero1>=numero3:
        mayor = numero1
    elif numero2>=numero1 and numero2>=numero3:
        mayor = numero2
    else:
        mayor = numero3
    return mayor 
print(mayor_de_tres_numeros(4,9,2)) #Imprime: 9
print(mayor_de_tres_numeros(7,7,2)) #Imprime: 7