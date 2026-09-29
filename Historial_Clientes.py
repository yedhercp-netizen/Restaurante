def Historial():
    from Helpers import verificacion_seguimiento
    with open ("Historial_Restaurante.txt", "r") as HR:
        Lista = HR.readlines()
        Telefono = input("\nIngresa el numero telefonico de la persona: ")
        if verificacion_seguimiento(Telefono):
            return
        print("\n")
        for i in Lista:
            Caracteristicas = i.split(" / ")
            for x in Caracteristicas:
                no_importante, importante = x.split(": ")
                if importante == Telefono:
                    print(i, end="")
                    return