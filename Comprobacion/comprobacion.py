from  Inputs.entrada import *


class Check:
    def __init__(self):
        self.objE = Ingreso()

    def Cedula10(self):
        booleano = False
        while booleano == False:
            ced = input("Cedula: ")
            if len(ced) == 10:
                booleano = True #OJO
                break
            elif len(ced) != 10:
                print("Error, la cedula debe tener 10 digitos\n")
        return ced

    def Telefono10(self):
        booleano = False
        while booleano == False:
            telf =  input("Telefono: ")
            if len(telf) == 10:
                booleano = True #OJO
                break
            elif len(telf) != 10:
                print("Error, el numero de telefono debe tener 10 digitos\n")
        return telf

    def check_Cod(self, cod, lista):
        obj = None
        for i in range(len(lista)):
            if cod == lista[i].cod:
                obj = lista[i]
                break
        return obj

    def check_Cantidad(self, i, obj):
        booleano = False
        while booleano == False:
            cantidad_comprar = self.objE.numero_Int("Cantidad " + "item " + str(i + 1) + ": ")
            if cantidad_comprar > 0 and cantidad_comprar <= obj.cantidad:
                booleano == True #OJO
                break
            else:
                print("No hay tal cantidad en el stock, intentelo de nuevo\n")
        return cantidad_comprar








