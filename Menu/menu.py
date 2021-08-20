from Inputs.entrada import *

class Menu:
    def __init__(self):
        self.objEntrada = Ingreso()

    def myop(self, lista):
        #Imprimir menu
        for i in range(len(lista)):
            print(str(i+1)+".- "+lista[i])
        op = -1
        while op < 1 or op > len(lista):
            op = self.objEntrada.numero_Int("Ingrese una opcion: ")
            if op < 1 or op > len(lista):
                print("Error, la opcion ingresada no es valida\n")
        return op


