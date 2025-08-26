'''
 GOTITA S.A


Facturación del Servicio de Agua Potable

El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes (tarifas y ajustes según el consumo y el tipo de cliente).
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.



                                -Tarifa base:

Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.

El costo por metro cúbico (m³) de agua es de $200/m³.
#################################################################################################

                    -Bonificaciones y Recargos según tipo de cliente:


        Cliente Residencial:

Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.


        Cliente Comercial:

Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
Si el consumo es menor a 50 m³, se aplica un recargo del 5%.


        Cliente Industrial:

Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
Si el consumo es menor a 200 m³, se aplica un recargo del 10%.


        Casos especiales:

Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.

En todos los casos, se aplica el IVA del 21% sobre el total.






-----------------Requerimientos del programa:----------------

1.Solicitar al usuario:

    Cantidad de metros consumidos
    Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.


2.Calcular:

    Subtotal de consumo.
    Bonificaciones, si corresponde
    Recargos, si corresponde
    Subtotal, con recargos y bonificaciones.
    IVA aplicado (21%), si corresponde.
    Total final a pagar.


3.Mostrar en pantalla el desglose de los cálculos.

'''




"""
-Tarifa base:

Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.

El costo por metro cúbico (m³) de agua es de $200/m³."""





cargo_fijo = 7000 # ademas de costo por consumo
costo_x_metro = 200 # $200/m³
iva = 21 # a todos los casos aplico el iva del 21%
porcentaje = 0
bonificacion = 0
recargo = 0
subtotal_con_bonificaciones = 0
subtotal_con_recargo = 0
porcentaje_beneficio = 0
porcentaje_recargo = 0
total_con_iva = 0
total_con_recargo_mas_iva = 0
total_con_bonificacion_mas_iva = 0
subtotal_de_consumo = 0
iva_aplicado_a_consumo = 0


metros_consumidos = float(input("Ingresar la cantidad de metros de agua consumidos: "))

if metros_consumidos > 0:
    tipo_de_cliente = input("Ingrese el tipo de cliente: \n RESIDENCIAL, COMERCIAL o INDUSTRIAL:")
    subtotal_de_consumo = costo_x_metro * metros_consumidos + cargo_fijo
    if tipo_de_cliente == "RESIDENCIAL":
        if subtotal_de_consumo < 35000:
            porcentaje_beneficio = 5
        else:
            if metros_consumidos < 30:
                porcentaje_beneficio = 10
            elif metros_consumidos > 80:
                porcentaje_recargo = 15
        print(f"\n El subtotal de consumo RESIDENCIAL es: ${subtotal_de_consumo}")
    elif tipo_de_cliente == "COMERCIAL":
        if metros_consumidos > 300:
            porcentaje_beneficio = 12
        elif metros_consumidos > 150:
            porcentaje_beneficio = 8
        elif metros_consumidos < 50:
            porcentaje_recargo = 5
        print(f"\n El subtotal de consumo COMERCIAL es: ${subtotal_de_consumo}")
    elif tipo_de_cliente == "INDUSTRIAL":
        if metros_consumidos > 1000:
            porcentaje_beneficio = 30
        elif metros_consumidos > 500:
            porcentaje_beneficio = 20
        elif metros_consumidos < 200:
            porcentaje_recargo = 10
        print(f"\n El subtotal de consumo INDUSTRIAL es: ${subtotal_de_consumo}")
        
    bonificacion = (subtotal_de_consumo * porcentaje_beneficio) / 100

    recargo = (subtotal_de_consumo * porcentaje_recargo) / 100


    subtotal_con_recargo = subtotal_de_consumo + recargo

    subtotal_con_bonificaciones = subtotal_de_consumo - bonificacion

    #calculo del iva

    iva_aplicado_a_consumo = subtotal_de_consumo * iva / 100

    iva_a_sub_recargo = subtotal_con_recargo * iva / 100

    iva_a_sub_bonificaciones = subtotal_con_bonificaciones * iva / 100

    # totales con iva incluido

    total_con_iva = subtotal_de_consumo + iva_aplicado_a_consumo

    total_con_recargo_mas_iva = subtotal_con_recargo + iva_a_sub_recargo

    total_con_bonificacion_mas_iva = subtotal_con_bonificaciones + iva_a_sub_bonificaciones
    
    if bonificacion == 0 and recargo != 0:
        print(f" El recargo aplicado es: ${recargo}\n El subtotal con recargo es: ${subtotal_con_recargo}\n El IVA aplicado al subtotal de recargo es: {iva_a_sub_recargo}\n El total mas el recargo con IVA es: ${total_con_recargo_mas_iva}")
    elif recargo == 0 and bonificacion != 0:
        print(f" La bonificacion aplicada es: ${bonificacion}\n El subtotal con bonificaciones es: ${subtotal_con_bonificaciones}\n El iva aplicado al subtotal de bonificaciones es: ${iva_a_sub_bonificaciones}\n El total bonificado mas IVA es: ${total_con_bonificacion_mas_iva}")
    else:
        print(f" El IVA aplicado al consumo es: ${iva_aplicado_a_consumo}\n El total con IVA es: ${total_con_iva}")
else:
    print("INGRESE UN NUMERO MAYOR A CERO")


