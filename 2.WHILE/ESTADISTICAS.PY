# """Contadores - Acumuladores - Máximos y mínimos"""


# ^ Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

# contador = 0
# while contador < 10:
#     contador = contador + 1
#     print(contador)

# ^ Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

# contador = 11
# while contador > 1:
#     contador = contador - 1
#     print(contador)


# ^ Mostrar la suma de los números desde el 1 hasta el 10.

# contador = 0
# suma = 0
# while contador < 10:
#     contador = contador + 1
#     suma = suma + contador

# print(suma)


# ^ Mostrar la suma de los números pares desde el 1 hasta el 10.


# contador = 0
# suma = 0
# while contador < 10:
#     contador = contador + 2
#     suma = suma + contador


# print(suma)


# ^ Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.


# contador = 0
# suma = 0

# while contador < 5:
#     numero = int(input("INGRESE UN NUMERO: "))
#     contador = contador + 1
#     suma = suma + numero
# promedio = suma / contador

# print(f"La suma total es: {suma}")
# print(f"El promedio es:{promedio}")





# ^ Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.


# seguir = "si"
# suma = 0
# contador = 0

# while seguir == "si":
#     numero = int(input("ingrese un numero: "))

#     suma += numero

#     seguir = input("desea continuar? si/no: ")
#     contador += 1


# promedio = suma / contador

# print (f"La suma acumulada es : {suma}")
# print (f"El promedio es : {promedio}")


# ^ Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.


# seguir = "si"

# contador = 0
# suma_positivos = 0
# producto_negativo = 1
# bandera = True

# while seguir == "si":
#     numero = int(input("INGRESE UN NUMERO: "))
#     if numero > 0:
#         suma_positivos = suma_positivos + numero
#     elif numero < 0:
#         bandera = False
#         producto_negativo = producto_negativo * numero

#     seguir = input("Desea continuar? si/no: ")
#     if seguir == "no":
#         break    

# print(f"La suma de los numeros positivos es: {suma_positivos}")

# if bandera == False:
#     print(f"El producto de los negativos es: {producto_negativo}")
# else:
#     print("NO SE INGRESARON NUMEROS NEGATIVOS")



# ^ Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# contador = 0

# while contador < 10:
#     numero = input("Ingrese un numero: ")
#     numero = int(numero)

#     if contador == 0:
#         numero_maximo = numero
#         numero_minimo = numero
#     else:
#         if numero > numero_maximo:
#             numero_maximo = numero
#         if numero < numero_minimo:
#             numero_minimo = numero

#     contador = contador + 1

# print(f"EL MAXIMO NUMERO ES: {numero_maximo}")
# print(f"EL NUMERO MINIMO ES: {numero_minimo}")


# ?Anexo

# ^ Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

# contador = 0
# suma = 0
# bandera = True


# while contador < 5 or bandera == True:
#     contador += 1
#     numero = int(input("ingrese un numero: "))
#     suma = suma + numero

#     if contador >= 5:
#         seguir = input("queres ingresar otro numero: si/no? ")
#         if seguir == "si":
#             continue
#         else:
#             bandera = False

# print(f"la suma es igual a: {suma}")
# print(f"el promedio es igual a: {suma/contador}")

# ^ Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.


# num_minimo = 5
# num_maximo = 10
# contador = 0
# suma = 0

# while contador < num_minimo or contador < num_maximo:
#     contador += 1
#     numero = int(input("INGRESE UN NUMERO: "))
#     suma = suma + numero

# promedio = suma/contador

# print(f"la suma es: {suma}")
# print(f"el promedio es igual a: {promedio}")



"""Integrador While
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos."""



# bandera = True
# suma_negativos = 0
# suma_positivos = 0
# contador_negativo = 0
# contador_positivo = 0
# bandera_positivo = True
# promedio_positivos = 0
# contador_total = 0

# while bandera == True:
#     numero = int(input("INGRESE UN NUMERO: "))
#     contador_total += 1

#     if numero < 0:
#         contador_negativo += 1
#         suma_negativos = suma_negativos + numero

#     elif numero >= 0:
#         suma_positivos = suma_positivos + numero
#         contador_positivo += 1
#         if bandera_positivo == True:
#             positivo_mas_grande = numero
#             bandera_positivo = False
#         else:
#             if numero > positivo_mas_grande:
#                 positivo_mas_grande = numero

#     seguir = input("Quiere seguir ingreando numeros? si/no: ")

#     if seguir == "si":
#         continue
#     else:
#         break

# porcentaje = (contador_negativo * 100) / contador_total 

# if contador_positivo != 0:
#     promedio_positivos = suma_positivos / contador_positivo
# print(f"La suma de los numeros negativos es igual a: {suma_negativos}\n Se ingresaron {contador_negativo} numero negativos")
# print(f"La suma de los numeros positivos es igual a: {suma_positivos}\n El promedio de los positivos es: {promedio_positivos:.2f}")
# print(f"El positivo mas grande es {positivo_mas_grande}")
# print(f"El porcentaje de numeros negativos ingresados es: {porcentaje:.2f}%")