from Entidades.entidades import *


class Archivo:
    #Crear archivo
    def create_file(self, nombre, cadena, modo):
        archivo = open(nombre, modo)
        archivo.write(cadena)
        archivo.close()

    #Retorna una lista de objetos tipo cliente
    def getDatos_Cliente(self, nombre):
        listaclientes = []
        archivo = open(nombre, "r")
        for linea in archivo.readlines():  # por cada linea haz
            tupla = linea.split(";")  # crea una tupla y separa los campos de la linea cuando veas ;

            obj = Cliente(tupla[0], tupla[1], tupla[2], tupla[3])
            listaclientes.append(obj)  # por cada vuelta guardamos el objeto en una lista
        return listaclientes

    #Retorna una lista de objetos tipo producto
    def getDatos_Producto(self, nombre):
        listaproductos = []
        archivo = open(nombre, "r")
        for linea in archivo.readlines():  # por cada linea haz
            tupla = linea.split(";")  # crea una tupla y separa los campos de la linea cuando veas ;

            obj = Producto(tupla[0], tupla[1], tupla[2], float(tupla[3]), int(tupla[4]))
            listaproductos.append(obj)  # por cada vuelta guardamos el objeto en una lista
        return listaproductos

    #Retorna una lista de facturas
    def getDatos_Facturas(self, nombre):
        listafacturas = []
        archivo = open(nombre, "r")
        for linea in archivo.readlines():  # por cada linea haz
            tupla = linea.split(";")  # crea una tupla y separa los campos de la linea cuando veas ;

            obj = Factura(tupla[0], tupla[1], tupla[2])
            listafacturas.append(obj)  # por cada vuelta guardamos el objeto en una lista
        return listafacturas


