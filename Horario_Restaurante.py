def Dia(Variable):
    from datetime import date
    dia = int(Variable)
    dia_hoy = date.today().day
    if dia >= dia_hoy:
        return True
    else:
        print("Ese dia ya a pasado")
        return False

def Mes(Variable):
    from datetime import date
    mes = Variable
    mes_hoy = date.today().month
    if int(mes) >= int(mes_hoy):
        return True
    else:
        print("Esa fecha ya a pasado")
        return False

def horarios():
    from Helpers import Verificacion_Existencia
    from Helpers import verificacion_seguimiento
    meses = [
        "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO",
        "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE",
        "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
        ]
    Telefono_input = input("\nIngrese su numero de telefono: ").upper()
    if not Telefono_input.isnumeric():
        return print("Solo puede ingresar numeros")
    if verificacion_seguimiento(Telefono_input):
        return
    Nombre_input = input("\nIngrese su nombre: ").upper()
    if not Nombre_input.replace(" ", "").isalpha():
        return print("Solo puedes ingresar letras")
    if verificacion_seguimiento(Nombre_input):
        return
    Dia_input = input("\nIngrese el día que quiere reservar: ").upper()
    if not Telefono_input.isnumeric():
        return print("Solo puede ingresar numeros")
    if verificacion_seguimiento(Dia_input):
        return
    numero = 1
    for i in meses:
        print(numero, i)
        numero += 1
    Mes_input = input("\nIngrese el mes que quiere reservar: ").upper()
    if not Mes_input.replace(" ", "").isnumeric():
            return print("Solo puedes ingresar numeros")
    if not Mes(Mes_input):
        return
    if verificacion_seguimiento(Mes_input):
        return
    Hora_input = input("\nIngrese la hora al la que van a lleguar [Estamos abiertos desde las 10-22]:  ").upper()
    if not Telefono_input.isnumeric():
        return print("Solo puede ingresar numeros")
    if verificacion_seguimiento(Hora_input):
        return
    if int(Hora_input) < 10 and int(Hora_input) > 22:
        return("Favor de solo ingresar de la hora que se indica")
    info_Cliente = (f"Telefono: {Telefono_input} / Nombre: {Nombre_input} / Hora: {Hora_input} / Dia: {Dia_input} / Mes: {Mes_input} / Año: 2026 / Reserva: Activa / Comida: nada")
    if Verificacion_Existencia(info_Cliente):
        return print("Esta reserva ya a sido tomada")
    with open("Historial_Restaurante.txt", "a") as HR:
        HR.write(info_Cliente + "\r")