import main as m
import os

empleados = []

def mostrar_menu_empleado():
    os.system('clear')
    print("---------------------------------------------")
    print("             Agregar empleado                ")
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
        code = int(input("--> Digite el DNI del empleado que desea registrar: "))
        nombre_empleado = input("--> Digite el nombre del empleado que desea registrar: ")
        empleado = [code, nombre_empleado]
        empleados.append(empleado)
        if empleado in empleados:
            inventario = True
            print("Empleado registrado de forma exitosa!")
            opc = input("¿Desea realizar un nuevo registro? [y]Si [n]No: ")
            if opc == "y":
                inventario = False
            else:
                mostrar_menu_empleado()
        else:
            print("Error en registro. Por favor intente de nuevo")

def listar():
    os.system('clear')
    print("Los empleados registrados en el sistema son:","\n",empleados)
    opc = input("presione [e] para volver al menú: ")
    if opc == "e":
        mostrar_menu_empleado()

def consultar():
    os.system('clear')
    encontrado = False
    while encontrado == False:
        codigo = int(input("Ingrese el DNI del empleado que desea buscar (Oprima 0 para salir): "))
        if codigo != 0:
            for empleado in empleados:
                code, nombre = empleado
                if codigo == code:
                    encontrado = True
                    print("el empleado asignado con ese DNI es: ", empleado)
                    opc = input("¿Desea realizar una nueva consulta? [y]Si [n]No: ")
                    if opc == "y":
                        encontrado = False
                    else:
                        mostrar_menu_empleado()    
        else:
            mostrar_menu_empleado()


def actualizar():
    modificado = False
    while modificado == False:
        code = int(input("Ingrese el DNI del empleado que desea modificar (Oprima 0 para salir): "))
        if code != 0:
            for empleado in empleados: 
                codigo, nombre = empleado
                if code == codigo:
                    print("El empleado a modificar es: ", empleado)
                    n_codigo = int(input("Ingrese DNI del nuevo empleado: "))
                    n_nombre = input("Ingrese nombre del nuevo empleado: ")
                    empleados[empleados.index(empleado)] = [n_codigo, n_nombre]
                    modificado = True
                    print("La lista de empleados ha sido actualizada: ",empleados)
                    opc = input("¿Desea realizar un nuevo cambio? [y]Si [n]No: ")
                    if opc == "y":
                        modificado = False
                    else:
                        mostrar_menu_empleado() 
        else:
            mostrar_menu_empleado()

def eliminar():
    os.system('clear')
    encontrado = False
    while encontrado == False:
        codigo = int(input("Ingrese DNI del empleado que desea eliminar (Oprima 0 para salir): "))
        if codigo != 0:
            for empleado in empleados:
                code, nombre = empleado
                if codigo == code:
                    encontrado = True
                    print("el empleado asignado con ese DNI es:","\n",empleado)
                    eliminar = input("¿Desea eliminarlo? [y]Si [n]No para salir: ")
                    if eliminar == "y":
                        empleados.pop(empleados.index(empleado))
                        print("La lista de empleados ahora es: ", empleados)
                        opc = input("¿Desea eliminar otro empleado de la lista? [y]Si [n]No: ")
                        if opc == "y":
                            encontrado = False
                        else:
                            mostrar_menu_empleado()
                    else:
                        mostrar_menu_empleado()
        else:
            mostrar_menu_empleado()
