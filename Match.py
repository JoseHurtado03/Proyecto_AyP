class Match:
    def __init__(self, home_team, away_team, date, stadium_id, match_id):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.stadium_id = stadium_id
        self.match_id = match_id
    def show_match(self):
        '''La función muestra los partidos'''
        return f"""
        Equipo Local: {self.home_team}
        Equipo Visitante: {self.away_team}
        Fecha: {self.date}
        ID del Estadio: {self.stadium_id}
        ID del Partido: {self.match_id}
        """