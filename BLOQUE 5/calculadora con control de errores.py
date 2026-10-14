'''
Algoritmo: Calculadora con control de errores
Entrada: texto_a, texto_b (textos), operacion
Salida: resultado numérico o mensaje de error
Bloque:
    Intentar:
        num_a <- convertir texto_a a decimal/entero
        num_b <- convertir texto_b a decimal/entero
        Si operacion == "suma":
            Devolver num_a + num_b
        Si no si operacion == "division":
            Devolver num_a / num_b
        Fin si
    Excepto error de valor:
        Devolver "Error: valor no numérico"
    Excepto división por cero:
        Devolver "Error: división entre cero"
FIN
calculadora con control de errores("siete","cuatro","division")
calculadora con control de errores("7","4","suma")
'''
def calculadora_segura(texto_a, texto_b, operacion):
    """Suma o divide dos textos numéricos controlando los errores posibles."""
    try:
        num_a = float(texto_a)
        num_b = float(texto_b)
        if operacion == "suma":
            return num_a + num_b
        elif operacion == "division":
            return num_a / num_b
    except ValueError:
        return "Error: valor no numérico"
    except ZeroDivisionError:
        return "Error: división entre cero"
print(calculadora_segura("siete","cuatro","division"))
print(calculadora_segura("7","4","suma"))