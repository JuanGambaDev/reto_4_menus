import venta as ven
import empleado as emp
import producto as prod
import cliente as client
import os

def mostrar_menu_principal():
    os.system('clear')
    print("---------------------------------------------")
    print("               Market Cicle                  ")
    print("---------------------------------------------")
    print("[1]Agregar producto.")
    print("[2]Agregar empleado.")
    print("[3]Agregar cliente.")
    print("[4]Registrar venta.")
    print("[5]Salir.")
    print("")
    opcion = input("*Selecciona su opción: ")
    if opcion == "1":
        prod.mostrar_menu_producto()
    elif opcion == "2":
        emp.mostrar_menu_empleado()
    elif opcion == "3":
        client.mostrar_menu_cliente()
    elif opcion == "4":
        ven.iniciar_venta()
    elif opcion == "5":
        print("--> Fin")
        print("")
        # Salir de la aplicación
        exit()

def init ():
    mostrar_menu_principal()

    
if __name__ == "__main__":
    init()