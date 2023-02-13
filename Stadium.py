class Stadium:
    def __init__(self, name, location, dni):
        self.name = name
        self.location = location
        self.dni = dni
    def show_stadium(self):
        '''La función muestra los estadios de fútbol'''
        return f"""
        Nombre: {self.name}
        Ubicación: {self.location}
        ID: {self.dni}
        """