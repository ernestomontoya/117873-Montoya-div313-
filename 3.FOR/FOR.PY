
"""For"""

#^1.	Mostrar los números ascendentes desde el 1 al 10

# for i in range(10):
#     print(i+1)


#^2.	Mostrar los números descendentes desde el 10 al 1

# for i in range(10,0,-1):
#     print(i)


#^3.	Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.


# numero = int(input("INGRESE UN NUMERO: "))


# for i in range(numero + 1):
#     print(i)


#^ 4.	Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15 …

# numero = int(input("INGRESE UN NUMERO: "))

# for i in range(11): # si reemplazo 11 x numero, me va a dar la tabla hasta el numero ingresado. con esto me da siempre los primeros 10 numeros
#     print(f"{numero} x {i} = {numero * i}")


#^5.	Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

# suma = 0

# for i in range(1,11):
#     # print(i)
#     numero = int(input("INGRESE UN NUMERO: "))
#     if numero == 0:
#         break
#     else:
#         suma = numero + suma
    
# promedio = suma / i

# print(f"la suma es: {suma} y  el promedio es: {promedio}")

#^ 6.	Imprimir los números múltiplos de 3 entre el 1 y el 10.



# for i in range(0,11,3):
#     if i > 0:
#         print(i)


#^7.	Mostrar los números pares que hay desde la unidad hasta el número 50.

# for i in range(0,52,2):
#     if i > 0:
#         print(i)



#^ 8.	Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

"""
1
12
123
1234
12345
"""

# numero = int(input("INGRESE UN NUMERO: "))

# for i in range(1,numero+1):
#     for j in range(1,i+1):
#         print(f"{j}",end="") #end="" imprime seguido sin saltar de linea. para que el otro me imprima al lado y no abajo
#     print("")


#^ 9.	Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.


# numero = int(input("INGRESAR UN  NUMERO: "))
# cantidad_divisores = 0

# for i in range(1,numero + 1):
#     if numero % i == 0:
#         print(i)
#         cantidad_divisores += 1
# print(f"la cantidad de divisores encontrados es igual a: {cantidad_divisores}")
        

#^10.	Ingresar un número. Determinar si el número es primo o no.

# numero_ingresado = int(input("Ingrese un numeroo: "))
# bandera = False

# for i in range(2,numero_ingresado):
#     if numero_ingresado % i == 0:
#         bandera = True
#         break
#     else:
#         break

# if bandera == False:
#     print(f"el numero {numero_ingresado} ES primo")
# else:
#     print(f"el numero {numero_ingresado} NO es primo")



#^Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

# numero_ingresado = int(input("Ingrese un numeroo: "))
# bandera = False

# for i in range(2,numero_ingresado):
#     if numero_ingresado % i == 0:
#         bandera = True
#         break
#     else:
#         break

# if bandera == False:
#     print(f"el numero {numero_ingresado} ES primo")
# else:
#     print(f"el numero {numero_ingresado} NO es primo")

