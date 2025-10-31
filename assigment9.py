# 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"El restaurante '{self.restaurant_name}' sirve comida {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"¡El restaurante '{self.restaurant_name}' está ahora abierto!")
restaurant = Restaurant("La Buena Mesa", "Mediterránea")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
# 9-2
restaurant1 = Restaurant("Sakura Garden", "Japanese")
restaurant2 = Restaurant("Taco Fiesta", "Mexican")
restaurant3 = Restaurant("Royal Curry", "Indian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
# 9-3
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
    def describe_user(self):
        print(f"User Profile:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Location: {self.location}\n"
              f"Email: {self.email}\n")
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!\n")
user1 = User("Alice", "Johnson", 28, "New York", "alice@example.com")
user2 = User("Brian", "Lee", 34, "Los Angeles", "brian@example.com")
user3 = User("Sofia", "Martinez", 22, "Miami", "sofia@example.com")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
# 9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 
    def describe_restaurant(self):
        print(f"El restaurante '{self.restaurant_name}' sirve comida {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"¡El restaurante '{self.restaurant_name}' está ahora abierto!")
    def set_number_served(self, number):
        """Establece la cantidad de clientes servidos."""
        self.number_served = number
    def increment_number_served(self, number):
        """Incrementa el número de clientes servidos."""
        self.number_served += number
restaurant = Restaurant("El Buen Sabor", "Mexicana")
print(f"Clientes servidos: {restaurant.number_served}")
restaurant.number_served = 50
print(f"Clientes servidos (actualizado directamente): {restaurant.number_served}")
restaurant.set_number_served(120)
print(f"Clientes servidos (usando set_number_served): {restaurant.number_served}")
restaurant.increment_number_served(30)
print(f"Clientes servidos después de un día ocupado: {restaurant.number_served}")
# 9-5
class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
        self.login_attempts = 0 
    def describe_user(self):
        print(f"Perfil del usuario:\n"
              f"Nombre: {self.first_name} {self.last_name}\n"
              f"Edad: {self.age}\n"
              f"Ciudad: {self.city}\n"
              f"Correo: {self.email}\n")
    def greet_user(self):
        print(f"¡Hola {self.first_name}! Bienvenido/a de nuevo.\n")
    def increment_login_attempts(self):
        """Incrementa el número de intentos de inicio de sesión."""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """Reinicia los intentos de inicio de sesión a 0."""
        self.login_attempts = 0
user = User("Marta", "López", 27, "Sevilla", "marta.lopez@email.com")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Intentos de inicio de sesión: {user.login_attempts}")
user.reset_login_attempts()
print(f"Intentos de inicio de sesión después de reiniciar: {user.login_attempts}")
# 9-6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"El restaurante '{self.restaurant_name}' sirve comida {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"¡El restaurante '{self.restaurant_name}' está ahora abierto!")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="heladería"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vainilla", "chocolate", "fresa", "menta", "caramelo"]
    def display_flavors(self):
        print(f"Sabores disponibles en '{self.restaurant_name}':")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")
ice_cream_stand = IceCreamStand("Frosty Delight")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
# 9-7
class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
        self.login_attempts = 0
    def describe_user(self):
        print(f"Perfil del usuario:\n"
              f"Nombre: {self.first_name} {self.last_name}\n"
              f"Edad: {self.age}\n"
              f"Ciudad: {self.city}\n"
              f"Correo: {self.email}\n")
    def greet_user(self):
        print(f"¡Hola {self.first_name}! Bienvenido/a de nuevo.\n")
class Admin(User):
    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = [
            "puede agregar publicaciones",
            "puede eliminar publicaciones",
            "puede bloquear usuarios",
            "puede restablecer contraseñas"
        ]
    def show_privileges(self):
        print(f"Privilegios del administrador {self.first_name}:")
        for privilege in self.privileges:
            print(f" - {privilege}")
admin_user = Admin("Laura", "Sánchez", 31, "Madrid", "laura.admin@email.com")
admin_user.describe_user()
admin_user.show_privileges()
# 9-8
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "puede agregar publicaciones",
                "puede eliminar publicaciones",
                "puede bloquear usuarios"
            ]
        self.privileges = privileges
    def show_privileges(self):
        print("Privilegios del administrador:")
        for privilege in self.privileges:
            print(f" - {privilege}")
class Admin(User):
    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = Privileges()
super_admin = Admin("Diego", "Torres", 40, "Barcelona", "diego.admin@email.com")
super_admin.describe_user()
super_admin.privileges.show_privileges()
# 9-9
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"Este coche tiene una batería de {self.battery_size}-kWh.")
    def get_range(self):
        """Devuelve la autonomía aproximada según el tamaño de la batería."""
        if self.battery_size == 40:
            range_km = 240
        elif self.battery_size == 65:
            range_km = 400
        print(f"Este coche puede recorrer aproximadamente {range_km} km con una carga completa.")
    def upgrade_battery(self):
        """Aumenta la capacidad a 65 kWh si aún no lo está."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("La batería ha sido mejorada a 65 kWh.")
        else:
            print("La batería ya está actualizada.")
class ElectricCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.battery = Battery()
    def describe_car(self):
        print(f"{self.make} {self.model}")
my_car = ElectricCar("Nissan", "Leaf")
my_car.describe_car()
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()
# 9-10
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"El restaurante '{self.restaurant_name}' sirve comida {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"¡El restaurante '{self.restaurant_name}' está ahora abierto!")
from restaurant import Restaurant
my_restaurant = Restaurant("La Estrella Dorada", "Mediterránea")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
# 9-11
class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
    def describe_user(self):
        print(f"Usuario: {self.first_name} {self.last_name} - {self.age} años - {self.city}")
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"]
        self.privileges = privileges
    def show_privileges(self):
        print("Privilegios del administrador:")
        for privilege in self.privileges:
            print(f" - {privilege}")
class Admin(User):
    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = Privileges()
admin = Admin("Lucía", "García", 30, "Madrid", "lucia.admin@email.com")
admin.describe_user()
admin.privileges.show_privileges()
# 9-12
class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
    def describe_user(self):
        print(f"Usuario: {self.first_name} {self.last_name} - {self.age} años - {self.city}")
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"]
        self.privileges = privileges
    def show_privileges(self):
        print("Privilegios del administrador:")
        for privilege in self.privileges:
            print(f" - {privilege}")
class Admin(User):
    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = Privileges()
admin = Admin("Carlos", "Morales", 42, "Sevilla", "carlos.admin@email.com")
admin.describe_user()
admin.privileges.show_privileges()
# 9-13
import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return random.randint(1, self.sides)
die_6 = Die()
for i in range(10):
    print(f"Dado de 6 lados: {die_6.roll_die()}")
die_10 = Die(10)
for i in range(10):
    print(f"Dado de 10 lados: {die_10.roll_die()}")
die_20 = Die(20)
for i in range(10):
    print(f"Dado de 20 lados: {die_20.roll_die()}")
# 9-14
import random
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
winning_combination = random.sample(elements, 4)
print("Los números/letras ganadores son:")
print(winning_combination)
print("¡Cualquier boleto que tenga esta combinación gana un premio!")
# 9-15
import random
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
winning_combination = random.sample(elements, 4)
my_ticket = random.sample(elements, 4)
count = 0
while my_ticket != winning_combination:
    count += 1
    winning_combination = random.sample(elements, 4)
print(f"Tu boleto {my_ticket} ha ganado después de {count} intentos.")
# 9-16
import random
import math
import datetime
import statistics
print("El módulo 'random' se usa para generar valores aleatorios, ideal para juegos, sorteos o simulaciones.")
print("Ejemplo:")
print(f"Número aleatorio entre 1 y 10: {random.randint(1, 10)}")
print("\nEl módulo 'math' proporciona funciones matemáticas avanzadas.")
print("Ejemplo:")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print("\nEl módulo 'datetime' maneja fechas y horas.")
print("Ejemplo:")
print(f"Fecha y hora actuales: {datetime.datetime.now()}")
print("\nEl módulo 'statistics' ofrece herramientas para análisis estadístico.")
print("Ejemplo:")
print(f"Media de [10, 20, 30]: {statistics.mean([10, 20, 30])}")