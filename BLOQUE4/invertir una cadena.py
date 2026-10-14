'''
Algoritmo: Invertir una cadena de texto
Entrada: texto 
Salida: texto invertido 
Bloque de desarrollo:
    Si longitud de texto <= 1 entonces
        Devolver texto
    Si no
        Devolver último carácter + invertir_texto(texto sin el último carácter)
    Fin si
'''
def invertir_texto(texto):
    """Invierte una cadena de texto de forma recursiva."""
    if len(texto) <= 1:
        return texto
    return texto[-1] + invertir_texto(texto[:-1])
print(invertir_texto("hola mundo aqui estoy"))