#TPO 7 - SALON DE FIESTAS -

# Viggiano, Augusto
# Villanueva, Camilo
# Zolezzi, Juan

# Se pide realizar un programa que permita gestionar la facturación de un salón de fiestas.

import random

def generar_invitados():
    return random.randint(50, 200)

# Se generan eventos aleatorios con un tipo de evento y una cantidad de invitados.
def generar_eventos():
    eventos = []
    for _ in range(random.randint(10, 30)):
        tipoDeEvento = random.choice(["casamiento", "15 años", "cumpleaños", "bautismo", "otros"])
        invitados = generar_invitados()
        eventos.append([tipoDeEvento, invitados])
    return eventos

# Se generan los eventos.
eventos = generar_eventos()

bandera = True
precioFijo50 = [750000, 850000, 650000, 750000, 800000]
precioAdicional100 = [6500, 7500, 5500, 6500, 6500]
precioAdicional200 = [7000, 8000, 6000, 7000, 8000]
costoPorEvento = [160000, 180000, 160000, 170000, 180000]
totales = []

facturacion_casamiento = cantidad_casamiento = 0
facturacion_15 = cantidad_15 = 0
facturacion_cumple = cantidad_cumple = 0
facturacion_bautismo = cantidad_bautismo = 0
facturacion_otros = cantidad_otros = 0

# Se calcula el costo de cada evento.

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
        evento.append(costoFacturacion)

# Se calcula la facturación total de cada tipo de evento.
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
            
# Se muestra el menú.
while bandera:
    print("\nMenú")
    print("1. Total de la facturación del mes, el costo y cuantos eventos fueron")
    print("2. Total de facturación, costo y cantidad de cada tipo de evento")
    print("3. Total de facturación de cada tipo de evento, ordenado de mayor a menor")
    print("4. Ingresar un tipo de evento y mostrar la facturación y cantidad de invitados")
    print("5. Salir\n")

# Se pide al usuario que ingrese una opción.
    opcion = (input("Ingrese la opción: "))

    if opcion == "1":
        print("Seleccionaste la opcion 1")

        total_facturacion = 0
        total_costo = 0
        
# Se calcula la facturación total, el costo total y la cantidad de eventos.
        for evento in eventos:
            total_facturacion += costoFacturacion
            
        for evento in eventos:
            total_costo += costoInvitado
            
        total_eventos = len(eventos)

        print(f"Total facturación: {total_facturacion}, total costo: {total_costo}, total eventos: {total_eventos}")
        totales.append([total_facturacion, total_eventos])
        print()

    elif opcion == "2":
        print("Seleccionaste la opcion 2")

        totales = [
            ("casamiento", facturacion_casamiento, costo_casamiento, cantidad_casamiento),
            ("15 años", facturacion_15, costo_15, cantidad_15),
            ("cumpleaños", facturacion_cumple, costo_cumple, cantidad_cumple),
            ("bautismo", facturacion_bautismo, costo_bautismo, cantidad_bautismo),
            ("otros", facturacion_otros, costo_otros, cantidad_otros),
        ]

# Se ordenan los eventos de mayor a menor.

        
        for i in range(len(totales)):
            for j in range(i + 1, len(totales)):
                if totales[i][1] < totales[j][1]:
                    totales[i], totales[j] = totales[j], totales[i]
            print(f"Tipo de evento: {totales[i][0]}, Total facturación: {totales[i][1]}, Total costo: {totales[i][2]}, Cantidad de eventos: {totales[i][3]}")
        print()

    elif opcion == "3":
        print("Seleccionaste la opcion 3")

        totales_facturacion = [
            ("casamiento", facturacion_casamiento),
            ("15 años", facturacion_15),
            ("cumpleaños", facturacion_cumple),
            ("bautismo", facturacion_bautismo),
            ("otros", facturacion_otros),
        ]

# Se ordenan los eventos de mayor a menor.
        for i in range(len(totales_facturacion)):
            for j in range(i + 1, len(totales_facturacion)):
                if totales_facturacion[i][1] < totales_facturacion[j][1]:
                    totales_facturacion[i], totales_facturacion[j] = totales_facturacion[j], totales_facturacion[i]
            print(f"Tipo de evento: {totales_facturacion[i][0]}, Total facturación: {totales_facturacion[i][1]}")
        print()

    elif opcion == "4":
        print("Seleccionaste la opcion 4")
        eventoIngresado = input("Ingrese el tipo de evento: ").lower().strip()
        eventoEncontrado = False

# Se busca el evento ingresado por el usuario.
        for evento in eventos:
            tipoDeEvento, invitados, costoFacturacion = evento
            if eventoIngresado == tipoDeEvento:
                print("Facturacion del evento:",costoFacturacion, " Cantidad de invitados:",invitados)
                eventoEncontrado = True

# Se muestra un mensaje si no se encontraron eventos.
        if eventoEncontrado == False:  
            print("No se encontraron eventos de este tipo")
        print()
        
# Se finaliza el programa.
    elif opcion == "5":
        print("Seleccionaste la opcion 5")
        bandera = False
        print("Gracias por utilizar el programa")

    else:
        print("Opción no válida")