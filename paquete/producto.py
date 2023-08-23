class Producto:
    def __init__(self, nombre, tienda, precio, cantidad):
        self.nombre = nombre
        self.tienda = tienda.title()
        self.precio = precio
        self.cantidad = cantidad
        
    def __str__(self):
        return f"{self.nombre} ({self.cantidad}) en {self.tienda} por ${self.precio} c/u"