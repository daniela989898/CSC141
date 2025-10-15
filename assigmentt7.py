# 7-1
car = input("¿Qué tipo de coche de alquiler te gustaría? ")
print(f"Déjame ver si puedo encontrarte un {car.title()}.")
print()
# 7-2
people = int(input("¿Cuántas personas hay en tu grupo para cenar? "))
if people > 8:
    print("Lo siento, tendrán que esperar por una mesa.")
else:
    print("Su mesa está lista, síganme por favor.")
print()
# 7-3
number = int(input("Introduce un número: "))
if number % 10 == 0:
    print(f"El número {number} es múltiplo de 10.")
else:
    print(f"El número {number} no es múltiplo de 10.")
# 7-4
print("=== 7-4 Pizza Toppings ===")
print("Escribe 'quit' para terminar.\n")

while True:
    topping = input("Introduce un ingrediente para tu pizza: ")
    if topping.lower() == 'quit':
        print("Terminando el pedido de pizza...\n")
        break
    else:
        print(f"Añadiré {topping} a tu pizza.")
# 7-5 
print("=== 7-5 Movie Tickets ===")
print("Escribe 'quit' para salir.\n")
while True:
    age_input = input("¿Cuál es tu edad? ")
    if age_input.lower() == 'quit':
        print("Saliendo del programa de boletos...\n")
        break
    age = int(age_input)
    if age < 3:
        print("Tu entrada es gratis.")
    elif 3 <= age <= 12:
        print("Tu entrada cuesta $10.")
    else:
        print("Tu entrada cuesta $15.")
#7-6
print("=== 7-6 Three Exits ===\n")
print("Versión 1: Condición en el while")
topping = ""
while topping.lower() != 'quit':
    topping = input("Agrega un ingrediente (escribe 'quit' para salir): ")
    if topping.lower() != 'quit':
        print(f"Añadiré {topping} a tu pizza.")
print("¡Pedido completado!\n")
print("Versión 2: Variable activa")
active = True
while active:
    topping = input("Agrega un ingrediente (escribe 'quit' para salir): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Añadiré {topping} a tu pizza.")
print("¡Pedido completado!\n")
print("Versión 3: Usando break")
while True:
    topping = input("Agrega un ingrediente (escribe 'quit' para salir): ")
    if topping.lower() == 'quit':
        break
    print(f"Añadiré {topping} a tu pizza.")
print("¡Pedido completado!\n")
#7-7
print("=== 7-7 Infinity ===")
while True:
    print("¡Este bucle nunca termina! (Presiona CTRL+C para detenerlo)")
#7-8
sandwich_orders = ['jamón', 'atún', 'pollo', 'vegetal']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Preparé tu sándwich de {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print("\nTodos los sándwiches han sido preparados:")
for sandwich in finished_sandwiches:
    print(f" - {sandwich.title()}")
#7-9
print("\n=== 7-9 No Pastrami ===")
sandwich_orders = ['jamón', 'pastrami', 'pollo', 'pastrami', 'atún', 'pastrami']
finished_sandwiches = []
print("Lo sentimos, ¡nos hemos quedado sin pastrami!\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Preparé tu sándwich de {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print("\nEstos sándwiches fueron preparados:")
for sandwich in finished_sandwiches:
    print(f" - {sandwich.title()}")
#7-10
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    dream_vacation = input("If you could visit one place in the world, where would you go? ")
    responses[name] = dream_vacation
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")