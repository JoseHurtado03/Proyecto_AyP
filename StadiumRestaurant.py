from RestaurantInventory import RestaurantInventory
from TicketShop import TicketShop
from MatchesOrganizer import MatchesOrganizer
from ResFacture import ResFacture
stadiums = MatchesOrganizer.pass_stadium()
factures = TicketShop.pass_facture()
restaurants = RestaurantInventory.pass_restaurant()
res_factures = []
class StadiumRestaurant:
    def perfect_num(num):
        '''Recibe un número y retorna True si el número es un Número Perfecto. 
        Si no, retorna False'''
        suma = 0
        for i in range(1,num):
            if (num % i == 0):
                suma += i
        if num == suma:
            return True
        else:
            return False
    def register_shop():
        '''Registra las compras en un restaurante. Valida que el cliente sea VIP,
        Muestra el menú del restaurante, calcula el precio total a pagar y guarda
        la factura generada en la compra'''
        dni = input("Por favor, ingrese la cédula del cliente: ")
        for facture in factures:
            if dni == facture.dni:
                if facture.ticket_type == "general":
                    print("El cliente está registrado, pero no posee una entrada VIP")
                    break
                elif facture.ticket_type == "vip":
                    print("Cliente VIP encontrado exitosamente")
                    subtotal = 0
                    discount = 0
                    iva = 16
                    aux_res = []
                    for restaurant in restaurants:
                        if facture.stadium_id == restaurant.stadium_id:
                            aux_res.append(restaurant)
                    for restaurant_s in aux_res:
                        aux = 0
                        name = facture.name
                        dni = facture.dni
                        products = []
                        print(f"{aux+1}- {restaurant_s.name}")
                        choose_res = int(input("Ingresa el restaurante al que quieres ir: "))
                        print(f"\nBienvenido a {aux_res[choose_res-1].name}\n")
                        exit = "n"
                        while exit == "n":
                            print("Realice la búsqueda de lo que desea ordenar")
                            RestaurantInventory.search_product(aux_res[choose_res-1])
                            product_buy = input("Ingrese el nombre del producto que desea comprar (Copiar y pegar): ")
                            for product in aux_res[choose_res-1].products:
                                if product_buy.capitalize() == product.name:
                                    products.append(product_buy)
                                    quantity = int(input("¿Cuántos desea comprar?: "))
                                    subtotal += (quantity * product.price)
                                    option = input("¿Desea comprar otro producto? (y/n): ")
                                    while option != "y" and option != "n":
                                        option = input("¡ERROR! ¿Desea comprar otro producto? (y/n): ")
                                    if option == "y":
                                        pass
                                    elif option == "n":
                                        if StadiumRestaurant.perfect_num(int(dni)):
                                            discount += 15
                                        else:
                                            discount += 0
                                        aux_discount = (subtotal * (discount/100))
                                        aux_subtotal = (subtotal - aux_discount)
                                        aux_iva = (aux_subtotal * (iva/100))
                                        total = (subtotal - aux_discount) + aux_iva
                                        res_facture = ResFacture(name, dni, aux_res[choose_res-1].name, products, subtotal, discount, iva, total)
                                        print(ResFacture.show_res_facture(res_facture))
                                        confirm = input("¿Desea proceder con la compra? (y/n): ").lower()
                                        while option != "y" and option != "n":
                                            confirm = input("¡ERROR! ¿Desea proceder con la compra? (y/n): ")
                                        if confirm == "y":
                                            print("TRANSACCIÓN REALIZADA EXITOSAMENTE. ¡Buen provecho!")
                                            res_factures.append(res_facture)
                                            exit = "y"
                                        elif confirm == "n":
                                            print("Transacción detenida. Vuelva pronto")
                                            exit = "y"
    def save_data_res_facture():
        '''La función guarda los datos de todos las facturas del restaurante en un documento .txt'''
        for facture in res_factures:
            facturas_rest = open("facturas_rest", "a")
            facturas_rest.write(f"{facture.name}-{facture.dni}-{facture.restaurant}-{facture.products}-{facture.subtotal}-{facture.discount}-{facture.iva}-{facture.total}\n")
            facturas_rest.close()
    def read_data_res_facture():
        '''Lee todos los datos de las facturas del restaurante guardadas 
        en un documento .txt y los agrega a la lista de facturas'''
        with open("facturas_rest") as f:
            for line in f:
                name = line.split("-")[0]
                dni = line.split("-")[1]
                restaurant = line.split("-")[2]
                products = line.split("-")[3]
                subtotal = line.split("-")[4]
                discount = line.split("-")[5]
                iva = line.split("-")[6]
                total = line.split("-")[7]
                res_facture = ResFacture(name, dni, restaurant, products, subtotal, discount, iva, total)
                res_factures.append(res_facture)
                print(ResFacture.show_res_facture(res_facture))