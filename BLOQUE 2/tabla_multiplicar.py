'''
Algoritmo: Tabla de multiplicar
Entrada: numero (número entero)
Salida: tabla de multiplicación
Inicio:
    Para i desde 1 hasta 10:
        Mostrar numero, "x", i, "=", numero * i
    Fin para
FIN
'''
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número, del 1 al 10."""
    for i in range(1, 11):  #en python el ultimo numero de la orquilla no cuenta
        print(f"{numero}x{i}={numero * i}") #Esa f antes de las comillas se utiliza para crear un f-string
print(tabla_multiplicar(3))