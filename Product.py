class Product:
    def __init__(self, name, quantity, price, type_product):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.type_product = type_product
    def show_product(self):
        '''Muestra la información de un producto'''
        return f"""
        Nombre: {self.name}
        Cantidad: {self.quantity}
        Precio= {self.price}
        Tipo de Producto: {self.type_product}
        """