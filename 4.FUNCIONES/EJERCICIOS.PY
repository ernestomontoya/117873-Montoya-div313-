# Funciones

#^ Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def ingresar_numero_entero(mensaje:str)-> int:
    """
    LA FUNCION PIDE UN NUMERO ENTERO Y LO RETORNA

    RECIBE UN MENSAJE PIDIENDO EL NUMERO

    RETORNA EL NUMERO ENTERO
    
    """
    
    numero = int(input(mensaje))

    return numero


# numero = ingresar_numero("ingresar un numero entero: ")
# print(f"INGRESASTE EL NUMERO: {numero}")



#^ Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def ingresar_numero_flotante(mensaje:str)-> int:
    """
    LA FUNCION PIDE UN NUMERO FLOTANTE Y LO RETORNA

    RECIBE UN MENSAJE PIDIENDO EL NUMERO

    RETORNA EL NUMERO FLOTANTE
    
    """
    numero = float(input(mensaje))
    return numero

# numero = ingresar_numero_flotante("ingresar un numero flotante: ")
# print(f"INGRESASTE EL NUMERO: {numero}")

#^ Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def pedir_cadena(mensaje:str)->str:
    """
    LA FUNCION PIDE UN MENSAJE Y LO RETORNA
    """
    cadena = input(mensaje)
    return cadena

# pedido = pedir_cadena("ingresa un mensaje/cadena: ")
# print(f"INGRESASTE EL SIGUIENTE MENSAJE:\n{pedido}")

#^ Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def calcular_area_rectangulo(base: int|float ,altura: int|float)-> int|float:
    """
    calcula el area de un rectangulo

    recibe el valor de la base y la altura como entero o flotante

    retorna el valor del area

    """
    area = base * altura
    return area

# base = float(input("INGRESE EL VALOR DE LA BASE: "))
# altura = float(input("INGRESE EL VALOR DE LA ALTURA: "))

# area_rectangulo = calcular_area_rectangulo(base,altura)

# print(f"EL AREA DE UN RECTANGULO ES IGUAL A: {area_rectangulo}")

#^ Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

import math

def calcular_area_circulo(diametro: int|float)-> int|float:
    """
    LA FUNCION CALCULA EL AREA DE UN CIRCULO

    RECIBE EL TAMAÑO DEL DIAMETRO int|float

    RETORNA EL VALOR DEL AREA
    """
    area_del_circulo = math.pi * (diametro/2)**2
    return area_del_circulo


# area_de_un_circulo = calcular_area_circulo(12)

# print(f"EL AREA DE UN CIRCULO ES DE: {area_de_un_circulo}")

#^ Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.


def verificar_paridad(numero: int)-> str:
    """
    LA FUNCION ME DICE SI EL NUMERO INGRESADO ES O NO PAR\n
    RECIBE UN NUMERO ENTERO\n
    RETORNA EL MANSAJE INDICANDO SI ES O NO PAR
    """
    if numero % 2 == 0:
        mensaje = "ES PAR"
    else:
        mensaje = "NO ES PAR"
    return mensaje


# numero_a = int(input("ingrese un numero: "))
# print(f"EL NUMERO {numero_a} {verificar_paridad(numero_a)}")


#^ Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def verificar_paridad(numero: int)-> bool:
    """
    LA FUNCION ME DICE SI EL NUMERO INGRESADO ES O NO PAR\n
    RECIBE UN NUMERO ENTERO\n
    RETORNA TRUE SI EL NUMERO ES PAR O FALSE SI NO ES PAR
    """
    if numero % 2 == 0:
        resultado = True    
    else:
        resultado = False
    return resultado

# numero_a = int(input("ingrese un numero: "))
# print(verificar_paridad(numero_a))

#^ Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def calcular_maximo(numero_a: int, numero_b: int ,numero_c: int)-> int:
    """
    LA FUNCION CALCULA EL MAXIMO NUMERO ENTRE TRES VALORES\n
    RECIBE 3 NUMEROS ENTEROS\n
    RETORNA EL VALOR ENTERO MAS GRANDE 
    """
    max_numero = numero_a 
    if numero_b > max_numero:
        max_numero = numero_b
    if numero_c > max_numero:
        max_numero = numero_c
    return max_numero

# print(f"El maximo numero entre tres numeros es: {calcular_maximo(5,5,1)}")


#^ Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_potencia(base: int|float, exponente: int|float)-> int|float:
    """
    LA FUNCION SE ENCARGA DE CALCULAR LA POTENCIA DE UN NUMERO\n
    RECIBE LA BASE Y EL EXPONENTE INT|FLOAT \n
    RETORNA EL RESULTADO DE LA POTENCIA
    """
    resultado = base ** exponente
    return resultado

# print(calcular_potencia(2,0.5))

#^ Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.



#^ Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.



#^ Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.



#^ Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

