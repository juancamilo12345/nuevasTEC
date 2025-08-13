#se agrega inventario de tienda con un diccionario

inventario_tienda = {
    "manzanas": 50,
    "naranjas": 30,
    "platanos": 20,
    "fresas": 15,
    "carne": 100,
    "pan": 80,
    "leche": 60,
    "huevos": 40,
    "queso": 25,
    "arroz": 90,
    "pasta": 70,
    "aceite": 45,
    "azucar": 55,
    "sal": 35,
    "cereal": 65,
    "jugo": 75
}

def mostrar_menu():
    print("¡Bienvenido a nuestra tienda!")
    print("--- Productos disponibles ---")
    for producto, precio in inventario_tienda.items():
        print(f"- {producto.capitalize()}: ${precio:.2f}")
    print("-" * 25)

carrito = {}
total_compra = 0

while True:
    mostrar_menu()
    
    accion = input("¿Qué deseas hacer? (agregar, ver, pagar, salir): ").lower()
    
    if accion == "agregar":
        producto = input("Ingresa el nombre del producto que deseas agregar: ").lower()
        if producto in inventario_tienda:
            cantidad = int(input(f"¿Cuántas unidades de {producto} quieres? "))
            if producto in carrito:
                carrito[producto] += cantidad
            else:
                carrito[producto] = cantidad
            print(f"{cantidad} {producto}(s) agregados al carrito.")
        else:
            print("Ese producto no está en el inventario.")
            
    elif accion == "ver":
        print("--- Tu carrito de compras ---")
        if not carrito:
            print("El carrito está vacío.")
        else:
            for producto, cantidad in carrito.items():
                precio_unitario = inventario_tienda[producto]
                subtotal = precio_unitario * cantidad
                print(f"- {producto.capitalize()} (x{cantidad}): ${subtotal:.2f}")
        
    elif accion == "pagar":
        print("--- Factura de compra ---")
        total_compra = 0
        for producto, cantidad in carrito.items():
            precio_unitario = inventario_tienda[producto]
            subtotal = precio_unitario * cantidad
            print(f"- {producto.capitalize()} (x{cantidad}): ${subtotal:.2f}")
            total_compra += subtotal
        print("-" * 25)
        print(f"Total a pagar: ${total_compra:.2f}")
        print("¡Gracias por tu compra!")
        break
        
    elif accion == "salir":
        print("¡Vuelve pronto!")
        break
    
    else:
        print("Opción no válida. Por favor, elige entre 'agregar', 'ver', 'pagar' o 'salir'.")