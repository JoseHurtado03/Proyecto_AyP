class Restaurant:
    def __init__(self, name, stadium_id, products):
        self.name = name
        self.stadium_id = stadium_id
        self.products = products
    def show_restaurant(self):
        '''La función muestra los restaurantes'''
        return f"""
        Nombre del Restaurante: {self.name}
        Productos: {self.products}
        """