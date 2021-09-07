import main as m
import os

productos = []

def mostrar_menu_producto():
    os.system('clear')
    print("---------------------------------------------")
    print("             Agregar Producto                ")
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
        agregar_producto()
    elif opcion == "2":
        listar_producto()
    elif opcion == "3":
        consultar_producto()
    elif opcion == "4":
        actualizar_producto()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        m.mostrar_menu_principal()

def agregar_producto():
    os.system('clear')
    inventario = False
    while inventario == False:
        code = int(input("--> Digite el codigo del producto que desea registrar: "))
        nombre_producto = input("--> Digite el nombre del producto que desea registrar: ")
        producto = [code, nombre_producto]
        productos.append(producto)
        if producto in productos:
            inventario = True
            print("Producto registrado de forma exitosa!")
            opc = input("¿Desea realizar un nuevo registro? [y]Si [n]No: ")
            if opc == "y":
                inventario = False
            else:
                mostrar_menu_producto()
        else:
            print("Error en registro. Por favor intente de nuevo")

def listar_producto():
    os.system('clear')
    print("Los productos registrados en el sistema son:\n",productos)
    opc = input("presione [e] para volver al menú: ")
    if opc == "e":
        mostrar_menu_producto()

def consultar_producto():
    os.system('clear')
    encontrado = False
    while encontrado == False:
        codigo = int(input("Ingrese codigo del producto que desea buscar (Oprima 0 para salir): "))
        if codigo != 0:
            for producto in productos:
                code, nombre = producto
                if codigo == code:
                    encontrado = True
                    print("el producto asignado con ese codigo es: ", producto)
                    opc = input("¿Desea realizar una nueva consulta? [y]Si [n]No: ")
                    if opc == "y":
                        encontrado = False
                    else:
                        mostrar_menu_producto()    
        else:
            mostrar_menu_producto()


def actualizar_producto():
    modificado = False
    while modificado == False:
        code = int(input("Ingrese codigo del producto que desea modificar (Oprima 0 para salir): "))
        if code != 0:
            for producto in productos: 
                codigo, nombre = producto
                if code == codigo:
                    print("El producto a modificar es: ", producto)
                    n_codigo = int(input("Ingrese codigo del nuevo producto: "))
                    n_nombre = input("Ingrese nombre del nuevo producto: ")
                    productos[productos.index(producto)] = [n_codigo, n_nombre]
                    modificado = True
                    print("La lista de productos ha sido actualizada: ",productos)
                    opc = input("¿Desea realizar un nuevo cambio? [y]Si [n]No: ")
                    if opc == "y":
                        modificado = False
                    else:
                        mostrar_menu_producto() 
        else:
            mostrar_menu_producto()

def eliminar_producto():
    os.system('clear')
    encontrado = False
    while encontrado == False:
        codigo = int(input("Ingrese codigo del producto que desea eliminar (Oprima 0 para salir): "))
        if codigo != 0:
            for producto in productos:
                code, nombre = producto
                if codigo == code:
                    encontrado = True
                    print("el producto asignado con ese codigo es:","\n",producto)
                    eliminar = input("¿Desea eliminarlo? [y]Si [n]No para salir: ")
                    if eliminar == "y":
                        productos.pop(productos.index(producto))
                        print("La lista de productos ahora es: ", productos)
                        opc = input("¿Desea eliminar otro producto de la lista? [y]Si [n]No: ")
                        if opc == "y":
                            encontrado = False
                        else:
                            mostrar_menu_producto()
                    else:
                        mostrar_menu_producto()
        else:
            mostrar_menu_producto()

