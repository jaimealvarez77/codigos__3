'''
Algoritmo: Acceso seguro a una lista
Entrada: lista (lista), posicion (número entero)
Salida: elemento en la posición o mensaje de error
Bloque:
    Intentar:
        Devolver lista[posicion]
    Excepto error de índice fuera de rango:
        Devolver "Error: posición fuera de rango"
LLAMADAS:
acceso seguro a una lista([2,17,"julian_alvarez"],2)
acceso seguro a una lista([124,"holacaracola"],2)
FIN
'''
def obtener_elemento(lista, posicion):
    """Accede a una posición de una lista controlando el error de rango."""
    try:
        return lista[posicion]
    except IndexError:
        return "Error: posición fuera de rango"
print(obtener_elemento([2,17,"julian_alvarez"],2))
print(obtener_elemento([124,"holacaracola"],2))
