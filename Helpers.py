def Verificacion_Existencia(Variable):
    with open("Historial_Restaurante.txt", "r") as AC:
        Archivo = AC.readlines()
        for i in Archivo:
            if Variable in i:
                return True
        print("No se a encontrado la reservacion")
        return False

def verificacion_seguimiento(variable: str):
    import string
    import time
    def salir(variable):
        if "BACK" in variable:
            return True
        return False
    
    if not variable.strip():
        print("No se puede dejar el espacio basio")
        time.sleep(1)
        print("\033[1A\033[2K",end="")
        for i in range(1,4):
            print("Regresando" + ("." * i))
            time.sleep(0.5)
            print("\033[1A\033[2K",end="")
        return True

    if any(i in string.punctuation for i in variable):
        print("No se puede agregar simbolos")
        time.sleep(1)
        print("\033[1A\033[2K",end="")
        for i in range(1,4):
            print("Regresando" + ("." * i))
            time.sleep(0.5)
            print("\033[1A\033[2K",end="")
        return True

    if salir(variable):
        print("Saliendo al menu inicial")
        time.sleep(1)
        print("\033[1A\033[2K",end="")
        for i in range(1,4):
            print("Regresando" + ("." * i))
            time.sleep(0.5)
            print("\033[1A\033[2K",end="")
        return True
    return False

def Verificacion_Cuenta_Cancelada(Variable: str):
    with open("Historial_Restaurante.txt", "r") as HR:
        lineas = HR.readlines()
        for i in lineas:
            if Variable.split() == i.split():
                i.strip(" / ")
                for x in i:
                    no_importante, importante = x.strip()
                    if importante.split() == "Desactiva":
                        print("Esta reservacion ya esta desactivada")
                        return False
                return True