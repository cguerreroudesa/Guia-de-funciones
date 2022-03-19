#Ejercicios de la guia con una estrella

#E2
"""Escriba una función que devuelva el cuadrado de un número (sin utilizar el operador de potencia
del lenguaje de programación)."""

def Cuadrado (x):
    Cuadrado_de_x = x * x
    return Cuadrado_de_x

#E3
"""Escriba una función llamada sumador que recibe dos argumentos y devuelva su suma. Luego,
ejecute pruebas con distintos tipos de datos (dos strings, dos en punto flotante, un int y un str, etc.)."""

def sumador (a, b):
    return a+b

#sumador ("hola", "chau") #Dos strings
#sumador (3.4, 5.7) #Dos floats
#sumador (6, "Hi") #un Int y un str

#E4
"""Corrija la siguiente función defectuosa para que devuelva la multiplicación entre dos números:
def multiply(a, b):
    answer = a * b   
"""

def multiply(a, b):
    answer = a * b
    return answer

#E5
"""Implemente una función que solicite un número por la consola, que represente el radio de una
circunferencia, y muestre en pantalla el perímetro de dicha circunferencia. En la consola se debe ver lo
siguiente:
Ingrese un valor que representa el radio de una circunferencia: [ENTRADA]
El perímetro resultante es [RESULTADO]
"""

def perimetro ():
    pi = 3.141592653589793
    Radio= int (input ("Ingrese un valor que representa el radio de una circunferencia: "))
    print (f"El perimetro resultantes es: {pi * Radio}." )
