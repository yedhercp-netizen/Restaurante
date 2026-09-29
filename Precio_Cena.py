def Menu():
    from Helpers import verificacion_seguimiento
    from Helpers import Verificacion_Existencia
    from Helpers import Verificacion_Cuenta_Cancelada
    print("""== Menu de Peru Lindo ==""")
    Menu = {
    "1": "Ceviche",
    "2": "Lomo Saltado",
    "3": "Ají de Gallina",
    "4": "Arroz Chaufa",
    "5": "Anticuchos",
    "6": "Papa a la Huancaína",
    "7": "Causa Rellena",
    "8": "Pollo a la Brasa",
    "9": "Tallarines Verdes",
    "10": "Suspiro a la Limeña"
    }
    nombre_input = input("Ingresa su nombre: ").upper()
    if verificacion_seguimiento(nombre_input):
        return
    Telefono_input = input("Ingrese su telefono: ").upper()
    if verificacion_seguimiento(Telefono_input):
        return
    Dia_input = input("Ingrese el dia de la reservacion: ").upper()
    if verificacion_seguimiento(Dia_input):
        return
    Mes_input = input("Ingrese el mes de la reservacion: ").upper()
    if verificacion_seguimiento(Mes_input):
        return
    Hora_input = input("Ingrese la hora de la reservacion: ").upper()
    if verificacion_seguimiento(Hora_input):
        return
    info_Cliente = (f"Telefono: {Telefono_input} / Nombre: {nombre_input} / Hora: {Hora_input} / Dia: {Dia_input} / Mes: {Mes_input} / Año: 2026 / Reserva: Activa / Comida: nada \r")
    if not Verificacion_Cuenta_Cancelada(info_Cliente):
        return print("Esta reservacion ya a sido utilisada o se a caducado")
    if Verificacion_Existencia(info_Cliente):
        return print("Esta reservacion no existe")
    numero = 1
    for i in Menu.values():
        print(numero, i)
        numero += 1    
    accion = input("Por favor ingrese el numero de la comida que quiere: ")
    if verificacion_seguimiento(accion):
        return
    if accion in Menu:
        print("Se a pedido: " + Menu[accion])
        with open("Historial_Restaurante.txt", "r") as HR:
            lineas = HR.readlines()

        with open("Historial_Restaurante.txt", "w") as HR:
            for i in lineas:
                if i.strip() != info_Cliente.strip():
                    HR.write(i)

        with open("Historial_Restaurante.txt", "a") as HR:
            info_Cliente_new = (f"Telefono: {Telefono_input} / Nombre: {nombre_input} / Hora: {Hora_input} / Dia: {Dia_input} / Mes: {Mes_input} / Año: 2026 / Reserva: Desactiva / Comida: {Menu[accion]} \r")
            HR.write(info_Cliente_new)
    else:
        return print("Esa comida no esta en el menu")
Menu()