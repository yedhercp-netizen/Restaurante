def alta():
    from Helpers import Verificacion_Existencia
    from Helpers import verificacion_seguimiento
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
    info_Cliente = (f"Telefono: {Telefono_input} / Nombre: {Nombre_input}")
    if Verificacion_Existencia(info_Cliente):
        return print("Esta reserva ya a sido tomada")
    with open("Historial_Restaurante.txt", "a") as HR:
        HR.write(info_Cliente + "\r")