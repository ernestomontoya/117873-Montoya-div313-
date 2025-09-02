"""
Validaciones
"""
#^Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

# clave = "1234"

# contraseña = input("INGRESE LA CLAVE: ")
# while contraseña != "1234":
#     contraseña = input("CONTRASEÑA INCORRECTA.\nREINGRESE LA CLAVE: ")
# print("#######################\n   CONTRASEÑA CORRECTA\n#######################")


#^Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

# clave = "hola1234"
# contador = 0
# contraseña = input("INGRESE LA CLAVE: ")
# while contraseña != "hola1234":
#     contraseña = input("CONTRASEÑA INCORRECTA.\nREINGRESE LA CLAVE: ")
#     contador += 1
#     if contador == 2:
#         break
# if contador == 2:
#     print("AGOTO LOS TRES INTENTOS")
# else:
#     print("#######################\n   CONTRASEÑA CORRECTA\n#######################")

#^Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

# nota = int(input("INGRESE UN NOTA ENTRE 1-10: "))

# while not(nota > 0 and nota < 11):
#    nota = int(input("reingrese la nota: "))

# print(f"La nota es: {nota}")

#^Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

# color =input("INGRESE UN COLOR.... PUEDE SER:\nROJO\nVERDE\nAZUL\n\n")

# while color != "rojo" and color != "verde" and color != "azul":
#     color =input("REINGRESE UN COLOR.... PUEDE SER:\nROJO\nVERDE\nAZUL\n\n")

# print(f"eligio el color: \n {color}")


"""Integrador Validaciones
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla."""



# apellido = input("INGRESE EL APELLIDO: ")

# edad = int(input("INGRESE SU EDAD: "))
# while edad < 18 or edad > 90:
#     edad = int(input("REINGRESE SU EDAD: "))

# estado_civil = input("INGRESE EL ESTADO CIVIL: ")
# while estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "divorciado" and estado_civil !="viudo":
#     estado_civil = input("REINGRESE EL ESTADO CIVIL: ")

# legajo = int(input("INGRESE SU LEGAJO: "))

# while legajo < 1111 or legajo > 9999:
#     legajo = int(input("REINGRESE SU LEGAJO: "))



# print(f""""    DATOS DE LA PERSONA:
#         APELLIDO:{apellido}
#         EDAD:{edad}
#         ESTADO CIVIL:{estado_civil}
#         LEGAJO:{legajo}
#         """)