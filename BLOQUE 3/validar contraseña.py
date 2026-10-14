'''
Algoritmo: Validar contraseña
Entrada: contrasena , longitud_minima
Salida: valor booleano (True o False)
Inicio:
    Si longitud de contrasena >= longitud_minima:
        Devolver True
    Si no
        Devolver False
    Fin Si
FIN

'''
def validar_contraseña(contraseña):
    longitud_minima=8
    if len(contraseña) >= longitud_minima:
      return "TRUE"
    else:
      return "FALSE"
print(validar_contraseña("pajaritos33"))
print(validar_contraseña("mbappe"))
