#E13
''' Escriba una función que dado un número devuelva el primer número múltiplo de 10 inferior o
igual a él. Por ejemplo, para 153 debe devolver 150.
'''
def n_multiplo (n):
    while n % 10 != 0:
        n += 1
    return n

print (n_multiplo (1))

#E14
''' Escriba una función que dado un tiempo en segundos, retorne el tiempo en horas, minutos y
segundos (similar al ejercicio 12). Por ejemplo, para 3745 debe devolver 1, 2, 25.
'''
def tiempo (seg):
    hora = int (seg/3600)
    segundos = seg - (hora * 3600)
    minutos = int (segundos / 60)
    segundos -= (minutos * 60)
    return (hora, minutos, segundos)
