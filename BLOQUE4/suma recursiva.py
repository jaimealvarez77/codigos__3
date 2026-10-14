'''
Algoritmo: Suma recursiva de una lista
Entrada: numeros (lista de números)
Salida: suma total (número)
INICIO:
    Si la lista numeros está vacía:
        Devolver 0
    Si no
        Devolver primer elemento de numeros + suma_lista(resto de numeros)
    Fin si
FIN
'''
def suma_lista(numeros):
    """Suma los elementos de una lista de forma recursiva."""
    if len(numeros) == 0:
        return 0
    return numeros[0] + suma_lista(numeros[1:])
print(suma_lista([8,7,15]))