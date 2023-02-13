from Product import Product
class Beverage(Product):
    def __init__(self, name, quantity, price, type_product, additional):
        super().__init__(name, quantity, price, type_product)
        self.additional = additional
    def show_product(self):
        '''La función muestra los productos registrados como bebida'''
        return f"""
        Nombre: {self.name}
        Precio: {self.price}
        Tipo: {self.type_product}
        Adicional: {self.additional}
        """