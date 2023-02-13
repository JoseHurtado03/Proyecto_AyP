class Facture:
    def __init__(self, ticket_id, name, dni, game, stadium_id, ticket_type, seat, subtotal, discount, iva, total):
        self.ticket_id = ticket_id
        self.name = name
        self.dni = dni
        self.game = game
        self.stadium_id = stadium_id
        self.ticket_type = ticket_type
        self.seat = seat
        self.subtotal = subtotal
        self.discount = discount
        self.iva = iva
        self.total = total
    def show_facture(self):
        '''La función muestra la factura generada en la compra de la entrada'''
        return f"""
        -------------------------------------
        |          ****FACTURA****          |
        -------------------------------------
        |ID del ticket: {self.ticket_id}    
        |Nombre: {self.name}                
        |Cédula: {self.dni}                 
        |ID del Partido: {self.game} 
        |ID del Estadio: {self.stadium_id}       
        |Tipo de ticket: {self.ticket_type} 
        |Asiento(s): {self.seat}            
        |Subtotal= {self.subtotal}$         
        |Descuento= {self.discount}$        
        |IVA= {self.iva}%                   
        ------------------------------------- 
        |TOTAL A PAGAR= {self.total}        
        -------------------------------------
        """