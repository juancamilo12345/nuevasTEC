#se agrega inventario de tienda con un diccionario

inventario_tienda = {
    "manzanas": 50,
    "naranjas": 30,
    "platanos": 20,
    "fresas": 15
    "carne": 100,
    "pan": 80,
    "leche": 60,
    "huevos": 40,
    "queso": 25
    "arroz": 90,
    "pasta": 70,
    "aceite": 45
    "azucar": 55,
    "sal": 35,
    "cereal": 65,
    "jugo": 75
}

def mostrar_menu():
    print("¡Bienvenido a nuestra tienda!")
    print("--- Productos disponibles ---")
    for producto, precio in inventario.items():
        print(f"- {producto.capitalize()}: ${precio:.2f}")
    print("-" * 25)