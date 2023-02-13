class ResFacture:
    def __init__(self, name, dni, restaurant, products, subtotal, discount, iva, total):
        self.name = name
        self.dni = dni
        self.restaurant = restaurant
        self.products = products
        self.subtotal = subtotal
        self.discount = discount
        self.iva = iva
        self.total = total
    def show_res_facture(self):
        '''La función muestra la factura generada en la compra'''
        return f"""
        -------------------------------------
        |  ****FACTURA DEL RESTAURANTE****  |
        -------------------------------------   
        |Nombre: {self.name}                
        |Cédula: {self.dni}                 
        |Restaurante: {self.restaurant} 
        |Productos comprados: {self.products}                  
        |Subtotal= {self.subtotal}$         
        |Descuento= {self.discount}$        
        |IVA= {self.iva}%                   
        ------------------------------------- 
        |TOTAL A PAGAR= {self.total}        
        -------------------------------------
        """