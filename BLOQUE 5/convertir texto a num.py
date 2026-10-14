'''
Algoritmo: Convertir texto a número
Entrada: texto (cadena de caracteres)
Salida: número entero convertido o mensaje de error
Inicio:
    Intentar:
        Devolver entero(texto)
    Excepto error de valor:
        Devolver "Error: no es un número"
FIN
LLAMADAS:
convertir texto a numero("hola"))
convertir texto a numero("7"))
'''
def convertir_a_entero(texto):
    """Convierte un texto a entero controlando el error de formato."""
    try:
        return int(texto)
    except ValueError:
        return "Error: no es un número"
print(convertir_a_entero("hola"))
print(convertir_a_entero("7"))