# 3-1
names = ["Marcos", "Daniela", "Maria", "Dani"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
# 3-2
for name in names:
    print(f"¡Hola, {name}! Espero que tengas un buen día.")
# 3-3
transportations = ["tren", "avión", "bici", "coche"]
for transport in transportations:
    print(f"Me gustaria tener {transport}.")
# 3-4
names = ["abuelo", "Rafa Nadal", "Roger Federer"]
for name in names:
    print(f"Querido {name}, Megustaría invitarte a cenar.")
# 3-5 
del names[2]
names.append(" Siento que no puedas asistir a la cena ojala tener otra oportunidad para poder cenar juntos.")
print(names)
# 3-6 
print("\nHe encontrado una mesa mas grande!")
names.insert(0, 'Rafa Nadal')
guest = ["Arina Sabalenka"]
for name in guest:
    print(f"{name.title()}, podrias venir a la cena.")

    del names[2]
names.append
# 3-7 
guests = ["abuelo", "Roger Federer", "Arina Sabalenca"]
print("\nLo siento, la nueva mesa no llegará a tiempo. Solo puedo invitar a dos personas.")
while len(guests) > 2:
    removed = guests.pop()
    print(f"Perdón, {removed.title()}, no te puedo invitar a la cena.")
for name in guests:
    print(f"{name.title()}, todavía estás invitado a cenar.")
guests.clear()
print("\nLista final de invitados:", guests)
# 3-8 
places = ["París", "León", "Bilbao", "Berlin", "Copenage"]
print(places) 
print(sorted(places))
print(places) 
print(sorted(places, reverse=True)) 
print(places) 
places.reverse()
print(places) 
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places) 
# 3-9
invitations = ["abuelo", "Rafa Nadal", "Roger Federer"]
count_invitations = len(invitations)
print(f"{count_invitations} personas vendrán a mi cena.") 
# 3-10
countries = ["España", "Canadá", "China", "Italia", "Suiza"]
print(countries) 
countries.append("India")
print(countries)
countries.insert(2, "Chile") 
print(countries)
del countries[4] 
print(countries)
popped = countries.pop(50)
print(f"Eliminado: {popped}")
print(countries)
print(sorted(countries))
print(countries)
countries.sort()
print(countries)
countries.reverse()
print(countries)
print(f"Tamaño de la lista: {len(countries)}")
# 3-11 
#File "c:\Users\dandi\Favorites\CSC141\asigment3\assigment3.py", line 69, in <module>popped = countries.pop(50)IndexError: pop index out of range