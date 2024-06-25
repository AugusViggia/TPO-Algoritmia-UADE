## menu con el while y la bandera
## ordenar de mayor a menor sin sorted punto 2 y 3
## borrar lineas que no sirvan
## optimizar el codigo


import random

def generar_invitados():
    return random.randint(50, 201)

def generar_eventos():
    eventos = []
    for _ in range(random.randint(10, 31)):
        tipoDeEvento = random.choice(["casamiento", "15 años", "cumpleaños", "bautismo", "otros"])
        invitados = generar_invitados()
        eventos.append([tipoDeEvento, invitados])
    return eventos

# Generar eventos al inicio
eventos = generar_eventos()
print(eventos)

bandera = True

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
        for evento in eventos:
            if evento[0] == "casamiento":
                costo = 160000
                if evento[1] == 50:
                    costoFacturacion = 750000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < evento[1] <= 100:
                    costoFacturacion = costo + (6500 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                elif 100 < evento[1] <= 200:
                    costoFacturacion = costo + (7000 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                else:
                    print("Numero de invitados no valido")
                    
            elif evento[0] == "15 años":
                costo = 180000
                if evento[1] == 50:
                    costoFacturacion = 850000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < evento[1] <= 100:
                    costoFacturacion = costo + (7500 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                elif 100 < evento[1] <= 200:
                    costoFacturacion = costo + (8000 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                else:
                    print("Numero de invitados no valido")
                    
            elif evento[0] == "cumpleaños":
                costo = 160000
                if evento[1] == 50:
                    costoFacturacion = 650000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < evento[1] <= 100:
                    costoFacturacion = costo + (5500 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                elif 100 < evento[1] <= 200:
                    costoFacturacion = costo + (6000 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                else:
                    print("Numero de invitados no valido")

            elif evento[0] == "bautismo":
                costo = 170000
                if evento[1] == 50:
                    costoFacturacion = 750000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < evento[1] <= 100:
                    costoFacturacion = costo + (6500 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                elif 100 < evento[1] <= 200:
                    costoFacturacion = costo + (7000 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                else:
                    print("Numero de invitados no valido")

            elif evento[0] == "otros":
                costo = 180000
                if evento[1] == 50:
                    costoFacturacion = 800000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < evento[1] <= 100:
                    costoFacturacion = costo + (6500 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                elif 100 < evento[1] <= 200:
                    costoFacturacion = costo + (7000 * evento[1])
                    costoInvitado = costo + (evento[1] * 2500)
                else:
                    print("Numero de invitados no valido")

            # Agregar el evento a la lista de eventos
            if costo and costoFacturacion:
                evento.extend([costo, costoFacturacion])
        

        # Calcular los totales
        total_facturacion = 0
        for evento in eventos:
            total_facturacion += evento[3]
            
        total_costo = 0
        for evento in eventos:
            total_costo += evento[2]
            
        total_eventos = len(eventos)

        # Imprimir los totales
        print(f"Total facturación: {total_facturacion}, total costo: {total_costo}, total eventos: {total_eventos}")
        print(eventos)
        print()
        pass

##-------------------------------------------------------------------------------##

#PUNTO 2

    elif opcion == "2":
        print("You selected option 2")
# Crear listas para almacenar la facturación, costo y cantidad de cada tipo de evento
        facturacion_casamiento = costo_casamiento = cantidad_casamiento = 0
        facturacion_15 = costo_15 = cantidad_15 = 0
        facturacion_cumple = costo_cumple = cantidad_cumple = 0
        facturacion_bautismo = costo_bautismo = cantidad_bautismo = 0
        facturacion_otros = costo_otros = cantidad_otros = 0

        # Recorrer la lista de eventos
        for evento in eventos:
            tipoDeEvento, invitados, costo, costoFacturacion = evento

            # Agregar la facturación y el costo al tipo de evento correspondiente
            if tipoDeEvento == "casamiento":
                facturacion_casamiento += costoFacturacion
                costo_casamiento += costo
                cantidad_casamiento += 1
            elif tipoDeEvento == "15 años":
                facturacion_15 += costoFacturacion
                costo_15 += costo
                cantidad_15 += 1
            elif tipoDeEvento == "cumpleaños":
                facturacion_cumple += costoFacturacion
                costo_cumple += costo
                cantidad_cumple += 1
            elif tipoDeEvento == "bautismo":
                facturacion_bautismo += costoFacturacion
                costo_bautismo += costo
                cantidad_bautismo += 1
            else:
                facturacion_otros += costoFacturacion
                costo_otros += costo
                cantidad_otros += 1

        totales = [
            ("casamiento", facturacion_casamiento, costo_casamiento, cantidad_casamiento),
            ("15 años", facturacion_15, costo_15, cantidad_15),
            ("cumpleaños", facturacion_cumple, costo_cumple, cantidad_cumple),
            ("bautismo", facturacion_bautismo, costo_bautismo, cantidad_bautismo),
            ("otros", facturacion_otros, costo_otros, cantidad_otros),
        ]

        print("somos la lista eventos",eventos)

        def obtener_facturacion(total):
            return total[1]

        # Ordenar la lista por facturación
        totales_ordenados = sorted(totales, key=obtener_facturacion, reverse=True)

        for total in totales_ordenados:
                print(f"Tipo de evento: {total[0]}, Total facturación: {total[1]}, Total costo: {total[2]}, Cantidad de eventos: {total[3]}")        
        print()

        # # Definir una función para obtener la facturación de un total
        # print("Los totales ordenados son: ", totales_ordenados)
        # print()   

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

        for evento in eventos:
            tipoDeEvento, invitados, costo, costoFacturacion = evento
            if eventoIngresado == tipoDeEvento:
                print("Facturacion del evento:",costoFacturacion, " Cantidad de invitados:",invitados)

        if eventoIngresado != tipoDeEvento or costoFacturacion == 0:
                print("No se encontraron eventos de este tipo")
                pass

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

