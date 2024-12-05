inventory = [
    {"id": 1, "name": "Macbook", "price": 999.99}, 
    {"id": 2, "name": "Airpods", "price": 599.99},  
    {"id": 3, "name": "IPhone", "price": 89.99}     
]

# Cart to store selected products
cart = []

# Function to display available products
def display_products():
    print("\nAvailable Products:")
    for product in inventory:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")
    print()

# Function to add a product to the cart
def add_to_cart():
    try:
        product_id = int(input("Enter the product ID to add to cart: "))  # Prompt for product ID
        quantity = int(input("Enter the quantity: "))  # Prompt for quantity

        # Find the product in inventory
        product = next((item for item in inventory if item["id"] == product_id), None)
        if product:
            # Check if the product is already in the cart
            existing_item = next((item for item in cart if item["id"] == product_id), None)
            if existing_item:
                existing_item["quantity"] += quantity  # Update quantity if exists
            else:
                # Add new product to cart
                cart.append(
                    {"id": product_id, "name": product["name"], "price": product["price"], "quantity": quantity})
            print(f"{product['name']} added to cart.")
        else:
            print("Invalid product ID.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Function to display the cart
def view_cart():
    if not cart:  # Check if cart is empty
        print("\nYour cart is empty.\n")
        return
    print("\nYour Shopping Cart:")
    total = 0  # Initialize total cost
    for item in cart:
        item_total = item["price"] * item["quantity"]  # Calculate total for each item
        total += item_total  # Add to overall total
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Total: ${item_total:.2f}")
    print(f"Overall Total: ${total:.2f}\n")

# Function to remove an item from the cart
def remove_from_cart():
    try:
        product_id = int(input("Enter the product ID to remove from cart: "))  # Prompt for product ID
        # Find the item in the cart
        item = next((item for item in cart if item["id"] == product_id), None)
        if item:
            cart.remove(item)  # Remove item from cart
            print(f"{item['name']} removed from cart.")
        else:
            print("Item not found in cart.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Function to complete the purchase
def complete_purchase():
    if not cart:  # Check if cart is empty
        print("\nYour cart is empty. Cannot complete purchase.\n")
        return
    total = sum(item["price"] * item["quantity"] for item in cart)  # Calculate total cost
    print(f"\nYour total is: ${total:.2f}")
    confirm = input("Do you want to complete the purchase? (yes/no): ").strip().lower()  # Prompt for confirmation
    if confirm == "yes":
        print("Purchase completed successfully. Thank you!")  # Complete purchase
        cart.clear()  # Clear the cart
    else:
        print("Purchase canceled.")

# Main menu to interact with the store
def menu():
    while True:
        print("\nMenu:")
        print("1. View Products")  # Option to view products
        print("2. Add to Cart")  # Option to add products to cart
        print("3. View Cart")  # Option to view cart
        print("4. Remove from Cart")  # Option to remove products from cart
        print("5. Complete Purchase")  # Option to complete the purchase
        print("6. Exit")  # Option to exit
        try:
            choice = int(input("Enter your choice: "))  # Prompt for menu choice
            if choice == 1:
                display_products()
            elif choice == 2:
                add_to_cart()
            elif choice == 3:
                view_cart()
            elif choice == 4:
                remove_from_cart()
            elif choice == 5:
                complete_purchase()
            elif choice == 6:
                print("Exiting the store. Goodbye!")  # Exit message
                break
            else:
                print("Invalid choice. Please select a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Entry point of the program
if __name__ == "__main__":
    menu()
