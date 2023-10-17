# Dinero inicial del usuario
availableMoney = 100

# Diccionario que contiene los productos y sus precios
products = {
    "Water": 10,
    "Milk": 20,
    "Eggs": 15
}

# Inicializamos el carrito como una lista vacía para almacenar los ítems
cart = []

# Función para mostrar el menú
def showMenu():
    print("Welcome to the terminal shopping cart.")
    print("1. Display Products")
    print("2. View Cart")
    print("3. Add Item to Cart")
    print("4. Remove Item from Cart")
    print("5. Exit")




# Función para mostrar el menú de productos disponibles
def showProducts():
  print("Menu:")
  for product, price in products.items():
    print(f"{product} - ${price}")

# Función para agregar un ítem al carrito
def addItemToCart(product):
    cart.append(product)
    print(f"{product} has been added to your cart.")

# Función para mostrar los ítems comprados.
def showPurchasedItems():
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item in cart:
            print("- " + item)

# Función para comprar ítems en el carrito
def purchaseItems():
    total = 0
    print("Items in your cart:")
    for item in cart:
        print("- " + item)
        # Calculamos el total sumando el precio de los productos
        if item == "Water":
            total += 10
        elif item == "Milk":
            total += 20
        elif item == "Eggs":
            total += 15
    print(f"Total amount: ${total}")
    # Limpiamos el carrito después de la compra
    cart.clear()

def addProduct():
    if len(cart) >= 10:
        print("Sorry, you cannot add more than 10 products to the cart.")
    else:
        showProducts()
        selection = input("Select a product (1-3): ")
        product = None
        if selection == "1":
            product = "Water"
        elif selection == "2":
            product = "Milk"
        elif selection == "3":
            product = "Eggs"
        else:
            print("Invalid option. Please select a valid number.")

        if product:
            addItemToCart(product)

def deleteCartItem():
    global availableMoney
    if len(cart) == 0:
        print("Your cart is empty. There are no items to delete.")
    else:
        print("Items in your cart:")
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item}")

        selection = input("Select the number of the item you wish to delete: ")
        try:
            selection = int(selection)
            if 1 <= selection <= len(cart):
                deleted_item = cart.pop(selection - 1)
                availableMoney -= products.get(deleted_item, 0)
                print(f"{deleted_item} Has been removed from the cart. Remaining money: ${availableMoney}")
            else:
                print("Invalid selection. Please select a valid number.")
        except ValueError:
            print("Invalid entry. Please enter a number.")

# Loop principal del programa
while True:
    showMenu()
    option = input("Please select an option: ")

    if option == "1":
        showProducts()
    elif option == "2":
        showPurchasedItems()
    elif option == "3":
        addProduct()
    elif option == "4":
        deleteCartItem()
    elif option == "5":
        print("Thank you for using our shopping cart, see you later!")
        break
    else:
        print("Invalid option. Please select a number from 1 to 5.")


