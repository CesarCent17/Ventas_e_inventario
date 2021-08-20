from Inputs.entrada import *
from Entidades.entidades import *
from Comprobacion.comprobacion import *
from Menu.menu import *
from Archivo.archivo import *

class Core:
    def __init__(self):
        self.objEntrada = Ingreso()
        self.objComprobar = Check()
        self.objMenu = Menu()
        self.objArc = Archivo()

    def main(self):
        print("\t\t Sistema de control de ventas e inventario")
        opciones = ["Bodega", "Ventas", "Salir"]
        op = self.objMenu.myop(opciones)

        if op == 1:
            self.menuBodega()

        elif op == 2:
            self.menuVenta()


        elif op == 3:
            print("Gracias por su preferencia tenga un buen dia!")

    #MENU BODEGA - PRINCIPAL
    def menuBodega(self):
        print("\n")
        print("\t\t Bodega")
        opciones = ["Consultar stock", "Kardex", "Registro de producto", "Adicionar cantidad a registro", "Atras"]
        op = self.objMenu.myop(opciones)
        if op == 1:
            self.consultarstock()
            self.menuBodega()
        elif op == 2:
            self.Kardex()
            self.menuBodega()
        elif op == 3:
            self.registro_de_producto()
            self.menuBodega()
        elif op == 4:
            self.adiccion_Cantidad()
            self.menuBodega()
        elif op == 5:
            print("\n")
            self.main()

    #OPCION 1
    def consultarstock(self):
        print("\n")
        print("Consulta stock")
        cod = input("Codigo: ")
        self.listaproductos = self.objArc.getDatos_Producto("Productos.txt")
        obj = self.objComprobar.check_Cod(cod, self.listaproductos)
        if obj != None:
            print(f"Producto = {obj.marca} {obj.descripcion}\n"
                  f"Cantidad = {obj.cantidad}\n")
        elif obj == None:
            print("\n")
            print("Error, El codigo que ingreso no coincide con los registros")
            print("Ayuda: puede obtener el codigo del producto al momento de observar el kardex")

    #OPCION 2
    def Kardex(self):
        print("\n")
        print("\t\t Kardex")
        self.listaproductos = self.objArc.getDatos_Producto("Productos.txt")
        for i in range(len(self.listaproductos)):
            print(self.listaproductos[i].getDatos())

    #OPCION 3
    def registro_de_producto(self):
        self.listaproductos = self.objArc.getDatos_Producto("Productos.txt")
        print("\n")
        print("\t\t Registro de producto")
        print("Nota: El codigo del producto es un identificador unico")
        cod = input("Codigo: ")
        obj = self.objComprobar.check_Cod(cod, self.listaproductos)
        if obj != None:
            print("Este producto ya existe!")
        elif obj == None:
            marca = input("Marca: ")
            descripcion = input("Descripcion: ")
            precio_unitario = self.objEntrada.numero_Float("Precio unitario: ")
            cantidad = self.objEntrada.numero_Int("Cantidad: ")
            obj_Producto = Producto(cod, marca, descripcion, precio_unitario, cantidad)
            msg = obj_Producto.cod + ";" + obj_Producto.marca + ";" + obj_Producto.descripcion + ";" + str(obj_Producto.precio_unitario) + ";" + str(obj_Producto.cantidad)+";\n"
            self.objArc.create_file("Productos.txt", msg, "a")
            print("Registro de producto ingresado con exito!\n")

    #OPCION 4
    def adiccion_Cantidad(self):
        #Mostrar items
        listacod = []
        listamarcas = []
        listacantidades = []
        print("\n")
        print("\t\tSeleccione un item")
        print("Nota: en esta opcion se adicionara un nuevo valor a la cantidad actual en stock\n")
        self.listaproductos = self.objArc.getDatos_Producto("Productos.txt")

        for i in range(len(self.listaproductos)):
            codigo = (self.listaproductos[i].cod)
            marca = (self.listaproductos[i].marca)
            cantidad = (self.listaproductos[i].cantidad)
            listacod.append(codigo)
            listamarcas.append(marca)
            listacantidades.append(cantidad)

        for i in range(len(listacod)):
            print(f"Codigo = {listacod[i]}\n"
                  f"Marca = {listamarcas[i]}\n"
                  f"Cantidad actual = {listacantidades[i]}\n")

        #Elegir item
        cod = input("Codigo: ")
        obj = self.objComprobar.check_Cod(cod, self.listaproductos)
        if obj == None:
            print("El producto no existe")
        elif obj != None:
            print("\n")
            print("\t\tAdicionar nueva cantidad al item")
            agregar = self.objEntrada.numero_Int("Adicionar nueva cantidad: ")
            print(f"Cantidad actual = {obj.cantidad}")
            print(f"Cantidad por adicionar = {agregar}")
            obj.cantidad += agregar
            print(f"Nueva cantidad total = {obj.cantidad}")
            msg = ""
            for i in range(len(self.listaproductos)):
                msg = msg + self.listaproductos[i].cod + ";" + self.listaproductos[i].marca + ";" + self.listaproductos[i].descripcion + ";" + \
                      str(self.listaproductos[i].precio_unitario) + ";" + str(self.listaproductos[i].cantidad)+";\n"
            self.objArc.create_file("Productos.txt", msg, "w")
            print("Los datos se han actualizado correctamente!")

    #MENU VENTAS - PRINCIPAL
    def menuVenta(self):
        print("\n")
        print("\t\t Menu de ventas")
        opciones = ["Realizar venta", "Consulta clientes",  "Atras"]
        op = self.objMenu.myop(opciones)

        if op == 1:
            self.realizar_Venta()


        elif op == 2:
            self.consultaclientes()
            self.menuVenta()

        elif op == 3:
            print("\n")
            self.main()
    def realizar_Venta(self):
        #IMPRIMIR ITEMS
        print("\n")
        print("\t\t Items")
        self.listaproductos = self.objArc.getDatos_Producto("Productos.txt")
        for i in range(len(self.listaproductos)):
            print(self.listaproductos[i].getDatos())
        print(f"Existen {len(self.listaproductos)} items")
        print("Ayuda: entre todos los productos disponibles seleccione cuantos items desea elegir para llevar al carrito")
        print("Nota: se aplicara un descuento del 15% por la compra de 10 productos que contengan el mismo codigo\n")
        print("\t\t Ventas al por mayor y menor")

        #ELEGIR CANTIDAD DE ITEMS
        cantidad_items_eleccion = self.objEntrada.numero_Int("Cantidad de items: ")

        #COMPROBACION DE CANTIDAD ELEGIDA DE ITEMS

        #CANTIDAD ERRONEA -  REGRESA AL MENU
        if cantidad_items_eleccion > len(self.listaproductos) or cantidad_items_eleccion <= 0:
            print("La cantidad de items elegida esta fuera de rango")
            self.menuVenta()

        elif cantidad_items_eleccion > 0 and cantidad_items_eleccion <= len(self.listaproductos):
            listacarrito, listacantidadcomprar = self.recoger_listas(cantidad_items_eleccion)

            if len(listacarrito) > 0:
                print("\n")
                print("Su carrito contiene: ")
                for i in range(len(listacarrito)):
                    print("Producto: "+listacarrito[i].cod+" Cantidad: " +str(listacantidadcomprar[i]))
                obj = self.menu_crear_Cliente()
                if obj == None:
                    self.menuVenta()
                elif obj != None:
                    self.crear_Factura(obj, listacarrito, listacantidadcomprar)
                    self.main()
            elif len(listacarrito) == 0:
                self.menuVenta()
    def recoger_listas(self, cantidad):
        listacarrito = []
        listacantidadcomprar = []

        for i in range(cantidad):
            cod = input("Codigo " + "item " + str(i + 1) + ": ")
            obj = self.objComprobar.check_Cod(cod, self.listaproductos)

            if obj == None:
                print("Error, el codigo ingresado no coincide con los registros")
                break

            #BUG
            elif obj != None:
                if obj.cantidad > 0:
                    cantidad_comprar = self.objComprobar.check_Cantidad(i, obj)
                    listacarrito.append(obj)
                    listacantidadcomprar.append(cantidad_comprar)

                elif obj.cantidad == 0:
                    print("Actualmente no hay disponibilidad del producto")
                    break

        return listacarrito, listacantidadcomprar

    #Crear al cliente
    def menu_crear_Cliente(self):
        print("\n")
        print("\t\t Menu de registro de cliente")
        op = ["Datos personales", "Consumidor final", "Cancelar Compra"]
        op = self.objMenu.myop(op)
        if op == 1:
            obj = self.clientes_Datos_Personales()
        elif op == 2:
            obj = self.cliente_Consumidor_Final()
        elif op == 3:
            print("Se canceló la compra!")
            obj = None
        return obj
    def clientes_Datos_Personales(self):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = self.objComprobar.Cedula10() #BUCLE
        telefono = self.objComprobar.Telefono10() #BUCLE
        self.listaclientes = self.objArc.getDatos_Cliente("Clientes.txt")
        obj = Cliente(nombre, apellido, cedula, telefono)

        # Lo agrego a la lista de clientes
        self.listaclientes.append(obj)

        #Lo agrego al archivo
        msg = obj.nombre+";"+obj.apellido+";"+obj.cedula+";"+obj.telefono+";\n"
        self.objArc.create_file("Clientes.txt", msg, "a")
        print("Cliente registrado exitosamente!\n")
        return obj
    def cliente_Consumidor_Final(self):
        nombre = "Consumidor"
        apellido = "final"
        cedula = "----------"
        telefono = "----------"
        self.listaclientes = self.objArc.getDatos_Cliente("Clientes.txt")
        obj = Cliente(nombre, apellido, cedula, telefono)

        # Lo agrego a la lista de clientes
        self.listaclientes.append(obj)

        # Lo agrego al archivo
        msg = obj.nombre + ";" + obj.apellido + ";" + obj.cedula + ";" + obj.telefono + ";\n"
        self.objArc.create_file("Clientes.txt", msg, "a")
        print("Cliente registrado exitosamente!\n")
        return obj

    #Crear factura y pagar
    def crear_Factura(self, cliente_obj, carrito, cantidad_comprar):
        cliente = cliente_obj.nombre+" "+cliente_obj.apellido
        cedula = cliente_obj.cedula
        telefono = cliente_obj.telefono
        self.listafacturas = self.objArc.getDatos_Facturas("Facturas.txt")
        obj = Factura(cliente, cedula, telefono)
        self.listafacturas.append(obj)
        msg = obj.cliente + ";" + obj.cedula + ";" + obj.telefono + ";\n"
        self.objArc.create_file("Facturas.txt", msg, "a")
        #PRESENTACION DE FACTURA
        print("########## FACTURA ##########")
        print(f"Cliente: {cliente}\n"
              f"Cedula: {cedula}\n"
              f"Telefono: {telefono}\n")

        print("#############################")

        #IMPRIMIR PRODUCTOS
        for i in range(len(carrito)):
            print(f"\nPRODUCTO ITEM #{i+1}: {carrito[i].marca} {carrito[i].descripcion}\n"
                  f"Cantidad: {cantidad_comprar[i]}\n"
                  f"Precio unitario: ${carrito[i].precio_unitario:.2f}\n"
                  f"Precio total: ${carrito[i].precio_unitario*cantidad_comprar[i]:.2f}\n")

        descuento_total, subtotal = self.valor_desc_subtotal(carrito, cantidad_comprar)
        valor_a_pagar = subtotal-descuento_total
        print("#############################")
        print(f"Subtotal: ${subtotal:.2f}\n"
              f"Descuento: ${descuento_total:.2f}\n"
              f"Valor a pagar: ${valor_a_pagar:.2f}\n")
        input("Presione <Enter> para continuar")

        for i in range(len(carrito)):
            carrito[i].cantidad -= cantidad_comprar[i]
            msg = ""
            for i in range(len(self.listaproductos)):
                msg = msg + self.listaproductos[i].cod+";"+self.listaproductos[i].marca+";"+\
                      self.listaproductos[i].descripcion+ ";"+str(self.listaproductos[i].precio_unitario)\
                      +";"+str(self.listaproductos[i].cantidad)+";\n"
            self.objArc.create_file("Productos.txt", msg, "w")
        print("Gracias tenga un buen dia!\n")
    def valor_desc_subtotal(self, listadeitems, cantidad_comprar):
        lista_descuento_total, lista_subtotal = self.recogerListas_desc(listadeitems, cantidad_comprar)
        descuento_total = 0
        for i in lista_descuento_total:
            descuento_total += i
        subtotal = 0
        for i in lista_subtotal:
            subtotal += i
        return descuento_total, subtotal
    def recogerListas_desc(self, listadeitems, cantidad_comprar):
        lista_descuento_total = []
        lista_subtotal = []
        for i in range(len(listadeitems)):
            if cantidad_comprar[i] >= 10:
                descuento15 = (listadeitems[i].precio_unitario * cantidad_comprar[i]) * 0.15
                #valortotal_itemdesc = (listadeitems[i].precio_unitario * cantidad_comprar[i]) - descuento15
                lista_descuento_total.append(descuento15)

        for i in range(len(listadeitems)):
            lista_subtotal.append(listadeitems[i].precio_unitario * cantidad_comprar[i])

        return lista_descuento_total, lista_subtotal

    #Consulta cliente
    def consultaclientes(self):
        print("\n")
        print("\t\t Consulta de clientes")
        listaclientes = self.objArc.getDatos_Cliente("Clientes.txt")
        for i in range(len(listaclientes)):
            print(listaclientes[i].getDatos())




























