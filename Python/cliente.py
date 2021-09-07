import main as m
import os

clientes = []

def mostrar_menu_cliente():
    os.system('clear')
    print("---------------------------------------------")
    print("             Agregar cliente                 ")
    print("---------------------------------------------")
    print("[1]Agregar")
    print("[2]Listar")
    print("[3]Consultar")
    print("[4]Actualizar")
    print("[5]Eliminar")
    print("[6]Volver al menú princiapl")
    print("")
    opcion = input("*Selecciona su opción: ")
    if opcion == "1":
        agregar()
    elif opcion == "2":
        listar()
    elif opcion == "3":
        consultar()
    elif opcion == "4":
        actualizar()
    elif opcion == "5":
        eliminar()
    elif opcion == "6":
        m.mostrar_menu_principal()

def agregar():
    os.system('clear')
    inventario = False
    while inventario == False:
        code = int(input("--> Digite el DNI del cliente que desea registrar: "))
        nombre_cliente = input("--> Digite el nombre del cliente que desea registrar: ")
        cliente = [code, nombre_cliente]
        clientes.append(cliente)
        if cliente in clientes:
            inventario = True
            print("* --> Cliente registrado de forma exitosa!")
            opc = input("¿Desea realizar un nuevo registro? [y]Si [n]No: ")
            if opc == "y":
                inventario = False
            else:
                mostrar_menu_cliente()
        else:
            print("Error en registro. Por favor intente de nuevo")

def listar():
    os.system('clear')
    print("Los clientes registrados en el sistema son:","\n",clientes)
    opc = input("presione [e] para volver al menú: ")
    if opc == "e":
        mostrar_menu_cliente()

def consultar():
    os.system('clear')
    encontrado = False
    while encontrado == False:
        codigo = int(input("Ingrese el DNI del cliente que desea buscar (Oprima 0 para salir): "))
        if codigo != 0:
            for cliente in clientes:
                code, nombre = cliente
                if codigo == code:
                    encontrado = True
                    print("el cliente asignado con ese DNI es: ", cliente)
                    opc = input("¿Desea realizar una nueva consulta? [y]Si [n]No: ")
                    if opc == "y":
                        encontrado = False
                    else:
                        mostrar_menu_cliente()    
        else:
            mostrar_menu_cliente()


def actualizar():
    modificado = False
    while modificado == False:
        code = int(input("Ingrese el DNI del cliente que desea modificar (Oprima 0 para salir): "))
        if code != 0:
            for cliente in clientes: 
                codigo, nombre = cliente
                if code == codigo:
                    print("El cliente a modificar es: ", cliente)
                    n_codigo = int(input("Ingrese DNI del nuevo cliente: "))
                    n_nombre = input("Ingrese nombre del nuevo cliente: ")
                    clientes[clientes.index(cliente)] = [n_codigo, n_nombre]
                    modificado = True
                    print("La lista de clientes ha sido actualizada: ",clientes)
                    opc = input("¿Desea realizar un nuevo cambio? [y]Si [n]No: ")
                    if opc == "y":
                        modificado = False
                    else:
                        mostrar_menu_cliente()
        else:
            mostrar_menu_cliente()

def eliminar():
    os.system('clear')
    encontrado = False
    while encontrado == False:
        codigo = int(input("Ingrese DNI del cliente que desea eliminar (Oprima 0 para salir): "))
        if codigo != 0:
            for cliente in clientes:
                code, nombre = cliente
                if codigo == code:
                    encontrado = True
                    print("El cliente asignado con ese DNI es:","\n",cliente)
                    eliminar = input("¿Desea eliminarlo? [y]Si [n]No para salir: ")
                    if eliminar == "y":
                        clientes.pop(clientes.index(cliente))
                        print("La lista de clientes ahora es: ", clientes)
                        opc = input("¿Desea eliminar otro cliente de la lista? [y]Si [n]No: ")
                        if opc == "y":
                            encontrado = False
                        else:
                            mostrar_menu_cliente()
                    else:
                        mostrar_menu_cliente()
        else:
            mostrar_menu_cliente()