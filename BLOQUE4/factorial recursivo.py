'''
Algoritmo: Factorial recursivo
Entrada: n 
Salida: resultado
Inicio:
    Si n == 0 o n == 1 entonces
        Devolver 1
    Si no
        Devolver n * factorial_recursivo(n - 1)
    Fin si
FIN
'''
def factorial_recursivo(n): # el factorial también se puede escribir como 5!=5*4!,4!=4*3!...
    """Calcula n! llamándose a sí misma(versión recursiva)."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)
print(factorial_recursivo(7))

