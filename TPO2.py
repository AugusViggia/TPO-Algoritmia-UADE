## menu con el while y la bandera
## ordenar de mayor a menor sin sorted punto 2 y 3
## borrar lineas que no sirvan
## optimizar el codigo


import random

# Inicializar la bandera y la lista de eventos
eventos = []

# Definir una función para generar un número aleatorio de invitados
def generar_invitados():
    return random.randint(50, 201)

# Generar un número aleatorio de eventos
for _ in range(random.randint(10, 31)):
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

##-------------------------------------------------------------------------------##

#PUNTO 2
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

# Crear una lista con los totales de cada tipo de evento
# totales = [
#     (f"casamiento, facturacion: {facturacion_casamiento}, costo: {costo_casamiento}, cantidad: {cantidad_casamiento}"),
#     (f"15 años, facturacion: {facturacion_15}, costo: {costo_15}, cantidad: {cantidad_15}"),
#     (f"cumpleaños, facturacion: {facturacion_cumple}, costo: {costo_cumple}, cantidad: {cantidad_cumple}"),
#     (f"bautismo, facturacion: {facturacion_bautismo}, costo: {costo_bautismo}, cantidad: {cantidad_bautismo}"),
#     (f"otros, facturacion: {facturacion_otros}, costo: {costo_otros}, cantidad: {cantidad_otros}"),
# ]

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

# # Definir una función para obtener la facturación de un total
# print("Los totales ordenados son: ", totales_ordenados)
# print()   

##-------------------------------------------------------------------------------##

#PUNTO 3
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
eventoIngresado = input("Ingrese el tipo de evento: ").lower().strip()

for evento in eventos:
    tipoDeEvento, invitados, costo, costoFacturacion = evento
    if eventoIngresado == tipoDeEvento:
        print("Facturacion del evento:",costoFacturacion, " Cantidad de invitados:",invitados)

if eventoIngresado != tipoDeEvento or costoFacturacion == 0:
        print("No se encontraron eventos de este tipo")
        pass

print()

