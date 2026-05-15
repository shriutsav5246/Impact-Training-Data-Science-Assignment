import time

ADMIN_PASSWORD = "1234"

MENU = {
    1: {
        "name": "Espresso",
        "base_price": 80,
        "ingredients": {"water": 50, "coffee": 18}
    },
    2: {
        "name": "Americano",
        "base_price": 100,
        "ingredients": {"water": 100, "coffee": 20}
    },
    3: {
        "name": "Latte",
        "base_price": 120,
        "ingredients": {"water": 200, "milk": 150, "coffee": 24}
    },
    4: {
        "name": "Cappuccino",
        "base_price": 150,
        "ingredients": {"water": 250, "milk": 100, "coffee": 24}
    },
    5: {
        "name": "Mocha",
        "base_price": 170,
        "ingredients": {"water": 200, "milk": 120, "coffee": 30}
    },
    6: {
        "name": "Flat White",
        "base_price": 140,
        "ingredients": {"water": 180, "milk": 130, "coffee": 22}
    },
    7: {
        "name": "Macchiato",
        "base_price": 110,
        "ingredients": {"water": 80, "milk": 30, "coffee": 20}
    }
}

resources = {
    "water": 5000,
    "milk": 3000,
    "coffee": 1500,
    "sugar": 1000,
    "whipped_cream": 500,
    "money": 0
}


def pause():
    time.sleep(0.8)


def show_menu():
    print("\n" + "=" * 55)
    print("                WELCOME TO COFFEE MACHINE")
    print("=" * 55)

    for key, coffee in MENU.items():
        print(f"{key}. {coffee['name']:15} ₹{coffee['base_price']}")

    print("-" * 55)
    print("Customer Options:")
    print("cart      -> View Cart")
    print("checkout  -> Pay Now")
    print("clear     -> Clear Cart")
    print("exit      -> Leave Machine")
    print("=" * 55)


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a value greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Numbers only.")


def yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ["yes", "y"]:
            return True
        elif ans in ["no", "n"]:
            return False
        print("Please enter yes or no.")


def customize_drink():
    print("\nCustomize Your Drink")

    while True:
        try:
            sugar = int(input("Sugar spoons (0-3): "))
            if 0 <= sugar <= 3:
                break
            print("Enter between 0 and 3.")
        except ValueError:
            print("Numbers only.")

    extra_shot = yes_no("Extra coffee shot (+₹20)? (yes/no): ")
    extra_milk = yes_no("Extra milk (+₹15)? (yes/no): ")
    whipped_cream = yes_no("Whipped cream (+₹25)? (yes/no): ")

    return {
        "sugar": sugar,
        "extra_shot": extra_shot,
        "extra_milk": extra_milk,
        "whipped_cream": whipped_cream
    }


def calculate_item(drink, quantity, custom):
    base = drink["base_price"]
    ingredients = drink["ingredients"].copy()
    extra_cost = 0

    if custom["sugar"] > 0:
        ingredients["sugar"] = custom["sugar"] * 5
        extra_cost += custom["sugar"] * 5

    if custom["extra_shot"]:
        ingredients["coffee"] = ingredients.get("coffee", 0) + 10
        extra_cost += 20

    if custom["extra_milk"]:
        ingredients["milk"] = ingredients.get("milk", 0) + 50
        extra_cost += 15

    if custom["whipped_cream"]:
        ingredients["whipped_cream"] = 20
        extra_cost += 25

    total_price = (base + extra_cost) * quantity

    scaled_ingredients = {}
    for item, amount in ingredients.items():
        scaled_ingredients[item] = amount * quantity

    return total_price, scaled_ingredients


def add_to_cart(cart, choice):
    drink = MENU[int(choice)]

    quantity = get_positive_integer(f"\nHow many {drink['name']} would you like? ")

    custom = customize_drink()

    price, ingredients = calculate_item(drink, quantity, custom)

    cart.append({
        "drink_name": drink["name"],
        "quantity": quantity,
        "custom": custom,
        "price": price,
        "ingredients": ingredients
    })

    print(f"\n{quantity} x {drink['name']} added to cart successfully.\n")


def view_cart(cart):
    if not cart:
        print("\nYour cart is empty.\n")
        return

    print("\n" + "=" * 55)
    print("                    YOUR CART")
    print("=" * 55)

    total = 0
    for idx, item in enumerate(cart, start=1):
        print(f"{idx}. {item['quantity']} x {item['drink_name']:15} ₹{item['price']}")
        total += item["price"]

    print("-" * 55)
    print(f"TOTAL BILL: ₹{total}")
    print("=" * 55 + "\n")


def clear_cart(cart):
    if not cart:
        print("\nCart already empty.\n")
        return

    cart.clear()
    print("\nCart cleared successfully.\n")


def check_resources(cart):
    required = {}

    for item in cart:
        for ingredient, amount in item["ingredients"].items():
            required[ingredient] = required.get(ingredient, 0) + amount

    for ingredient, needed in required.items():
        available = resources.get(ingredient, 0)
        if available < needed:
            print(
                f"\nSorry. Insufficient {ingredient}. "
                f"Required: {needed}, Available: {available}\n"
            )
            return False

    return True


def deduct_resources(cart):
    for item in cart:
        for ingredient, amount in item["ingredients"].items():
            resources[ingredient] -= amount


def calculate_total(cart):
    return sum(item["price"] for item in cart)


def process_payment(total):
    print(f"\nTotal amount to pay: ₹{total}")
    print("Type 'cancel' to cancel payment.\n")

    inserted = 0

    while inserted < total:
        amount = input("Insert amount: ₹").strip().lower()

        if amount == "cancel":
            print("\nPayment cancelled.\n")
            return False

        try:
            amount = int(amount)

            if amount <= 0:
                print("Enter a valid positive amount.")
                continue

            inserted += amount

            if inserted < total:
                print(f"Inserted: ₹{inserted} | Remaining: ₹{total - inserted}")

        except ValueError:
            print("Invalid amount.")

    if inserted > total:
        print(f"\nChange returned: ₹{inserted - total}")

    resources["money"] += total
    return True


def prepare_order(cart):
    print("\nPreparing your order...\n")

    for item in cart:
        for _ in range(item["quantity"]):
            print(f"Preparing {item['drink_name']}...")
            pause()
            print("Grinding coffee...")
            pause()
            print("Heating ingredients...")
            pause()
            print("Dispensing coffee...")
            pause()
            print(f"{item['drink_name']} ready ☕\n")
            pause()

    print("Order completed. Enjoy your coffee!\n")


def admin_panel():
    password = input("Enter admin password: ")

    if password != ADMIN_PASSWORD:
        print("Access denied.")
        return

    while True:
        print("\n" + "=" * 40)
        print("ADMIN PANEL")
        print("=" * 40)
        print("1. View stock")
        print("2. View earnings")
        print("3. Refill water")
        print("4. Refill milk")
        print("5. Refill coffee")
        print("6. Refill sugar")
        print("7. Refill whipped cream")
        print("8. Reset earnings")
        print("9. Exit admin")

        choice = input("Select option: ")

        if choice == "1":
            print("\nCurrent Stock:")
            for key, value in resources.items():
                if key != "money":
                    print(f"{key.capitalize()}: {value}")

        elif choice == "2":
            print(f"\nTotal earnings: ₹{resources['money']}")

        elif choice == "3":
            resources["water"] += get_positive_integer("Add water (ml): ")

        elif choice == "4":
            resources["milk"] += get_positive_integer("Add milk (ml): ")

        elif choice == "5":
            resources["coffee"] += get_positive_integer("Add coffee (g): ")

        elif choice == "6":
            resources["sugar"] += get_positive_integer("Add sugar (g): ")

        elif choice == "7":
            resources["whipped_cream"] += get_positive_integer("Add whipped cream (g): ")

        elif choice == "8":
            resources["money"] = 0
            print("Earnings reset.")

        elif choice == "9":
            break

        else:
            print("Invalid option.")


def checkout(cart):
    if not cart:
        print("\nYour cart is empty.\n")
        return

    view_cart(cart)

    if not check_resources(cart):
        return

    total = calculate_total(cart)

    if process_payment(total):
        deduct_resources(cart)
        prepare_order(cart)
        cart.clear()


def main():
    cart = []

    while True:
        show_menu()

        choice = input(
            "\nSelect coffee (1-7) or option (cart/checkout/clear/exit): "
        ).strip().lower()

        if choice == "exit":
            print("\nThank you for visiting. Goodbye!")
            break

        elif choice == "cart":
            view_cart(cart)

        elif choice == "checkout":
            checkout(cart)

        elif choice == "clear":
            clear_cart(cart)

        elif choice == "/admin":
            admin_panel()

        elif choice.isdigit() and int(choice) in MENU:
            add_to_cart(cart, choice)

        else:
            print("\nInvalid selection. Please try again.\n")


if __name__ == "__main__":
    main()