import main as m
import os

def imprimir_titulo():
    print("                                                 ")
    print("             ----------------------------------- ")
    print("            | # Sistema de registro de ventas # |")
    print("            |      *** Market cicle ***         |")
    print("             ----------------------------------- ")
    print("                                                 ")

def registrar_venta():
    print("--------------------------------------------------------------------------------------------")
    print("|                                   Registro de venta                                      |")
    print("--------------------------------------------------------------------------------------------")
    print(" ")
    fecha = input("Fecha de venta (dd/mm/aaaa): ")
    nombre_cliente = input("Nombre del cliente: ")
    id_cliente = input("Identificacion (Cliente): ")

    marca = input("Marca de la bicicleta (Specialized [1] Treck [2] BMC [3]): ")
    if marca == "1":
        marca = "Specialized"
    elif marca == "2":
        marca = "Treck"
    elif marca == "3":
        marca = "BMC" 
    else:
        print("Opcion no valida") 

    color = input("Color de la bicicleta (Roja [1] Negra [2] Roja-Negra [3]): ")
    if color == "1":
        color = "Specialized"
    elif color == "2":
        color = "Treck"
    elif color == "3":
        color = "BMC" 
    else:
        print("Opcion no valida")

    tipo = input("Tipo de bicicleta (Nacional [1] Importada [2]): ")
    if tipo == "1":
        tipo = "Nacional"
    elif tipo == "2":
        tipo = "Importada"
    else:
        print("valor no valido")

    precio_unitario = int(input("Precio Unitario: "))
    cantidad = int(input("Cantidad de bicicletas vendidas: "))
    iva = int(input("IVA (20% nacionales y 30% para importadas): "))

    return fecha, nombre_cliente, id_cliente, marca, color, tipo, precio_unitario, cantidad, iva

def verificar_codigo(codigo):
    if len(codigo) == 8 and codigo[2] == "*" and codigo[0] == codigo[7] and codigo.find("@") == -1 and codigo.find("&") == -1 and codigo.find("+") == -1 and codigo.find("=") == -1 :
        pass
    else:
        print("Error: Codigo invalido. No se puede realizar registro de venta, Intente nuevamente.")

def calcular_valor_total(pu,can): 
    valor_total = pu * can 
    return valor_total

def calcular_iva(vt,iv):
    valor_iva = vt * iv / 100
    return valor_iva


def imprimir_factura(f,c,i,m,pu,can,vt,vi):
    print("--------------------------------------------------------------------------------------------")
    print("|                               Factura de venta - Cliente                                 |")
    print("--------------------------------------------------------------------------------------------")
    print("|Cliente : ",c,"                                                                           |")
    print("|Identificación : ",i,"                                                                    |")
    print("--------------------------------------------------------------------------------------------")
    print("| Fecha  | Marca   | Valor unitario | Cantidad  | Valor total  | Valor IVA | Total a pagar |")
    print("--------------------------------------------------------------------------------------------")
    print("|", f, " |", m, "  |", pu, "  |", can, "  |", vt, "  |", vi,"  |", vt,"  |")
    print("--------------------------------------------------------------------------------------------")
    print(" ")

def calcular_bonificacion(vt):
    # Bonificacticon tipo A
    if vt >= 200000 and vt < 800000:
        bonificacion = vt * 5 / 100
    # Bonificacticon tipo B
    elif vt >= 800000 and vt < 1500000:
        bonificacion = vt * 10 / 10
    # Bonificacticon tipo C
    elif vt >= 1500000:
        bonificacion = vt * 15 / 100
    # No hay bonificacion
    else:
        bonificacion = "No hay comision"
    return bonificacion      

def imprimir_bonificacion(cv,nv,m,can,f,vt,com):
    print(" ")
    print("--------------------------------------------------------------------------------------------")
    print("|                               Bonificación - Vendedor                                    |")
    print("--------------------------------------------------------------------------------------------")
    print("| Codigo  | Vendedor   | Marca | Cantidad  | fecha de venta | Valor venta | valor comision |")
    print("--------------------------------------------------------------------------------------------")
    print("|", cv, " |", nv, " |", m, " |", can, "  |", f, " |", vt,"  |", com,"  |")
    print("--------------------------------------------------------------------------------------------")

def iniciar_venta():
    os.system('clear')
    registro = False
    while registro == False:
        imprimir_titulo()
        nombre_vendedor = input("Ingrese nombre del vendedor: ")
        codigo_vendedor = input("Ingrese codigo de vendedor: ")
        verificar_codigo(codigo_vendedor)
        fech, cliente, identificacion, marc, col, tip, precio_u, cant, impuest = registrar_venta()
        valor_t = calcular_valor_total(precio_u, cant)
        valor_impuesto = calcular_iva(valor_t, impuest)
        imprimir_factura(fech, cliente, identificacion, marc, precio_u, cant, valor_t, valor_impuesto)
        valor_comision = calcular_bonificacion(valor_t)
        imprimir_bonificacion(codigo_vendedor , nombre_vendedor, marc, cant, fech, valor_t, valor_comision)
        opc = input("Desea realizar un nuevo registro? [y]Si [n]No : ")
        if opc != "y":
            registro = True
            m.mostrar_menu_principal()




