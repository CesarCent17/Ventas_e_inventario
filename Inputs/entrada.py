class Ingreso:
    def numero_Int(self, msg):
        while True:
            try:
                n = int(input(msg))
                break
            except ValueError:
                print("Error, debe ingresar un numero entero\n")
        return n

    def numero_Float(self, msg):
        while True:
            try:
                n = float(input(msg))
                break
            except ValueError:
                print("Error, debe ingresar un numero flotante\n")
        return n




