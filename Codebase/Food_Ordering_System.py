# Menu dictionary jisme item ka naam (key) aur price (value) hai
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 80,
    "Coke": 40
}

# Cart list jisme customer ke add kiye gaye items store honge
cart = []
discount_applied = False


# 1. Menu Dikhana
def show_menu():
    print("\n--- MENU ---")
    for item in menu:
        print(f"{item} - Rs. {menu[item]}")


# 2. Cart Mein Item Dhundhna (index return karta hai, nahi mila toh -1)
def find_in_cart(name):
    for i in range(len(cart)):
        if cart[i][0] == name:
            return i
    return -1


# 3. Subtotal nikalne ke liye
def calculate_subtotal():
    subtotal = 0
    for food in cart:
        item = food[0]
        quantity = food[1]
        price = menu[item]
        subtotal = subtotal + (price * quantity)
    return subtotal


# 4. Item add karna (validation aur duplicate check ke saath)
def add_item():
    show_menu()
    item = input("\nEnter food item name: ").strip().title()

    # Item ki availability check karna
    if item not in menu:
        print("Sorry! This item is not available.")
        return

    # Item ki quantity check karna
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Please enter quantity in numbers.")
        return

    # Check karna ki item pehle se cart mein hai ya nahi
    index = find_in_cart(item)
    if index != -1:
        cart[index][1] += quantity  # Purani quantity mein add kar diya
    else:
        cart.append([item, quantity])

    print(f"{item} (x{quantity}) added to cart successfully!")


# 5. Item hatana
def remove_item():
    if not cart:
        print("Your cart is already empty.")
        return

    item = input("Enter item name to remove: ").strip().title()

    for food in cart:
        if food[0] == item:
            cart.remove(food)
            print(f"{item} removed successfully.")
            return

    print("Item not found in cart.")


# 6. Coupon lagana (10% discount)
def apply_coupon():
    global discount_applied
    code = input("Enter coupon code: ").strip().upper()
    if code == "SAVE10":
        discount_applied = True
        print("Coupon applied! 10% discount will be added at checkout.")
    else:
        print("Invalid coupon code. Only SAVE10 is accepted.")


# 7. Item Search karna (Price ke saath)
def search_item():
    name = input("Enter item name to search: ").strip().lower()
    if not name:
        print("Please enter a valid item name.")
        return

    found = False
    for item in menu:
        if name in item.lower():
            print(f"{item} - Rs. {menu[item]}")
            found = True

    if not found:
        print("Item not found.")


# 8. Checkout (Billing ka main part)
def checkout():
    global discount_applied

    # Step 1: Check karna ki cart khali toh nahi hai
    if not cart:
        print("Your cart is empty! Please add items before checkout.")
        return

    # Step 2: Subtotal calculate karna (Yahan () lagaya gaya hai)
    subtotal = calculate_subtotal()

    # Step 3: Discount calculate karna (10% agar SAVE10 laga hai)
    if discount_applied:
        discount = subtotal * 0.10
        discount_text = f"Discount (10%): {discount:.2f}"
    else:
        discount = 0.00
        discount_text = f"Discount: {discount:.2f}"

    # Discount ke baad bacha hua amount
    amount_after_discount = subtotal - discount

    # Step 4: GST (5% of amount after discount)
    gst = amount_after_discount * 0.05

    # Step 5: Delivery Charge (Free agar subtotal >= 300, warna 40)
    if subtotal >= 300:
        delivery = 0
        delivery_text = "0 (free)"
    else:
        delivery = 40
        delivery_text = "40"

    # Step 6: Final Total nikalna
    total = amount_after_discount + gst + delivery

    # Step 7: Bill print karna
    print("\n--- FINAL BILL ---")
    print(f"Subtotal: {subtotal:.2f} | {discount_text}")
    print(f"GST (5%): {gst:.2f} | Delivery: {delivery_text}")
    print(f"Total: {total:.2f}")

    # Order complete hone ke baad cart aur discount reset karna
    cart.clear()
    discount_applied = False


# 9. Main Menu Loop
while True:
    print("\n=== FOOD ORDERING SYSTEM ===")
    print("1. Show Menu")
    print("2. Search Item")
    print("3. Add Item to Cart")
    print("4. Remove Item from Cart")
    print("5. Apply Coupon")
    print("6. Checkout")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        show_menu()
    elif choice == "2":
        search_item()
    elif choice == "3":
        add_item()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        apply_coupon()
    elif choice == "6":
        checkout()
    elif choice == "7":
        print("Thank you for visiting! Goodbye.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
