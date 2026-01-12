# Inventory Management System

inventory = {}  # Empty dictionary to store products

while True:
    print("\n------ INVENTORY MENU ------")
    print("1. Add New Product")
    print("2. Update Product Quantity")
    print("3. Show All Products")
    print("4. Calculate Total Inventory Value")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # 1. Add New Product
    if choice == '1':
        name = input("Enter product name: ").title()
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per item: ₹"))
        inventory[name] = {'quantity': qty, 'price': price}
        print(f"✅ {name} added to inventory!")

    # 2. Update Product Quantity
    elif choice == '2':
        name = input("Enter product name to update: ").title()
        if name in inventory:
            new_qty = int(input("Enter new quantity: "))
            inventory[name]['quantity'] = new_qty
            print(f"🔄 Quantity of {name} updated to {new_qty}!")
        else:
            print("Product not found!")

    # 3. Show All Products
    elif choice == '3':
        if not inventory:
            print("No products in inventory!")
        else:
            print("\n📦 Current Inventory:")
            for name, details in inventory.items():
                print(f"{name} - Qty: {details['quantity']}, Price: ₹{details['price']}")

    # 4. Calculate Total Inventory Value
    elif choice == '4':
        if not inventory:
            print("No products to calculate!")
        else:
            total_value = sum(details['quantity'] * details['price'] for details in inventory.values())
            print(f"\n💰 Total Inventory Value: ₹{total_value:.2f}")

    # 5. Exit
    elif choice == '5':
        print("👋 Exiting Inventory System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")

 
