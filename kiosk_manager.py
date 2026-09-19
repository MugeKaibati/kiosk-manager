import os
kiosk_name = input("Enter kiosk name: ").strip().title()
owner_name = input("Enter owner's name: ").strip().title()

print(f"\nWelcome to {kiosk_name}'s Kiosk Manager, run by {owner_name}.")

if os.path.exists("inventory.txt"):
    inventory = {}

    with open("inventory.txt", "r") as file:
        for line in file:
            parts = line.split(",")

            product = parts[0].strip()
            price = int(parts[1].strip())
            quantity = int(parts[2].strip())

            inventory[product] = {
                "price": price,
                "quantity": quantity
            }

else:
    inventory = {
        "Bread": {"price": 65, "quantity": 20},
        "Milk": {"price": 55, "quantity": 15},
        "Sugar": {"price": 150, "quantity": 10}
    }

if os.path.exists("sales.txt"):
    sales = []

    with open("sales.txt", "r") as file:
        for line in file:
            parts = line.split(",")

            product = parts[0].strip()
            quantity = int(parts[1].strip())
            total = int(parts[2].strip())

            sales.append((product, quantity, total))

else:
    sales = []

while True:
    print("\n===== MENU =====")
    print("1) View Stock")
    print("2) Add/Restock a Product")
    print("3) Sell a Product")
    print("4) View Sales Report")
    print("5) Search Products")
    print("6) Exit")
    print("==================")

    choice = input("Choose an option: ").strip()

    if not choice.isdigit():
        print("Invalid input. Please enter a number (1-6).")
        continue

    choice = int(choice)

    if choice < 1 or choice > 6:
        print("Please choose a number between 1 and 6.")
        continue

    # View Stock
    if choice == 1:
        print("\n====== Current Stock ======")

        for product, details in inventory.items():
            print(
                f"Product: {product} | "
                f"Price: Ksh {details['price']} | "
                f"Quantity: {details['quantity']}"
            )

        print("===========================")

    # Add/Restock Product
    elif choice == 2:
        product = input("Enter product name: ").strip().title()
        if product =="":
            print("Product name cannot be empty.")
            continue
        

        if product not in inventory:
            price = input("Enter price: ")
            if not price.isdigit():
                print("Please enter a valid number.")
                continue
            price = int(price)
            if price <= 0:
                print("Price must be greater than 0.")
                continue
            quantity = input("Enter quantity: ")
            if not quantity.isdigit():
                print("Please enter a valid number.")
                continue
            quantity = int(quantity)
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            inventory[product] = {
                "price": price,
                "quantity": quantity
            }

            print(f"{product} added successfully!")

        else:
            quantity = input("Enter quantity to add: ")

            if not quantity.isdigit():
                print("Please enter a valid number.")
                continue

            quantity = int(quantity)

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            inventory[product]["quantity"] += quantity

            print(f"{product} restocked successfully!")

    # Sell Product
    elif choice == 3:
        product = input("Enter product name: ").strip().title()
        if product == "":
            print("Product name cannot be empty.")
            continue
        if product not in inventory:
            print(f"{product} does not exist.")

        else:
            buys = input("How many do you want to buy? ")
            if not buys.isdigit():
                print("Please enter a valid number.")
                continue
            buys = int(buys)
            if buys <= 0:
                print("Quantity must be greater than 0.")
                continue


            if buys <= inventory[product]["quantity"]:
                total = inventory[product]["price"] * buys

                inventory[product]["quantity"] -= buys

                sales.append((product, buys, total))
                with open("sales.txt", "a") as file:
                    file.write(f"{product}, {buys}, {total}\n")

                print(f"\nProduct: {product}")
                print(f"Quantity Sold: {buys}")
                print(f"Price Per Item: Ksh {inventory[product]['price']}")
                print(f"Total: Ksh {total}")
                print(f"Remaining Stock: {inventory[product]['quantity']}")

            else:
                print("There is not enough stock!")

    # Sales Report
    elif choice == 4:
        if not sales:
            print("No sales recorded yet.")
            continue
        total_revenue = 0
        unique_products = set()
        product_sales = {}

        for product, quantity, total in sales:

            if product not in product_sales:
                product_sales[product] = quantity
            else:
                product_sales[product] += quantity

            print(
                f"Sale: {product} | "
                f"Quantity: {quantity} | "
                f"Total: Ksh {total}"
            )

            total_revenue += total
            unique_products.add(product)

        best_product = ""
        highest_quantity = 0

        for product, quantity in product_sales.items():

            if quantity > highest_quantity:
                highest_quantity = quantity
                best_product = product

        print("\n====== SALES SUMMARY ======")
        print(f"Total Revenue: Ksh {total_revenue}")
        print(f"Unique Products Sold: {len(unique_products)}")
        print(f"Best-Selling Product: {best_product}")
        print(f"Quantity Sold: {highest_quantity}")
        print("===========================")

    # Search Products
    elif choice == 5:
        search = input("Enter product name to search: ").strip().lower()
        if search =="":
            print("Search item cannot be empty.")
            continue

        found = False

        for product, details in inventory.items():
            if search in product.lower():
                print(
                    f"Product: {product} | "
                    f"Price: Ksh {details['price']} | "
                    f"Quantity: {details['quantity']}"
                )
                found = True

        if not found:
            print("No matching products found.")

    # Exit
    elif choice == 6:
        with open("inventory.txt", "w") as file:

            for product, details in inventory.items():
                file.write(
                    f"{product}, "
                    f"{details['price']}, "
                    f"{details['quantity']}\n"
                )

        break