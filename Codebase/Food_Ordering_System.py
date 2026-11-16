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

# Menu Dikhana 
def show_menu():
    for item in menu:
        print(item, "- Rs.", menu[item])

# Cart Mein Item Dhundhna :
def find_in_cart(name):
    for i in range(len(cart)):
        if cart[i][0] == name:
            return i
    return -1

# Subtotal nikalne k liye :
def calculate_subtotal():

    subtotal = 0

    for food in cart:

        item = food[0]
        quantity = food[1]

        price = menu[item]

        subtotal = subtotal + (price * quantity)

    return subtotal

# Item add karna (validation ke saath):
def add_item():

    show_menu()

    item = input("\nEnter food item name: ").strip().title()

    # Item ki avalibality check krna:
    if item not in menu:
        print("Sorry! This item is not available.")
        return

    # Item ki quantity check karna :
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter quantity in numbers.")
        return

    # Item ko cart me add karna :
    cart.append([item, quantity])

    print(item, "added to cart successfully!")

# Item hatana :

def remove_item():

    item = input("Enter item name to remove: ").strip().title()

    for food in cart:

        if food[0] == item:
            cart.remove(food)
            print(item, "removed successfully.")
            return

    print("Item not found in cart.")

# Coupon lagana or 10% discount: 

def apply_coupon(code):
    global discount_applied
    if code == "SAVE10":
        discount_applied = True
        print("Coupon applied!")
    else:
        print("Invalid coupon code. Only SAVE10 is accepted.")


# Checkout (billing ka main part ):

def checkout():
    # Step 1: Check karna ki cart khali toh nahi hai
    if not cart:
        print("Your cart is empty! Please add items before checkout.")
        return

    # Step 2: Subtotal calculate karna
    subtotal = calculate_subtotal

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

    # Step 7: Bill print karna (Exact Test Case format mein)
    print(f"Subtotal: {subtotal:.2f} | {discount_text}")
    print(f"GST (5%): {gst:.2f} | Delivery: {delivery_text}")
    print(f"Total: {total:.2f}")


# Main Menu loop :  (Program ko baar baar chlana jab tak customer exit select na kare)

def search_item():
    name = input("Enter item name to search: ").lower()
    found = False
    for item in menu:   
        if name in item.lower():
            print(item)
            found = True
    if not found:
        print("Item not found.")