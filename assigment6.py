# 1
person = {
    "first_name": "Carlos",
    "last_name": "Ramírez",
    "age": 25,
    "city": "Madrid"
}
print("First name:", person["first_name"])
print("Last name:", person["last_name"])
print("Age:", person["age"])
print("City:", person["city"])
# 2
favorite_numbers = {
    "Ana": 7,
    "Luis": 12,
    "Marta": 3,
    "Jorge": 15,
    "Sofía": 22
}
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
#3 
glossary = {
    "Variable": "A name that stores a value in memory.",
    "Loop": "A structure used to repeat a block of code multiple times.",
    "Function": "A reusable block of code that performs a specific task.",
    "List": "A collection of ordered items that can be changed.",
    "Dictionary": "A collection of key-value pairs used to store related data."
}
for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")
#4
glossary = {
    "Variable": "A name that stores a value in memory.",
    "Loop": "A structure used to repeat a block of code multiple times.",
    "Function": "A reusable block of code that performs a specific task.",
    "List": "A collection of ordered items that can be changed.",
    "Dictionary": "A collection of key-value pairs used to store related data.",
    "Tuple": "An ordered collection of items that cannot be changed.",
    "Boolean": "A data type that can be either True or False.",
    "String": "A sequence of characters enclosed in quotes.",
    "Comment": "Text in code ignored by Python, used for explanations.",
    "Module": "A file containing Python definitions and functions to be reused."
}
for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")
#5
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "danube": "germany"
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print()
print("Rivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())
print()  
print("Countries included in the dictionary:")
for country in rivers.values():
    print(country.title())
#6
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}
people_to_poll = ["jen", "sarah", "mike", "laura", "phil"]
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll.")
    else:
        print(f"{person.title()}, we invite you to take the poll!")
#7
person1 = {"first_name": "Alice", "last_name": "Johnson", "age": 25, "city": "New York"}
person2 = {"first_name": "Bob", "last_name": "Smith", "age": 30, "city": "London"}
person3 = {"first_name": "Charlie", "last_name": "Brown", "age": 28, "city": "Paris"}
people = [person1, person2, person3]
for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")
    print()
#8
pet1 = {"animal": "dog", "owner": "Sarah"}
pet2 = {"animal": "cat", "owner": "Tom"}
pet3 = {"animal": "parrot", "owner": "Lucy"}
pets = [pet1, pet2, pet3]
for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
    print()
#9
favorite_places = {
    "Alice": ["Paris", "New York", "Rome"],
    "Bob": ["Tokyo", "Berlin"],
    "Charlie": ["Sydney"]
}
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f" - {place}")
    print()
#10
favorite_numbers = {
    "Alice": [7, 42, 99],
    "Bob": [3, 8],
    "Charlie": [10, 20, 30],
    "Diana": [5],
    "Ethan": [12, 24]
}
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")
    print()
#11
cities = {
    "New York": {
        "country": "USA",
        "population": "8.6 million",
        "fact": "Known as the city that never sleeps."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "13.9 million",
        "fact": "Home to the busiest train station in the world."
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Famous for the Eiffel Tower."
    }
}
for city, info in cities.items():
    print(f"{city}:")
    for key, value in info.items():
        print(f"  {key.title()}: {value}")
    print()
#12
cities = {
    "New York": {
        "country": "USA",
        "population": "8.6 million",
        "fact": "Known as the city that never sleeps.",
        "famous_food": "Bagels"
    },
    "Tokyo": {
        "country": "Japan",
        "population": "13.9 million",
        "fact": "Home to the busiest train station in the world.",
        "famous_food": "Sushi"
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Famous for the Eiffel Tower.",
        "famous_food": "Croissants"
    }
}
for city, info in cities.items():
    print(f"--- {city.upper()} ---")
    for key, value in info.items():
        print(f"{key.replace('_',' ').title()}: {value}")
    print()
