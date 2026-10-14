'''
Algoritmo: Promedio de una lista de números
Entrada: numeros (lista de números)
Salida: promedio (número decimal)
Inicio:
    Si la lista numeros está vacía entonces
        Devolver 0.0
    suma <- sumar todos los numeros
    cantidad <- longitud de numeros
    promedio <- suma / cantidad
    Devolver promedio
FIN
'''
def calcular_promedio(numeros):
    """Calcula la media aritmética de una lista de números."""
    if len(numeros) == 0:
        return 0.0
    return sum(numeros) / len(numeros)
print(calcular_promedio([6,7,8,9]))