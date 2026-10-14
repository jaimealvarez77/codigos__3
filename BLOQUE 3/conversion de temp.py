'''
Algoritmo: Conversión de temperatura (Celsius a Fahrenheit y viceversa)
   Entrada: celsius o fahrenheit (números)
   Salida: temperatura convertida
   Bloque:
    Función celsius_a_fahrenheit(celsius):
        Devolver (celsius * 9/5) + 32
    Función fahrenheit_a_celsius(fahrenheit):
        Devolver (fahrenheit - 32) * 5/9
    LLAMADAS:
    print(celsius_a_farenheit(40))
    print(farenheit_a_celsius(103))
FIN
'''
def celsius_a_fahrenheit(celsius):
   return (celsius * 9 / 5) + 32
print(celsius_a_fahrenheit(40))

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_a_celsius(103))
