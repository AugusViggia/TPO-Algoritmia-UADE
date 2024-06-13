import random
numero_aleatorio_eventos_por_mes = random.randint(10, 30)
numero_aleatorio_invitados_por_fiesta = random.randint(50, 200)

personas = 0

costoFacturacion = 0

costoInvitado = 0

tipoDeEvento = (input("Ingrese el tipo de evento que desea realizar: "))

if tipoDeEvento == "casamiento":
    costo = 160000
    
    if numero_aleatorio_invitados_por_fiesta == 50:
        costoFacturacion = 750000
        costoInvitado = costo + (50 * 2500)
        
        if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
            for i in range(50, 101):
                costoFacturacion = costo + (6500*i)
                costoInvitado = costo + (i * 2500)
        elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
            for i in range(101, 201):
                costoFacturacion = costo + (6000*i)
                costoInvitado = costo + (i * 2500)
    else:
        print("Numero de invitados no valido")
    
if tipoDeEvento == "15 años":
    costo = 180000
    
    if numero_aleatorio_invitados_por_fiesta == 50:
        costoFacturacion = 850000
        costoInvitado = costo + (50 * 2500)
        
        if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
            for i in range(50, 101):
                costoFacturacion = costo + (7500*i)
                costoInvitado = costo + (i * 2500)
        elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
            for i in range(101, 201):
                costoFacturacion = costo + (8000*i)
                costoInvitado = costo + (i * 2500)
    else:
        print("Numero de invitados no valido")

if tipoDeEvento == "cumpleaños":
    costo = 160000
    
    
    if numero_aleatorio_invitados_por_fiesta == 50:
        costoFacturacion = 650000
        costoInvitado = costo + (50 * 2500)
        if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
            for i in range(50, 101):
                costoFacturacion = costo + (5500*i)
                costoInvitado = costo + (i * 2500)
        elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
            for i in range(101, 201):
                costoFacturacion = costo + (6000*i)
                costoInvitado = costo + (i * 2500)
    else:
        print("Numero de invitados no valido")
    
    
if tipoDeEvento == "bautismo":
    costo = 170000
    
    if numero_aleatorio_invitados_por_fiesta == 50:
        costoFacturacion = 750000
        costoInvitado = costo + (50 * 2500)
        if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
            for i in range(50, 101):
                costoFacturacion = costo + (6500*i)
                costoInvitado = costo + (i * 2500)
        elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
            for i in range(101, 201):
                costoFacturacion = costo + (7000*i)
                costoInvitado = costo + (i * 2500)
    else:
        print("Numero de invitados no valido")
    
    
if tipoDeEvento == "otros":
    costo = 180000

    if numero_aleatorio_invitados_por_fiesta == 50:
        costoFacturacion = 800000
        costoInvitado = costo + (50 * 2500)
        
        if numero_aleatorio_invitados_por_fiesta > 50 and numero_aleatorio_invitados_por_fiesta <= 100:
            for i in range(50, 101):
                costoFacturacion = costo + (7000*i)
                costoInvitado = costo + (i * 2500)
        elif numero_aleatorio_invitados_por_fiesta > 100 and numero_aleatorio_invitados_por_fiesta <= 200:
            for i in range(101, 201):
                costoFacturacion = costo + (8000*i)
                costoInvitado = costo + (i * 2500)
    else:
        print("Numero de invitados no valido")
        

print(costoFacturacion)
print(costoInvitado)