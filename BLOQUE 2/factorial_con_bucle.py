'''
ALGORITMO: Factorial_con_bucle
ENTRADA: n (número entero)
SALIDA: resultado (número entero)
INICIO:
    resultado <- 1
    Para cada i desde 2 hasta n:
        resultado <- resultado * i
    Fin para
    Devolver resultado
FIN
'''
def factorial_con_bucle(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado
print(factorial_con_bucle(5))
print(factorial_con_bucle(10))