""" Desafío: Encuesta Tecnológica en UTN Technologies
UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado.
Las tecnologías en evaluación son:
 🔹 Inteligencia Artificial (IA)
 🔹 Realidad Virtual/Aumentada (RV/RA)
 🔹 Internet de las Cosas (IOT)
Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
🔹 Recolección de Datos
Cada empleado encuestado deberá proporcionar la siguiente información:
 ✔️ Nombre
 ✔️ Edad (debe ser 18 años o más)
 ✔️ Género (Masculino, Femenino, Otro)
 ✔️ Tecnología elegida (IA, RV/RA, IOT)
El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
🔹 Análisis de Datos
A partir de las respuestas, se deben calcular las siguientes métricas:
1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
Su género no sea Femenino 
Su edad está entre los 33 y 40 años.
3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


🔹 Requisitos del Programa
 ✔️ Los datos deben solicitarse y validarse correctamente.
 ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
 ✔️ Presentar los resultados de manera clara y organizada.
"""




votos_masculinos = 0
contador_empleado = 0
voto_empleado_no_ia = 0
bandera = True

while contador_empleado < 3: #EN REALIDAD ME PIDEN 10 EMPLEADOS. PUSE 3 PARA PROBAR
    nombre = input("INGRESE SU NOMBRE: ")

    edad = int(input("INGRESE SU EDAD. DEBE SER MAYOR DE 18 AÑOS: "))
    while edad < 18 or edad > 140:
        edad = int(input("REINGRESE SU EDAD. DEBE SER MAYOR DE 18 AÑOS: "))

    genero = input("INGRESE SU GENERO MASCULINO, FEMENINO, OTRO: ")
    while genero != "MASCULINO" and genero != "OTRO" and genero != "FEMENINO":
        genero = input("REINGRESE SU GENERO MASCULINO, FEMENINO, OTRO: ")

    tecnologia_elegida = input("INGRESA EL TIPO DE TECNOLOGIA... IA, RV/RA, IOT: ")
    while tecnologia_elegida != "IA" and tecnologia_elegida != "RV" and tecnologia_elegida != "RA" and tecnologia_elegida != "IOT":
        tecnologia_elegida = input("REINGRESA EL TIPO DE TECNOLOGIA... IA, RV/RA, IOT: ")
    
    contador_empleado += 1
    
    if tecnologia_elegida != "IA":
        if edad > 32 and edad < 41:
            if genero != "FEMENINO":
                voto_empleado_no_ia += 1

    
    if genero == "MASCULINO":
        if tecnologia_elegida == "IA" or tecnologia_elegida == "IOT":
            if edad > 24 and edad < 51:
                votos_masculinos += 1 
        if bandera == True: # EL PRIMER MASCULINO SERA EL MAS GRANDE HASTA QUE LO COMPARE CON EL SIGUIENTE
            edad_max = edad
            nombre_masculino_mayor = nombre
            voto_masculino_mayor = tecnologia_elegida
            bandera = False # CAMBIO EL ESTADO DE BANDERA PARA QUE A LOS SIGUIENTES LOS COMPARE
        else:
            if edad > edad_max:
                edad_max = edad
                nombre_masculino_mayor = nombre
                voto_masculino_mayor = tecnologia_elegida



porcetaje_votos_no_ia = (voto_empleado_no_ia * 100) / contador_empleado

#respuesta 1
print(f"La cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive) es: {votos_masculinos}\n")

#respuesta 2
print(f"""Porcentaje de empleados que NO votaron por IA, siempre y cuando:
            ●	Su género no sea Femenino 
            ●	Su edad está entre los 33 y 40 años.
      EL PORCETAJE ES IGUAL A: {porcetaje_votos_no_ia}\n""")

#respuesta 3
print(f"El hombre de mayor edad es: {nombre_masculino_mayor}\nVoto por la tecnologia {voto_masculino_mayor}\nTiene {edad_max} años de edad\n")        



