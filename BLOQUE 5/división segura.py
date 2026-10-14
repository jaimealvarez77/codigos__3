'''
Algoritmo: División segura
Entrada: a, b
Salida: resultado de la división o mensaje de error
INICIO:
    Intentar:
        Devolver a / b
    Excepto b==0:
        Devolver "Error división entre cero"
FIN
print(division_segura(10,0))
print(division_segura(5,2))
'''
def division_segura(a, b):
    """Divide dos números controlando la división entre cero."""
    try:
        return a / b
    except b==0:
        return "Error división entre cero"
print(division_segura(10,0))
print(division_segura(5,2))