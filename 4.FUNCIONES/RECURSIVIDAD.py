# Funciones recursivas

#^ Realizar una función recursiva que calcule la suma de los primeros números naturales:


def sumar_naturales(numero: int)->int:
    if numero == 0:
        return 0
    
    suma = numero + sumar_naturales(numero-1) 
    return suma


# print(sumar_naturales(3))

#^ Realizar una función recursiva que calcule la potencia de un número:


def calcular_potencia(base: int, exponente: int)-> int:
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1 )
    return resultado


# print(calcular_potencia(2,3))

#^ Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_digitos(numero: int)->int:
    if numero == 0:
        resultado = 0
    else: 
        resultado = (numero % 10) + sumar_digitos(numero // 10)

    return resultado

# print(sumar_digitos(12345))


#^ Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

def calcular_fibonacci(numero: int)-> int:
    pass

# Definición:
# La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:





# Nota general: en cada ejercicio al ingresar un número, se tendrá que utilizar la función get_int del módulo Input