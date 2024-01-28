def main():
    # Gather information from the user
    pizza_count = get_pizza_count()
    delivery_needed = get_delivery_choice()
    tuesday_discount = get_tuesday_discount()
    app_used = get_app_usage()

    # Calculate pizza cost
    pizza_cost = calculate_pizza_cost(pizza_count, tuesday_discount)

    # Calculate delivery cost
    delivery_cost = calculate_delivery_cost(delivery_needed, pizza_count)

    # Calculate total price
    total_price = pizza_cost + delivery_cost

    # Apply app discount if applicable
    total_price = apply_app_discount(total_price, app_used)

    # Display the final price
    display_final_price(total_price)

# Define functions for calculation and input validation
def get_pizza_count():
    # Get the number of pizzas ordered from the user
    print("_____________________________")
    print("_____________________________")
    print("WELCOME TO BECKETT PLAZE PIZZA")
    print("______________________________")
    print("______________________________")
    while True:
        try:
            count = int(input("How many pizzas ordered?--->  "))
            if count > 0:
                return count
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_delivery_choice():
    # Get the user's choice for delivery
    while True:
        choice = input("Is delivery required? (Y/N)---> ").upper()
        if choice in ["Y", "N"]:
            return choice == "Y"
        else:
            print("Please answer 'Y' or 'N'.")

def get_tuesday_discount():
    # Check if it's Tuesday and apply a discount accordingly
    while True:
        choice = input("Is it Tuesday? (Y/N)--->").upper()
        if choice in ["Y", "N"]:
            return choice == "Y"
        else:
            print("Please answer 'Y' or 'N'.")

def get_app_usage():
    # Check if the customer used the app for a discount
    while True:
        choice = input("Did the customer use the app? (Y/N)---> ").upper()
        if choice in ["Y", "N"]:
            return choice == "Y"
        else:
            print("Please answer 'Y' or 'N'.")

def calculate_pizza_cost(pizza_count, tuesday_discount):
    # Calculate the cost of pizzas with an optional Tuesday discount
    individual_pizza_cost = 12
    pizza_subtotal = pizza_count * individual_pizza_cost
    if tuesday_discount:
        # Apply a 50% discount on Tuesdays
        pizza_subtotal *= 0.5
    return pizza_subtotal

def calculate_delivery_cost(delivery_needed, pizza_count):
    # Calculate the delivery cost based on user choices
    delivery_charge = 2.50
    if not delivery_needed or pizza_count >= 5:
        # No delivery charge if pizzas are picked up or if 5 or more pizzas are ordered
        return 0
    else:
        return delivery_charge

def apply_app_discount(total_price, app_used):
    # Apply a 25% discount if the customer used the app
    if app_used:
        return total_price * 0.75
    else:
        return total_price

def display_final_price(total_price):
    # Display the final total price
    print("Total Price: £{:.2f}".format(total_price))

# Execute the main function
main()

