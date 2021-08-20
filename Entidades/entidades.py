class Cliente:
    def __init__(self, nombre, apellido, cedula, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono

    def getDatos(self):
        datos = f"Cliente: {self.nombre} {self.apellido}\n" \
                f"Cedula: {self.cedula}\n" \
                f"Telefono: {self.telefono}\n"
        return datos

class Producto:
    def __init__(self, cod, marca, descripcion, precio_unitario, cantidad):
        self.cod = cod
        self.marca = marca
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def getDatos(self):
        datos = f"Codigo: {self.cod}\n" \
                f"Marca: {self.marca}\n" \
                f"Descripcion: {self.descripcion}\n" \
                f"Precio unitario: ${self.precio_unitario:.2f}\n" \
                f"Disponibilidad: {self.cantidad}\n"
        return datos


class Factura:
    def __init__(self, cliente, cedula, telefono):
        self.cliente = cliente
        self.cedula = cedula
        self.telefono = telefono
