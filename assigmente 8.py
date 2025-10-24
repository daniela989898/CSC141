# 8-1
def display_message():
    print("In this chapter, I am learning about functions in Python.")
display_message()
# 8-2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonderland")
# 8-3
def make_shirt(size, message):
    print(f"The shirt size is {size}, and it will have the message: '{message}'.")
make_shirt("Medium", "Keep calm and code Python")
make_shirt(size="Large", message="Coding is fun!")
# 8-4
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size}, and it will have the message: '{message}'.")
make_shirt()
make_shirt(size="Medium")
make_shirt(size="Small", message="Python power!")
# 8-5
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik") 
describe_city("Akureyri")
describe_city("Tokyo", country="Japan") 
# 8-6
def city_country(city, country):
    """Return a string formatted like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"
pair1 = city_country("santiago", "chile")
pair2 = city_country("tokyo", "japan")
pair3 = city_country("paris", "france")
print(pair1)
print(pair2)
print(pair3)
# 8-7
def make_album(artist, title, num_songs=None):
    """Return a dictionary containing information about a music album."""
    album = {
        "artist": artist.title(),
        "title": title.title()
    }
    if num_songs:
        album["songs"] = num_songs
    return album
album1 = make_album("nirvana", "nevermind")
album2 = make_album("taylor swift", "1989", 13)
album3 = make_album("queen", "a night at the opera")
print(album1)
print(album2)
print(album3)
# 8-8
def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist.title(),
        "title": title.title()
    }
    if num_songs:
        album["songs"] = num_songs
    return album
while True:
    print("\nEnter album information (or type 'quit' to exit):")
    artist_name = input("Artist name: ")
    if artist_name.lower() == 'quit':
        break
    album_title = input("Album title: ")
    if album_title.lower() == 'quit':
        break
    songs_input = input("Number of songs (optional, press Enter to skip): ")
    if songs_input.lower() == 'quit':
        break
    if songs_input.strip():
        album = make_album(artist_name, album_title, int(songs_input))
    else:
        album = make_album(artist_name, album_title)
    print("\nAlbum created:")
    print(album)
# 8-9
def mostrar_mensajes(mensajes):
    """Muestra cada mensaje de una lista."""
    print("Mostrando todos los mensajes:")
    for mensaje in mensajes:
        print(f"- {mensaje}")
mensajes = ["Hola!", "¿Cómo estás?", "¡Nos vemos pronto!"]
mostrar_mensajes(mensajes)
# 8-10
def enviar_mensajes(mensajes, mensajes_enviados):
    """Imprime cada mensaje y lo mueve a la lista de mensajes enviados."""
    print("Enviando mensajes...")
    while mensajes:
        mensaje = mensajes.pop(0)
        print(f"Enviando: {mensaje}")
        mensajes_enviados.append(mensaje)
mensajes = ["Hola!", "¿Cómo estás?", "¡Nos vemos pronto!"]
mensajes_enviados = []
enviar_mensajes(mensajes, mensajes_enviados)
print("\nMensajes originales:", mensajes)
print("Mensajes enviados:", mensajes_enviados)
# 8-11
def enviar_mensajes(mensajes, mensajes_enviados):
    """Imprime cada mensaje y lo mueve a la lista de mensajes enviados."""
    print("Enviando mensajes...")
    while mensajes:
        mensaje = mensajes.pop(0)
        print(f"Enviando: {mensaje}")
        mensajes_enviados.append(mensaje)
mensajes = ["Hola!", "¿Cómo estás?", "¡Nos vemos pronto!"]
mensajes_enviados = []
enviar_mensajes(mensajes[:], mensajes_enviados)
print("\nLista original (sin cambios):", mensajes)
print("Lista de mensajes enviados:", mensajes_enviados)
# 8-12
def hacer_sandwich(*ingredientes):
    """Muestra un resumen del sándwich que se está ordenando."""
    print("\nPreparando un sándwich con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente.title()}")
    print("¡Tu sándwich estará listo pronto!")
hacer_sandwich("jamón", "queso")
hacer_sandwich("pollo", "lechuga", "tomate", "mayonesa")
hacer_sandwich("atún", "pepino", "huevo", "cebolla", "mostaza")
# 8-13
def construir_perfil(nombre, apellido, **info_usuario):
    """Crea un diccionario que contenga toda la información del usuario."""
    perfil = {}
    perfil["nombre"] = nombre.title()
    perfil["apellido"] = apellido.title()
    for clave, valor in info_usuario.items():
        perfil[clave] = valor
    return perfil
mi_perfil = construir_perfil(
    "carlos",
    "gonzález",
    edad=25,
    ciudad="madrid",
    profesion="desarrollador"
)
print(mi_perfil)
# 8-14
def crear_auto(fabricante, modelo, **info_extra):
    """Crea un diccionario con información sobre un auto."""
    auto = {
        "fabricante": fabricante.title(),
        "modelo": modelo.title()
    }
    for clave, valor in info_extra.items():
        auto[clave] = valor
    return auto
auto1 = crear_auto("subaru", "outback", color="azul", paquete_remolque=True)
auto2 = crear_auto("tesla", "model s", color="rojo", autopilot=True)
auto3 = crear_auto("toyota", "corolla", año=2024, transmision="automática")
print(auto1)
print(auto2)
print(auto3)