'''
ALGORITMO : categoria_peso
ENTRADAS : peso_kg
SALIDAS : categoria 
INICIO
      SI peso_kg<=1:
      categoria = "sobre"
      SI NO SI peso_kg<=5:
      categoria = "paquete pequeño"
      SI NO SI peso_kg<=20:
      categoria = "paquete grande"
      SI NO:
      categoria="voluminoso"
      FIN SI
      DEVOLVER caegoria
LLAMADAS :
categoria_peso(0,5)
categoria_peso(15)
FIN
'''
def categoria_envio(peso_kg):
    """Clasifica un envío según su peso en kilos."""
    if peso_kg<= 1:
        categoria= "sobre"
    elif peso_kg <= 5:
        categoria= "paquete pequeño"
    elif peso_kg<= 20:
        categoria= "paquete grande"
    else:
        categoria= "voluminoso"
    return categoria
print(categoria_envio(0.5)) #sobre
print(categoria_envio(15))  #paquete grande
