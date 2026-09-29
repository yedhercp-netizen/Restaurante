from Alta_Reservacion import alta
from Historial_Clientes import Historial
from Precio_Cena import Menu
from Horario_Restaurante import horarios
with open("Historial_Restaurante.txt", "a"):
    pass
while True:
    print("\nBienvenido a la pagina del Restaurante Peru Lindo")
    print("""Por favor ingrese alguna de los siguientes numeros
1. Crear Cuenta
2. Recervar
3. Cena
4. Historial de Clientes
5. Salir""")
    accion = input("Ingrese por favor al guno de los numero anterior mente mostrados: ")
    if accion.isnumeric():
        if int(accion) == 1:
            alta()
        elif int(accion) == 2:
            horarios()
        elif int(accion) == 3:
            Menu()
        elif int(accion) == 4:
            Historial()
        elif int(accion) == 5:
            pass
        else:
            print("Esa opcion no es pocible")
    else:
        print("Solo se puede ingresar numeros")