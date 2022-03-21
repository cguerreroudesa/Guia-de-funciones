#Ejercicios de la guia con dos estrellas

#E6
"""Para la función definida en el siguiente código, encuentre una implementación alternativa que
permita implementar la misma función pero reduciendo las 7 líneas del cuerpo de su definición a un cuerpo
de sólo 2 líneas."""



def some_function(first_word, second_word, third_word, fourth_word):
    print('Name: {} {}, Age: {} years'.format (first_word, second_word, third_word))
    print('Profession:', fourth_word)

#E7
"""Escriba una función que redondee un número de tipo flotante al entero más cercano y devuelva
este número entero.
Escriba un programa que pida al usuario el número y muestre en la consola interactiva el resultado
de ejecutar la función desarrollada."""

def Redondeo (n):
    n_redondeado = round(n)
    return (n_redondeado)

n_ingresado = float (input ('Escriba un numero flotante (con coma): ') )
print ('El numero más cercano al numero que ha ingresado es: ', Redondeo (n_ingresado))

#E8
"""La ecuación para el interés simple es:
Cn+k = Cn (1+ki)
donde:
    Cn es el capital al inicio del período,
    k es la cantidad de períodos,
    Cn+k es el capital pasados los k períodos,
    i es la tasa de interés nominal por período
    
Escriba:
una función que dada una tasa de interés anual, una cantidad de años y un capital inicial, retorne el
capital al finalizar el período.
un programa que pida al usuario los datos necesarios y muestre en la consola interactiva el resultado
de ejecutar la función desarrollada."""

def Cap_final (interes_anual, años, cap_inicial):
    capital_final = cap_inicial * (1 + (años * interes_anual))
    return capital_final

Cn = int (input ('Ingrese el capital inicial:'))
k = int (input('Ingrese la cantidad de años: '))
i = int (input('Por ultimo, ingrese la tasa de interes anual:'))

print (' Su capital al finalizar este periodo será de: ', Cap_final (i, k, Cn))

#E9
"""Dada la ecuacion de interes compuesto.
Escriba:
una función que dada una tasa de interés anual, una cantidad de años y un capital inicial, retorne el
capital al finalizar el período.
un programa que pida al usuario los datos necesarios y muestre en la consola interactiva el resultado
de ejecutar la función desarrollada."""

def Cap_final (interes_anual, años, cap_inicial):
    capital_final = cap_inicial * (1 + interes_anual) ** años
    return capital_final

Cn = int (input ('Ingrese el capital inicial:'))
k = int (input('Ingrese la cantidad de años: '))
i = int (input('Por ultimo, ingrese la tasa de interes anual:'))

print (' Su capital al finalizar este periodo será de: ', Cap_final (i, k, Cn))

#E10
""" Basandonos en el cálculo de la tasa de interés efectiva.
Escriba:
    una función que dada una tasa de interés nominal anual y períodos de composiciones mensuales
calcule la tasa efectiva anual para todo el año.
    un programa que pida al usuario los datos necesarios y muestre en la consola interactiva el resultado
de ejecutar la función desarrollada.
"""

def Tasa_efectiva_anual (interes_nominal_anual, frecuencia):
    r = ( (1 + (interes_nominal_anual / frecuencia) ** frecuencia) -1 )
    return r

i = int (input('Ingrese la tasa de interes nominal: '))
n = int (input('Por ultimo, ingrese la cantidad de periodos de composicion:'))

print (' La tasa efectiva anual para todo el año será de: ', Tasa_efectiva_anual (i, n) )

#E11
""" Basandonos en La ecuación para el valor futuro para un monto de capital con inversiones mensuales (interés
compuesto).

Escriba:
-una función que dados los tres primeros items del listado anterior, obtenga el monto final (FV).
-un programa que pida al usuario los datos necesarios y muestre en la consola interactiva el resultado
de ejecutar la función desarrollada.
"""

def monto_final (c_invertido_periodo, periodos, interes_nominal):
    FV = c_invertido_periodo * ( ( ((1 + interes_nominal)**periodos)-1 ) / interes_nominal )
    return FV

c = int (input('Ingrese el capital invertido en cada período: '))
k = int (input('Ingrese la cantidad de períodos:'))
r = int (input('Ingrese la tasa de interés nominal por período: '))

print (' El monto final será de: ', monto_final( c, k, r) )

#E12
"""Escriba una función que dadas la hora, minutos y segundos devuelva el tiempo en segundos.
Escriba un programa que pida la hora al usuario y muestre el tiempo en segundos."""

def t_segundos (h, m, s):
    segundos_totales = h * 3600 + m * 60 + s
    return segundos_totales

hora = int (input ('Ingrese la hora: '))
min = int (input ('Ingrese los minutos: '))
seg = int (input ('Ingrese los segundos: '))

print ('El tiempo en segundos es: ', t_segundos (hora, min, seg))