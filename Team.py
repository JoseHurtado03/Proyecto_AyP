class Team:
    def __init__(self, name, fifa_code, group):
        self.name = name
        self.fifa_code = fifa_code
        self.group = group
    def show_team(self):
        '''La función muestra los equipos de fútbol'''
        return f"""
        Nombre (País): {self.name}
        Código FIFA: {self.fifa_code}
        Grupo: {self.group}
        """