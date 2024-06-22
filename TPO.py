# import random
# numero_aleatorio_eventos_por_mes = random.randint(10, 30)
# numero_aleatorio_invitados_por_fiesta = random.randint(50, 200)

# personas = 0

# costoFacturacion = 0

# costoInvitado = 0

# tipoDeEvento = (input("Ingrese el tipo de evento que desea realizar: "))

# if tipoDeEvento == "casamiento":
#     costo = 160000
    
#     if numero_aleatorio_invitados_por_fiesta == 50:
#         costoFacturacion = 750000
#         costoInvitado = costo + (50 * 2500)
        
#         if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
#             for i in range(50, 101):
#                 costoFacturacion = costo + (6500*i)
#                 costoInvitado = costo + (i * 2500)
#         elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
#             for i in range(101, 201):
#                 costoFacturacion = costo + (6000*i)
#                 costoInvitado = costo + (i * 2500)
#     else:
#         print("Numero de invitados no valido")
    
# if tipoDeEvento == "15 años":
#     costo = 180000
    
#     if numero_aleatorio_invitados_por_fiesta == 50:
#         costoFacturacion = 850000
#         costoInvitado = costo + (50 * 2500)
        
#         if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
#             for i in range(50, 101):
#                 costoFacturacion = costo + (7500*i)
#                 costoInvitado = costo + (i * 2500)
#         elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
#             for i in range(101, 201):
#                 costoFacturacion = costo + (8000*i)
#                 costoInvitado = costo + (i * 2500)
#     else:
#         print("Numero de invitados no valido")

# if tipoDeEvento == "cumpleaños":
#     costo = 160000
    
    
#     if numero_aleatorio_invitados_por_fiesta == 50:
#         costoFacturacion = 650000
#         costoInvitado = costo + (50 * 2500)
#         if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
#             for i in range(50, 101):
#                 costoFacturacion = costo + (5500*i)
#                 costoInvitado = costo + (i * 2500)
#         elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
#             for i in range(101, 201):
#                 costoFacturacion = costo + (6000*i)
#                 costoInvitado = costo + (i * 2500)
#     else:
#         print("Numero de invitados no valido")
    
    
# if tipoDeEvento == "bautismo":
#     costo = 170000
    
#     if numero_aleatorio_invitados_por_fiesta == 50:
#         costoFacturacion = 750000
#         costoInvitado = costo + (50 * 2500)
#         if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
#             for i in range(50, 101):
#                 costoFacturacion = costo + (6500*i)
#                 costoInvitado = costo + (i * 2500)
#         elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
#             for i in range(101, 201):
#                 costoFacturacion = costo + (7000*i)
#                 costoInvitado = costo + (i * 2500)
#     else:
#         print("Numero de invitados no valido")
    
    
# if tipoDeEvento == "otros":
#     costo = 180000

#     if numero_aleatorio_invitados_por_fiesta == 50:
#         costoFacturacion = 800000
#         costoInvitado = costo + (50 * 2500)
        
#         if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
#             for i in range(50, 101):
#                 costoFacturacion = costo + (7000*i)
#                 costoInvitado = costo + (i * 2500)
#         elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
#             for i in range(101, 201):
#                 costoFacturacion = costo + (8000*i)
#                 costoInvitado = costo + (i * 2500)
#     else:
#         print("Numero de invitados no valido")
        

# print(costoFacturacion)
# print(costoInvitado)


#Primer punto
import random

# Inicializar la bandera y la lista de eventos
bandera=True
eventos = []

# Iniciar el bucle principal
while bandera:
    # Imprimir el menú de opciones
    print()
    print("Menú")
    print("1. Total de la facturación del mes, el costo y cuantos eventos fueron")
    print("2. Total de facturación, costo y cantidad de cada tipo de evento")
    print("3. Total de facturación de cada tipo de evento, ordenado de mayor a menor")
    print("4. Ingresar un tipo de evento y mostrar la facturación y cantidad de invitados")
    print("5. Salir")
    print()

    # Solicitar la opción del usuario
    opcion = (input("Ingrese la opción: "))

    # Opción 1: Calcular el total de la facturación del mes, el costo y cuantos eventos fueron
    if opcion == "1":
        print("You selected option 1")

        # Definir una función para generar un número aleatorio de invitados
        def generar_invitados():
            return random.randint(50, 200)

        # Generar un número aleatorio de eventos
        for _ in range(random.randint(10, 30)):
            # Generar un tipo de evento aleatorio
            tipoDeEvento = random.choice(["casamiento", "15 años", "cumpleaños", "bautismo", "otros"])  

            # Generar un número aleatorio de invitados
            invitados = generar_invitados()

            # Calcular el costo y la facturación en función del tipo de evento y el número de invitados
            if tipoDeEvento == "casamiento":
                costo = 160000
                if invitados == 50:
                    costoFacturacion = 750000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < invitados <= 100:
                    costoFacturacion = costo + (6500 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                elif 100 < invitados <= 200:
                    costoFacturacion = costo + (7000 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                else:
                    print("Numero de invitados no valido")
                    
            elif tipoDeEvento == "15 años":
                costo = 180000
                if invitados == 50:
                    costoFacturacion = 850000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < invitados <= 100:
                    costoFacturacion = costo + (7500 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                elif 100 < invitados <= 200:
                    costoFacturacion = costo + (8000 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                else:
                    print("Numero de invitados no valido")
                    
            elif tipoDeEvento == "cumpleaños":
                costo = 160000
                if invitados == 50:
                    costoFacturacion = 650000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < invitados <= 100:
                    costoFacturacion = costo + (5500 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                elif 100 < invitados <= 200:
                    costoFacturacion = costo + (6000 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                else:
                    print("Numero de invitados no valido")

            elif tipoDeEvento == "bautismo":
                costo = 170000
                if invitados == 50:
                    costoFacturacion = 750000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < invitados <= 100:
                    costoFacturacion = costo + (6500 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                elif 100 < invitados <= 200:
                    costoFacturacion = costo + (7000 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                else:
                    print("Numero de invitados no valido")

            elif tipoDeEvento == "otros":
                costo = 180000
                if invitados == 50:
                    costoFacturacion = 800000
                    costoInvitado = costo + (50 * 2500)
                elif 50 < invitados <= 100:
                    costoFacturacion = costo + (6500 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                elif 100 < invitados <= 200:
                    costoFacturacion = costo + (7000 * invitados)
                    costoInvitado = costo + (invitados * 2500)
                else:
                    print("Numero de invitados no valido")
               
            # Agregar el evento a la lista de eventos
            eventos.append([tipoDeEvento, invitados, costo, costoFacturacion])

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
        print()
        pass


    elif opcion == "2":
        #Punto 2
        eventos = []
        # Crear listas para almacenar la facturación, costo y cantidad de cada tipo de evento
        facturacion_casamiento = costo_casamiento = cantidad_casamiento = 0
        facturacion_15 = costo_15 = cantidad_15 = 0
        facturacion_cumple = costo_cumple = cantidad_cumple = 0
        facturacion_bautismo = costo_bautismo = cantidad_bautismo = 0
        facturacion_otros = costo_otros = cantidad_otros = 0

        # Recorrer la lista de eventos
        for evento in eventos:
            tipoDeEvento, invitados, costo, facturacion = evento

            # Agregar la facturación y el costo al tipo de evento correspondiente
            if tipoDeEvento == "casamiento":
                facturacion_casamiento += facturacion
                costo_casamiento += costo
                cantidad_casamiento += 1
            elif tipoDeEvento == "15 años":
                facturacion_15 += facturacion
                costo_15 += costo
                cantidad_15 += 1
            elif tipoDeEvento == "cumpleaños":
                facturacion_cumple += facturacion
                costo_cumple += costo
                cantidad_cumple += 1
            elif tipoDeEvento == "bautismo":
                facturacion_bautismo += facturacion
                costo_bautismo += costo
                cantidad_bautismo += 1
            else:
                facturacion_otros += facturacion
                costo_otros += costo
                cantidad_otros += 1

        # Crear una lista con los totales de cada tipo de evento
        totales = [
            ("casamiento", facturacion_casamiento, costo_casamiento, cantidad_casamiento),
            ("15 años", facturacion_15, costo_15, cantidad_15),
            ("cumpleaños", facturacion_cumple, costo_cumple, cantidad_cumple),
            ("bautismo", facturacion_bautismo, costo_bautismo, cantidad_bautismo),
            ("otros", facturacion_otros, costo_otros, cantidad_otros),
        ]

        # Definir una función para obtener la facturación de un total
        def obtener_facturacion(total):
            return total[1]

        # Ordenar la lista por facturación
        totales_ordenados = sorted(totales, key=obtener_facturacion, reverse=True)

        # Mostrar los resultados
        for total in totales_ordenados:
            print(f"Tipo de evento: {total[0]}, Total facturación: {total[1]}, Total costo: {total[2]}, Cantidad de eventos: {total[3]}")

        print()   
        pass 

    elif opcion == "3":
        #Punto 3    
        eventos = []
        # Crear listas para almacenar la facturación, costo y cantidad de cada tipo de evento
        facturacion_casamiento = costo_casamiento = cantidad_casamiento = 0
        facturacion_15 = costo_15 = cantidad_15 = 0
        facturacion_cumple = costo_cumple = cantidad_cumple = 0
        facturacion_bautismo = costo_bautismo = cantidad_bautismo = 0
        facturacion_otros = costo_otros = cantidad_otros = 0
        # Crear una lista con los totales de facturación de cada tipo de evento
        totales_facturacion = [
            ("casamiento", facturacion_casamiento),
            ("15 años", facturacion_15),
            ("cumpleaños", facturacion_cumple),
            ("bautismo", facturacion_bautismo),
            ("otros", facturacion_otros),
        ]

        # Ordenar la lista por facturación total
        # Define la función de ordenamiento
        def obtener_facturacion_total(ordenado):
            return ordenado[1]

        # Ordena la lista usando la función de ordenamiento
        totales_facturacion_ordenados = sorted(totales_facturacion, key=obtener_facturacion_total, reverse=True)
        for evento in totales_facturacion_ordenados:
            print(f"Tipo de evento: {evento[0]}, Total facturación: {evento[1]}")
        print()
        pass

    elif opcion == "4":
        #Punto 4
        import random
        eventos = []
        # Crear listas para almacenar la facturación, costo y cantidad de cada tipo de evento
        facturacion_casamiento = costo_casamiento = cantidad_casamiento = 0
        facturacion_15 = costo_15 = cantidad_15 = 0
        facturacion_cumple = costo_cumple = cantidad_cumple = 0
        facturacion_bautismo = costo_bautismo = cantidad_bautismo = 0
        facturacion_otros = costo_otros = cantidad_otros = 0

        # Definir las variables de los invitados para cada tipo de evento
        invitados_casamiento = random.randint(50, 200)  
        invitados_15 = random.randint(50, 200)  
        invitados_cumple = random.randint(50, 200)  
        invitados_bautismo = random.randint(50, 200)  
        invitados_otros = random.randint(50, 200)
        eventos = {
            "casamiento": {"facturacion": facturacion_casamiento, "invitados": invitados_casamiento},
            "15 años": {"facturacion": facturacion_15, "invitados": invitados_15},
            "cumpleaños": {"facturacion": facturacion_cumple, "invitados": invitados_cumple},
            "bautismo": {"facturacion": facturacion_bautismo, "invitados": invitados_bautismo},
            "otros": {"facturacion": facturacion_otros, "invitados": invitados_otros},
        }

        tipo_evento = input("Ingrese el tipo de evento: ").lower().strip()

        # Verifica si el tipo de evento ingresado está en el diccionario de eventos
        if tipo_evento in eventos:
            evento = eventos[tipo_evento]
            print(f"Facturación: {evento['facturacion']}, Cantidad de invitados: {evento['invitados']}")
        else:
            print("El tipo de evento ingresado no existe.")
        
        print()
        pass
    elif opcion == "5":
        bandera=False
        print("Gracias por usar el programa")
        
    else: print("Opción no válida, intente de nuevo.")