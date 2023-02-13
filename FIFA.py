from TicketShop import TicketShop
from MatchesOrganizer import MatchesOrganizer
from RestaurantInventory import RestaurantInventory
from StadiumRestaurant import StadiumRestaurant
class FIFA:
    def menu_principal():
        '''La función administra todas las funciones de los modulos del programa
        Además, muestra el menú principal del programa para que el usuario pueda
        moverse por el programa de manera intuitiva'''
        MatchesOrganizer.register_team()
        MatchesOrganizer.register_stadium()
        MatchesOrganizer.register_matches()
        RestaurantInventory.register_restaurant()
        TicketShop.read_data_client()
        TicketShop.read_data_facture()
        StadiumRestaurant.read_data_res_facture()
        print("\n⚽BIENVENIDO A QATAR 2022⚽\n")
        while True:
            print("MENÚ PRINCIPAL")
            option = input("""
            1- VENTA DE ENTRADAS
            2- GESTIÓN DE ASISTENCIA A PARTIDOS
            3- GESTIÓN DE VENTA DE RESTAURANTES
            4- ESTADÍSTICAS
            5- Salir del programa

            Ingrese el número del módulo al que se dirige: """)
            while not int(option) in range(1,6):
                option = input("¡ERROR! Ingrese el número del módulo al que desea acceder: ")
            if option == "1":
                TicketShop.register_client()    
            elif option == "2":
                TicketShop.match_attendance()
            elif option == "3":
                StadiumRestaurant.register_shop()
            elif option == "4":
                pass
            elif option == "5":
                TicketShop.save_data_client()
                TicketShop.save_data_facture()
                StadiumRestaurant.save_data_res_facture()
                break