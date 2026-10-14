'''
Algoritmo: Texto en mayúsculas y número de palabras
Entrada: frase
Salida: frase_mayus, num_palabras
Inicio:
    frase_mayuscula <- convertir frase a mayúsculas
    palabras <- separar frase por espacios
    num_palabras <- longitud de palabras
    Devolver frase_mayuscula, num_palabras
FIN
'''
def analizar_frase(frase):
    """Devuelve la frase en mayúsculas junto con su número de palabras."""
    frase_mayuscula = frase.upper()
    num_palabras = len(frase.split())
    return frase_mayuscula, num_palabras
print(analizar_frase("Hola mundo, adelante con todo"))