"""Módulos
Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

def get_int(mensaje:srt,mensaje_error:str,minimo:int,maximo:int,reintentos:int) -> int|None:
    pass

En donde:
mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
mínimo: valor mínimo admitido (inclusive)
máximo: valor máximo admitido (inclusive)
reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

En caso de que la función no haya podido conseguir un número válido, la misma retorna None.

                                      IMPRIMIR MENSAJE
                                             ↓
----------------------------->    PEDIR DATOS AL USUARIO
|                                            |
|                                            |
|                                            |
|                                            ↓
|       IMPRIMIR MENSAJE <<<---ERROR---  VALIDACION
|               |                            |
|               ↓                            ↓
SI-------¿HAY INTEENTOS?          ESCRIBIR DATO EN VARIAVLE DE SALIDA
                |                            |
                |                            |
                ↓                            ↓
                NO                           ↓
                ↓                         NUMERO
                ↓                         VALIDO           
               NONE



Repetir el mismo procedimiento para un dato de tipo float.
 
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):

def get_string(longitud: int) -> str|None:
    pass


Nota: utilizar la función len.



Realizar los siguientes módulos:
Input.py
get_int()
get_float()
get_string()
Validate.py
validate_number()
validate_length()

Nota: estas funciones las tendrán que desarrollar en el módulo Validate y utilizar en el módulo Input.py para realizar las validaciones necesarias.

Crear un repositorio en github con su apellido y nombre junto con el texto funciones_input:
Por ejemplo: scarafilo_german_funciones_input
Dicho repositorio deberá ser privado. Agregar a sus profesores como colaboradores.

"""



# def get_int(mensaje:str, mensaje_error:str,minimo:int,maximo:int,reintentos:int) -> int|None:
#     dato = input(mensaje)








# En donde:
# mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
# mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
# mínimo: valor mínimo admitido (inclusive)
# máximo: valor máximo admitido (inclusive)
# reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.