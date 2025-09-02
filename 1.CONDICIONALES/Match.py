"""Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche.
"""


estacion_del_año = input("ingrese la estacion del año:  ")

lugar = input("ingrese el lugar:  ")

match estacion_del_año:
    case "invierno":
        match lugar:
            case "bariloche":
                print("se viaja")
            case _:
                print("no se viaja")
    case "verano":
        match lugar:
            case "mar del plata" | "cataratas":
                print("se viaja")
            case _:
                print("no se viaja")
    case "otoño":
        print("se viaja")
    case "primavera":
        match lugar:
            case "bariloche":
                print("No se viaja")
            case _:
                print("se viaja")
    case _:
        print("no se viaja")



