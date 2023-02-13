import requests
from Product import Product
from Restaurant import Restaurant
from Beverage import Beverage
from Food import Food
restaurants = []
foods = []
beverages = []
class RestaurantInventory:
    def register_restaurant(url= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"):
        '''La función registra los restaurantes y además, registra los productos que se venden en cada restaurante, guardandolos como bebidas o comidas'''
        data = requests.get(url).json()
        for stadium in data:
            stadium_id = stadium["id"]
            for restaurant in stadium["restaurants"]:
                name_r = restaurant["name"]
                products = []
                for product in restaurant["products"]:
                    name = product["name"]
                    quantity = product["quantity"]
                    price = product["price"]
                    type_product = product["type"]
                    additional = product["adicional"]
                    if type_product == "food":
                        food = Food(name, quantity, price, type_product, additional)
                        foods.append(food)
                        products.append(food)
                    elif type_product == "beverages":
                        beverage = Beverage(name, quantity, price, type_product, additional)
                        beverages.append(beverage)
                        products.append(beverage)
                restaurant = Restaurant(name_r, stadium_id, products)
                restaurants.append(restaurant)
    def search_product(current_restaurant):
        '''La función permite hacer búsquedas de los productos por nombre, precio y tipo. Además, puede mostrar todo el menú del restaurant'''
        option = input("""
        1- Buscar por nombre
        2- Buscar por tipo
        3- Buscar por precio
        4- Ver todos los productos
        Ingrese la opción por la que desea buscar: """)
        while not int(option) in range(1,5):
            option= input("¡ERROR! Ingrese la opción por la que desea buscar: ")
        if option == "1":
            aux = 0
            name_s = input("Ingrese el nombre del producto: ").capitalize()
            for product in current_restaurant.products:
                if name_s == product.name:
                    print(f"****{aux+1}****")
                    print(Product.show_product(product))
                    aux += 1
        elif option == "2":
            aux = 0
            type_s = input("Ingrese el tipo de producto que busca (beverages/food): ")
            for product in current_restaurant.products:
                if type_s == product.type_product:
                    print(f"****{aux+1}****")
                    print(Product.show_product(product))
                    aux += 1
        elif option == "3":
            aux = 0
            price_s = input("Ingrese el monto máximo del precio: ")
            for product in current_restaurant.products:
                if int(price_s) >= product.price:
                    print(f"****{aux+1}****")
                    print(Product.show_product(product))
                    aux += 1
        elif option == "4":
            aux = 0
            for product in current_restaurant.products:
                print(f"****{aux+1}****")
                print(Product.show_product(product))
                aux += 1
    def pass_restaurant():
        '''Permite pasar la lista de restaurantes a otro módulo'''
        return restaurants