import requests
from Team import Team
from Stadium import Stadium
from Match import Match
teams = []
stadiums = []
matches = []
class MatchesOrganizer:
    def register_team(url= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"):
        '''Desde la API, la función guarda los datos de todos los equipos de fútbol'''
        data = requests.get(url).json()
        for team in data:
            name = team["name"]
            fifa_code = team["fifa_code"]
            group = team["group"]
            current_team = Team(name, fifa_code, group)
            teams.append(current_team)
    def show_teams():
        ''''Muestra la información de todos los equipos, ordenándolos con un índice'''
        aux = 0
        for team in teams:
            print(f"       ****{aux + 1}****")
            print(Team.show_team(team))
            aux += 1
    def register_stadium(url= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"):
        '''Desde la API, la función guarda los datos de todos los estadios de fútbol'''
        data = requests.get(url).json()
        for stadium in data:
            name = stadium["name"]
            location = stadium["location"]
            dni = stadium["id"]
            current_stadium = Stadium(name, location, dni)
            stadiums.append(current_stadium)
    def show_stadiums():
        ''''Muestra la información de todos los estadios, ordenándolos con un índice'''
        aux = 0
        for stadium in stadiums:
            print(f"       ****{aux + 1}****")
            print(Stadium.show_stadium(stadium))
            aux += 1
    def register_matches(url= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"):
        '''Desde la API, la función guarda los datos de todos los partidos de fútbol'''
        data = requests.get(url).json()
        for match in data:
            home_team = match["home_team"]
            for team in teams:
                if home_team == team.name:
                    home_team_o = team
            away_team = match["away_team"]
            for team in teams:
                if away_team == team.name:
                    away_team_o = team
            date = match["date"]
            stadium_id = match["stadium_id"]
            for stadium in stadiums:
                if stadium_id == stadium.dni:
                    stadium_o = stadium
            match_id = match["id"]
            current_match = Match(home_team_o.name, away_team_o.name, date, stadium_o.dni, match_id)
            matches.append(current_match)
    def show_matches():
        ''''Muestra la información de todos los partidos, ordenándolos con un índice'''
        aux = 0
        for match in matches:
            print(f"       ****{aux + 1}****")
            print(Match.show_match(match))
            aux += 1
    def search_match_team():
        '''Permite buscar un partido a través de uno de los equipos que van a participar'''
        aux = 0
        while aux == 0:
            search_team = input("Ingresa el nombre del equipo: ")
            for match in matches:
                if search_team == match.home_team or search_team == match.away_team:
                    print(f"       ****{aux + 1}****")
                    print(Match.show_match(match))
                    aux += 1
    def search_match_stadium():
        '''Permite buscar un partido a través del estadio del partido'''
        aux = 0
        while aux == 0:
            search_stadium = int(input("Ingresa el ID del estadio: "))
            for match in matches:
                if search_stadium == match.stadium_id:
                    print(f"       ****{aux + 1}****")
                    print(Match.show_match(match))
                    aux += 1
    def search_match_date():
        '''Permite buscar un partido a través de la fecha en la que se realizará'''
        aux = 0
        while aux == 0:
            search_date = input("Ingrese la fecha del partido (MM/DD/AAAA): ")
            for match in matches:
                if search_date in match.date:
                    print(f"       ****{aux + 1}****")
                    print(Match.show_match(match))
                    aux += 1
    def search_match():
        '''Administra todos los tipos de búsqueda de un partido, mostrándo un menú para
        que el usuario decida de qué manera desea buscar el partido'''
        option_search = input("""
        1- Por equipo
        2- Por estadio
        3- Por fecha
        
        Ingrese la opción con la que desea buscar un partido: """)
        while not int(option_search) in range(1,4):
            option_search = input("¡ERROR! Ingrese la opción con la que desea buscar un partido: ")
        if option_search == "1":
            MatchesOrganizer.search_match_team()
        elif option_search == "2":
            MatchesOrganizer.show_stadiums()
            MatchesOrganizer.search_match_stadium()
        elif option_search == "3":
            MatchesOrganizer.search_match_date()
    def show_seats():
        '''Muestra los asientos en forma de matriz para que el cliente pueda seleccionar uno o varios'''
        dictionary = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H"
        }
        columnas = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for key, value in dictionary.items():
            print(value, "()"*((len(columnas))-1))
        print(*columnas)
    def found_stadium_id(game):
        '''Recibe el número ID de un partido de fútbol registrado y devuelve el
        ID del estadio en el que se juagará ese partido'''
        for match in matches:
            if game == match.match_id:
                sta_id = match.stadium_id
                return sta_id
    def pass_stadium():
        '''Permite pasar la lista de estadios a otro módulo'''
        return stadiums