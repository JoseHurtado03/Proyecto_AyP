from Client import Client
from MatchesOrganizer import MatchesOrganizer
from Facture import Facture
clients = []
factures = []
class TicketShop:
    def choose_seat(num):
        '''La función permite seleccionar el asiento que desea el cliente'''
        aux_count = 0
        aux_seats = []
        while aux_count < num:
            MatchesOrganizer.show_seats()
            fila = input("Ingrese la fila del asiento: ")
            while not fila.isalpha():
                fila = input("¡ERROR! Ingrese la fila del asiento: ")
            columna = input("Ingrese la columna del asiento: ")
            while not columna.isnumeric() and columna not in range(1,11):
                columna = input("¡ERROR! Ingrese la columna del asiento")
            aux_seat = fila + columna
            #Falta validar que el asiento no esté ocupaddo ya, en el mismo partido
            aux_seats.append(aux_seat)
            aux_count += 1
        return aux_seats
    def is_vampire(num):
        dig = []
        if len(num) % 2 == 0:
            for i in num:
                dig.append(i) 
            half = len(dig)//2
            first_p = dig[:half]
            second_p = dig[half:]
            r_uno = ""
            r_dos = ""
            for e in first_p:
                r_uno += e
            for j in second_p:
                r_dos += j
            if int(r_uno) * int(r_dos) == num:
                return True
            else: 
                return False   
        else:
            return False
    def register_client():
        '''La función se encarga de registrar a los clientes y la factura que genera su compra'''
        while True:
            print("\n⚽VENTA DE ENTRADAS⚽")
            name = input("Ingrese su nombre y apellido: ")
            while not " " in name:
                name = input("¡ERROR! Ingrese su nombre Y apellio: ")
            dni = input("Ingrese su número de cédula: ")
            while not dni.isnumeric():
                dni = input("¡ERROR!Ingrese su número de cédula: ")
            age = input("Ingrese su edad: ")
            while not age.isnumeric():
                age = input("¡ERROR! Ingrese su edad: ")
            select_match = input("""
            1- Ver todos los partidos
            2- Realizar una búsqueda del partido
            Ingrese la opción que desea para seleccionar el partido: """)
            while select_match != "1" and select_match != "2":
                select_match = input("¡ERROR! Selecciones la opción que desea para seleccionar un partido: ")
            if select_match == "1":
                MatchesOrganizer.show_matches()
                game = input("Ingrese el ID del partido al que desea ir: ")
                while not int(game) in range(1,49):
                    game = ("¡ERROR! Ingrese el ID del partido al que desea ir: ")
            elif select_match == "2":
                MatchesOrganizer.search_match()
                game = input("Ingrese el ID del partido al que desea ir: ")
                while not int(game) in range(1,49):
                    game = ("¡ERROR! Ingrese el ID del partido al que desea ir: ")
            ticket_type = input("""Ingrese el tipo de entrada que desea: 
            General 
            VIP
            ---> """)
            stadium_id = MatchesOrganizer.found_stadium_id(game)
            quantity_ticket = input("Ingrese la cantidad de entradas que desea comprar: ")
            ticket_id = (f"974{dni}")
            attendance = False
            seat = TicketShop.choose_seat(int(quantity_ticket))
            iva = 16
            price = 0
            aux_discount = 0
            if ticket_type.lower() == "vip":
                price += 120
            elif ticket_type.lower() == "general":
                price += 50
            if TicketShop.is_vampire(dni):
                aux_discount += 50
            subtotal = price * int(quantity_ticket)
            discount = subtotal * (aux_discount / 100)
            aux_subtotal = subtotal - discount
            aux_iva = aux_subtotal * (iva/100)
            total = aux_subtotal + aux_iva
            facture = Facture(ticket_id, name, dni, game, stadium_id, ticket_type, seat, subtotal, discount, iva, total)
            print(Facture.show_facture(facture))
            confirmation = input("¿Seguro de que desea realizar la compra? (y/n): ").lower()
            while confirmation != "y" and confirmation != "n":
                confirmation = input("¡ERROR! ¿Seguro de que desea realizar la compra? (y/n): ")
            if confirmation == "y":
                client = Client(name, dni, age, game, ticket_type, ticket_id, attendance)
                clients.append(client)
                factures.append(facture)
                print("**TRANSACCIÓN EXITOSA**\n")
                option = input("¿Desea comprar otra entrada? (y/n): ")
                while option != "y" and option != "n":
                    option = input("¡ERROR! ¿Seguro de que desea realizar la compra? (y/n): ")
                if option == "y":
                    pass
                elif option == "n":
                    break
            elif confirmation == "n":
                print("**Transacción detenida**")
                option = input("¿Desea intentarlo nuevamente? (y/n): ")
                while option != "y" and option != "n":
                    option = input("¡ERROR! ¿Seguro de que desea realizar la compra? (y/n): ")
                if option == "y":
                    pass
                elif option == "n":
                    break
    def save_data_client():
        '''La función guarda los datos de todos los clientes en un documento .txt'''
        for client in clients:
            clientes = open("clientes", "a")
            clientes.write(f"{client.name} {client.dni} {client.age} {client.game} {client.ticket_type} {client.ticket_id} {client.attendance}\n")
            clientes.close()
    def read_data_client():
        '''La función lee todos los datos de los clientes anteriormente 
        guardados en un documento .txt y los guarda en la lista de clientes'''
        with open("clientes") as f:
            for line in f:
                name = line.split(" ")[0] + " " + line.split(" ")[1]
                dni = line.split(" ")[2]
                age = line.split(" ")[3]
                game = line.split(" ")[4]
                ticket_type = line.split(" ")[5]
                ticket_id = line.split(" ")[6]
                attendance = line.split(" ")[7]
                client = Client(name, dni, age, game, ticket_type, ticket_id, attendance)
                clients.append(client)
    def save_data_facture():
        '''La función guarda los datos de todos las facturas en un documento .txt'''
        for facture in factures:
            facturas = open("facturas", "a")
            facturas.write(f"{facture.ticket_id} {facture.name} {facture.dni} {facture.game} {facture.stadium_id} {facture.ticket_type} {facture.seat} {facture.subtotal} {facture.discount} {facture.iva} {facture.total}\n")
            facturas.close()
    def read_data_facture():
        '''Lee todos los datos de las facturas guardadas en un documento .txt
        y los agrega a la lista de facturas'''
        with open("facturas") as f:
            for line in f:
                ticket_id = line.split(" ")[0]
                name = line.split(" ")[1] + " " + line.split(" ")[2]
                dni = line.split(" ")[3]
                game = line.split(" ")[4]
                stadium_id = line.split(" ")[5]
                ticket_type = line.split(" ")[6]
                seat = line.split(" ")[7]
                subtotal = line.split(" ")[8]
                discount = line.split(" ")[9]
                iva = line.split(" ")[10]
                total = line.split(" ")[11]
                facture = Facture(ticket_id, name, dni, game, stadium_id, ticket_type, seat, subtotal, discount, iva, total)
                factures.append(facture)
    def match_attendance():
        '''La función permite validar la asistencia a los partidos, usando el número único de cada factura'''
        while True:
            verify_ticket_id = input("Ingrese el código ID único de la entrada: ")
            for client in clients:
                if verify_ticket_id == client.ticket_id:
                    if client.attendance == False:
                        print("Entrada validada exitosamente, disfrute el partido\n")
                        client.attendance = True
                    elif client.attendance == True:
                        print("El ID del ticket ya ha ingresado al partido")
                else:
                    print("El ID de la entrada no fue encontrado")
            option_attendance = input("¿Desea seguir validando entradas? (y/n): ")
            while option_attendance != "y" and option_attendance != "n":
                option_attendance = input("¡ERROR! ¿Desea seguir validando entradas? (y/n): ")
            if option_attendance == "y":
                pass
            elif option_attendance == "n":
                break
    def pass_facture():
        '''Permite pasar la lista de facturas a otro módulo'''
        return factures