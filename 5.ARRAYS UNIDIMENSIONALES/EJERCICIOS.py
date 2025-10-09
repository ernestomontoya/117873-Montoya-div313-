"""Arrays unidimensionales"""

#^Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.



def crear_array(cantidad):
   lista = [0] * cantidad
   
   return lista

# print(crear_array(5))


#^Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

def cargar_array(numero):
   array = crear_array(numero)
   for i in range(len(array)):
      valor = int(input("INGRESE UN NUMERO: "))
      array[i]= valor
   return array
   


# print(cargar_array(3))


#^Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 

def calcular_promedio(lista: list, mensaje_error:str)-> str | float:
   suma_elemento = 0
   if len(lista) == 0:
      return mensaje_error
   for i in range(len(lista)):
      suma_elemento += lista[i]
   promedio_elementos = suma_elemento / len(lista)
   
   return promedio_elementos



# lista_enteros = []

# print(f"El promedio es: {calcular_promedio(lista_enteros,"la lista esta vacia")}")


#^Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.


def calcular_promedio(lista: list, mensaje_error:str= "NO HAY POSITIVOS")-> str | float:
   """LA FUNCION CALCULA EL PROMEDIO DE NUMEROS POSITIVOS DE UNA LISTA
   RECIBE UN LISTA DE NUMEROS
   RECIBE UN MENSAJE DE ERROR EN CASO QUE NO HAYA POSITIVOS
   
   DEVUELVE EL RESULTADO DEL PROMEDIO O UN MENSAJE QUE NO SE INGRESO POSITIVOS"""

   suma_elemento = 0
   contador = 0
   for i in range(len(lista)):
      if lista[i] > 0:
         suma_elemento += lista[i]
         contador += 1
   if contador == 0:
      return mensaje_error
   promedio_elementos = suma_elemento / contador
   
   return promedio_elementos



# lista_enteros = []

# print(calcular_promedio(lista_enteros))


#^Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.


# def calcular_producto(lista):
#    resultado = 1
#    for numero in lista:
#       resultado = resultado * numero
#    return resultado


# lista_numeros = [3,5,12,14] # 2520

# print(calcular_producto(lista_numeros))


def calcular_producto(lista:list):
   resultado = 1
   for i in range(len(lista)):
      resultado = resultado * lista[i]
   return resultado


# lista_numeros = [3,5,12,14] # 2520

# print(calcular_producto(lista_numeros))



#^Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.


def encontrar_maximo(lista:list, mensaje="LISTA VACIA")->int | str:
   if len(lista) == 0:
      return mensaje
   else:
      num_max = lista[0]
      for i in range(len(lista)):
         if lista[i] > num_max:
            num_max = lista[i]
   return num_max


# lista_numeros = [-1,-8,5,24,15] 

# print(encontrar_maximo(lista_numeros))



#^Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.


def posicion_max_valor(lista, mensaje="lista vacia"):
   if len(lista) == 0:
      return mensaje
   else:
      num_max = lista[0] #el primer valor sera el maximo
      pos_max = []         #lista para guardar las posiciones
      for i in range(len(lista)):   #recorro la lista
         if lista[i] > num_max:     #comparo los numeros desde la posi 1 en adelante
            num_max = lista[i]      #si es mas grande sera el mayor 
            pos_max = [i]           # posicion del primer numero mas grande
         elif lista[i] == num_max:    # comparo si es el mas grande lo agredo a la lista
            pos_max.append(i)
   return num_max, pos_max

# lista_numeros = [4,5,12,14,3,14]

# print(posicion_max_valor(lista_numeros))



#^Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:

#Una lista de nombres (lista_nombres).
#Un nombre a buscar en la lista (nombre_antiguo).
#Un nombre de reemplazo (nombre_nuevo).
#La función debe realizar las siguientes acciones:
#Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
#Retornar la cantidad total de reemplazos realizados.


def reemplazar_nombres(lista_nombres, nombre_antiguo, nombre_nuevos):
   contador = 0 
   for i in range(len(lista_nombres)):
      if lista_nombres[i] == nombre_antiguo:
         lista_nombres[i] = nombre_nuevos
         contador += 1
   return contador


# lista_de_nombres = ["jose","pedro","juan","jose","nicolas"]
# nombre_viejo = "pedro"
# nombre_nuevito = "elizabeth"

# reemplazo = reemplazar_nombres(lista_de_nombres,nombre_viejo,nombre_nuevito)

# print(f"LA CANTIDAD DE REEMPLAZOS REALIZADOS ES IGUAL A: {reemplazo}")



#Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.


# def mostrar_interseccion(lista_a,lista_b):
#    interseccion = []
#    for i in range(len(lista_a)):
#       for j in range(len(lista_b)):
#          if lista_a[i] == lista_b[j] and lista_a[i] not in interseccion: #si el numero de a es igual al numero de la lista de b y ademas no se haya agregado con anterioridad
#             interseccion.append(lista_a[i])
#             break
#    return interseccion

# # print(mostrar_interseccion([2,5,4,8,4,3,6,1],[21,56,42,4,12,12,3,125]))


#otra forma
#!https://docs.python.org/es/3.14/library/stdtypes.html#set

def mostrar_interseccion(lista_a,lista_b):
   conjunto_a = set(lista_a)
   conjunto_b = set(lista_b)

   # lista_c = conjunto_a & conjunto_b
   lista_c = conjunto_a.intersection(conjunto_b)
   lista_c = list(lista_c)

   return lista_c


# print(mostrar_interseccion([2,5,4,8,4,3,6,1],[21,56,42,4,12,12,3,125]))





#? Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

# los paso a conjuntos para poder usar los metodos
def mostrar_union(lista_a,lista_b):
   conjunto_a = set(lista_a)
   conjunto_b = set(lista_b)

   # lista_c = conjunto_a | conjunto_b
   lista_c = conjunto_a.union(conjunto_b)
   lista_c = list(lista_c)

   return lista_c


# print(mostrar_union([2,5,4,8,4,3,6,1],[21,56,42,4,12,12,3,125]))

# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.


def mostrar_diferencias_en_array(lista_a,lista_b):
   conjunto_a = set(lista_a)
   conjunto_b = set(lista_b)

   lista_c = conjunto_a.difference(conjunto_b)
   return lista_c  
   
# print(mostrar_diferencias_en_array([2,5,4,8,4,3,6,1],[21,56,42,4,12,12,3,125]))
