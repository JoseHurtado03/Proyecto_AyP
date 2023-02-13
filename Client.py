class Client:
    def __init__(self, name, dni, age, game, ticket_type, ticket_id, attendance):
        self.name = name
        self.dni = dni
        self.age = age
        self.game = game
        self.ticket_type = ticket_type
        self.ticket_id = ticket_id
        self.attendance = attendance
    def show_client(self):
        '''La función muestra los clientes'''
        return f"""
        Nombre: {self.name}
        Cédula: {self.dni}
        Edad: {self.age}
        Partido: {self.game}
        Tipo de ticket: {self.ticket_type}
        ID del ticket: {self.ticket_id}
        """