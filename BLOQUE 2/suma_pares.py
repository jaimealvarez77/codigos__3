'''
ALGORITMO: SUMA_PARES_ENTRE1YN
ENTRADAS: n (numero entero)
SALIDAS: suma (numero entero)
INICIO
suma <- 0
para cada i desde 1 hasta N:
  SI i % 2 == 0:
    suma <- suma+i
  FIN SI
FIN PARA
DEVOLVER suma
LLAMADAS:
SUMA_PARES_ENTRE1YN(10)
SUMA_PARES_ETRE1YN(1)
FIN
'''
def suma_pares(n):
    """Suma los números pares entre 1 y n."""
    suma=0
    for i in range(1, n+1):
     if i % 2 == 0:
        suma = suma + i
    return suma
print(suma_pares(10))
print(suma_pares(1))
