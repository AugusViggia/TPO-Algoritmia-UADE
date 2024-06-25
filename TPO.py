## menu con el while y la bandera
## ordenar de mayor a menor sin sorted punto 2 y 3
## borrar lineas que no sirvan
## optimizar el codigo


import random

def generar_invitados():
    return random.randint(50, 200)

def generar_eventos():
    eventos = []
    for _ in range(random.randint(10, 30)):
        tipoDeEvento = random.choice(["casamiento", "15 años", "cumpleaños", "bautismo", "otros"])
        invitados = generar_invitados()
        eventos.append([tipoDeEvento, invitados])
    return eventos

# Generar eventos al inicio
eventos = generar_eventos()
print(eventos)

bandera = True
precioFijo50 = [750000, 850000, 650000, 750000, 800000]
precioAdicional100 = [6500, 7500, 5500, 6500, 6500]
precioAdicional200 = [7000, 8000, 6000, 7000, 8000]
costoPorEvento = [160000, 180000, 160000, 170000, 180000]
totales = []

for evento in eventos:
    if evento[0] == "casamiento":
        if evento[1] == 50:
            costoInvitado = costoPorEvento[0] + (50 * 2500)
        elif 50 < evento[1] <= 100:
            costoFacturacion = costoPorEvento[0] + (6500 * evento[1])
            costoInvitado = costoPorEvento[0] + (evento[1] * 2500)
        elif 100 < evento[1] <= 200:
            costoFacturacion = costoPorEvento[0] + (7000 * evento[1])
            costoInvitado = costoPorEvento[0] + (evento[1] * 2500)
        else:
            print("Numero de invitados no valido")
            
    elif evento[0] == "15 años":
        if evento[1] == 50:
            costoInvitado = costoPorEvento[1] + (50 * 2500)
        elif 50 < evento[1] <= 100:
            costoFacturacion = costoPorEvento[1] + (7500 * evento[1])
            costoInvitado = costoPorEvento[1] + (evento[1] * 2500)
        elif 100 < evento[1] <= 200:
            costoFacturacion = costoPorEvento[1] + (8000 * evento[1])
            costoInvitado = costoPorEvento[1] + (evento[1] * 2500)
        else:
            print("Numero de invitados no valido")
            
    elif evento[0] == "cumpleaños":
        if evento[1] == 50:
            costoInvitado = costoPorEvento[2] + (50 * 2500)
        elif 50 < evento[1] <= 100:
            costoFacturacion = costoPorEvento[2] + (5500 * evento[1])
            costoInvitado = costoPorEvento[2] + (evento[1] * 2500)
        elif 100 < evento[1] <= 200:
            costoFacturacion = costoPorEvento[2] + (6000 * evento[1])
            costoInvitado = costoPorEvento[2] + (evento[1] * 2500)
        else:
            print("Numero de invitados no valido")

    elif evento[0] == "bautismo":
        if evento[1] == 50:
            costoInvitado = costoPorEvento[3] + (50 * 2500)
        elif 50 < evento[1] <= 100:
            costoFacturacion = costoPorEvento[3] + (6500 * evento[1])
            costoInvitado = costoPorEvento[3] + (evento[1] * 2500)
        elif 100 < evento[1] <= 200:
            costoFacturacion = costoPorEvento[3] + (7000 * evento[1])
            costoInvitado = costoPorEvento[3] + (evento[1] * 2500)
        else:
            print("Numero de invitados no valido")

    elif evento[0] == "otros":
        if evento[1] == 50:
            costoInvitado = costoPorEvento[4] + (50 * 2500)
        elif 50 < evento[1] <= 100:
            costoFacturacion = costoPorEvento[4] + (6500 * evento[1])
            costoInvitado = costoPorEvento[4] + (evento[1] * 2500)
        elif 100 < evento[1] <= 200:
            costoFacturacion = costoPorEvento[4] + (7000 * evento[1])
            costoInvitado = costoPorEvento[4] + (evento[1] * 2500)
        else:
            print("Numero de invitados no valido")
            
    if costoFacturacion:
        evento.extend([costoFacturacion])
            
# Crear listas para almacenar la facturación, costo y cantidad de cada tipo de evento
facturacion_casamiento = cantidad_casamiento = 0
facturacion_15 = cantidad_15 = 0
facturacion_cumple = cantidad_cumple = 0
facturacion_bautismo = cantidad_bautismo = 0
facturacion_otros = cantidad_otros = 0

# Recorrer la lista de eventos
for evento in eventos:
    tipoDeEvento, invitados, *_ = evento

    if tipoDeEvento == "casamiento":
        facturacion_casamiento += costoFacturacion
        costo_casamiento = costoPorEvento[0]
        cantidad_casamiento += 1
    elif tipoDeEvento == "15 años":
        facturacion_15 += costoFacturacion
        costo_15 = costoPorEvento[1]
        cantidad_15 += 1
    elif tipoDeEvento == "cumpleaños":
        facturacion_cumple += costoFacturacion
        costo_cumple = costoPorEvento[2]
        cantidad_cumple += 1
    elif tipoDeEvento == "bautismo":
        facturacion_bautismo += costoFacturacion
        costo_bautismo = costoPorEvento[3]
        cantidad_bautismo += 1
    else:
        facturacion_otros += costoFacturacion
        costo_otros = costoPorEvento[4]
        cantidad_otros += 1
            
# Iniciar el bucle principal
while bandera:
    print("\nMenú")
    print("1. Total de la facturación del mes, el costo y cuantos eventos fueron")
    print("2. Total de facturación, costo y cantidad de cada tipo de evento")
    print("3. Total de facturación de cada tipo de evento, ordenado de mayor a menor")
    print("4. Ingresar un tipo de evento y mostrar la facturación y cantidad de invitados")
    print("5. Salir\n")

    # Solicitar la opción del usuario
    opcion = (input("Ingrese la opción: "))
    # Opción 1: Calcular el total de la facturación del mes, el costo y cuantos eventos fueron
    if opcion == "1":
        print("You selected option 1")

        # Calcular el costo y la facturación en función del tipo de evento y el número de invitados

            # Agregar el evento a la lista de eventos
        

        # Calcular los totales
        total_facturacion = 0
        total_costo = 0
        
        for evento in eventos:
            total_facturacion += costoFacturacion
            
        for evento in eventos:
            total_costo += costoInvitado
            
        total_eventos = len(eventos)

        # Imprimir los totales
        print(f"Total facturación: {total_facturacion}, total costo: {total_costo}, total eventos: {total_eventos}")
        totales.append([total_facturacion, total_eventos])
        print()
        pass

##-------------------------------------------------------------------------------##

#PUNTO 2

    elif opcion == "2":
        print("You selected option 2")

        totales = [
            ("casamiento", facturacion_casamiento, costo_casamiento, cantidad_casamiento),
            ("15 años", facturacion_15, costo_15, cantidad_15),
            ("cumpleaños", facturacion_cumple, costo_cumple, cantidad_cumple),
            ("bautismo", facturacion_bautismo, costo_bautismo, cantidad_bautismo),
            ("otros", facturacion_otros, costo_otros, cantidad_otros),
        ]

        def obtener_facturacion(total):
            return total[1]

        # Ordenar la lista por facturación
        totales_ordenados = sorted(totales, key=obtener_facturacion, reverse=True)

        for total in totales_ordenados:
                print(f"Tipo de evento: {total[0]}, Total facturación: {total[1]}, Total costo: {total[2]}, Cantidad de eventos: {total[3]}")        
        print()

##-------------------------------------------------------------------------------##

#PUNTO 3
    elif opcion == "3":
        print("You selected option 3")
        # Ordenar la lista por facturación total PUNTO 3
        totales_facturacion = [
            ("casamiento", facturacion_casamiento),
            ("15 años", facturacion_15),
            ("cumpleaños", facturacion_cumple),
            ("bautismo", facturacion_bautismo),
            ("otros", facturacion_otros),
        ]

        # Define la función de ordenamiento
        def obtener_facturacion_total(ordenado):
            return ordenado[1]

        # Ordena la lista usando la función de ordenamiento
        totales_facturacion_ordenados = sorted(totales_facturacion, key=obtener_facturacion_total, reverse=True)
        for evento in totales_facturacion_ordenados:
            print(f"Tipo de evento: {evento[0]}, Total facturación: {evento[1]}")
        print()

##-------------------------------------------------------------------------------##

#Punto 4
    elif opcion == "4":
        print("You selected option 4")
        eventoIngresado = input("Ingrese el tipo de evento: ").lower().strip()
        eventoEncontrado = False


        for evento in eventos:
            tipoDeEvento, invitados, costoFacturacion = evento
            if eventoIngresado == tipoDeEvento:
                print("Facturacion del evento:",costoFacturacion, " Cantidad de invitados:",invitados)
                eventoEncontrado = True

        if eventoEncontrado:  
            print("No se encontraron eventos de este tipo")

        print()
        
##-------------------------------------------------------------------------------##
#PUNTO 5
    elif opcion == "5":
        print("You selected option 5")
        bandera = False
        print("Gracias por utilizar el programa")

    else:
        print("Opción no válida")
        pass