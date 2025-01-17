print('Hi welcome to our chat room, this is our chatbot.')
name = input("What is your name? ")
print("Nice to meet you, " + name)

from datetime import datetime

birthday_YMD = input("Please enter your birthday (YYYY-MM-DD): ")
birthday = datetime.strptime(birthday_YMD, "%Y-%m-%d")
today = datetime.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
print(f"So you're {age} years old, nice. I hope you are doing well.")

def show_menu():
    print("\nHow can I assist you today? Please choose an option:")
    print("1. Food menu")
    print("2. Drink menu")
    print("3. Frequently Asked Questions")
    print("4. Exit")

def show_food_menu():
    print("\nFood Menu:")
    print("1. Main Course")
    print("2. Side Dishes")
    print("3. Back to main menu")

def show_main_course_menu():
    print("\nMain Course Menu:")
    print("1. Pizza")
    print("2. Burger")
    print("3. Wings")
    print("4. Back to Food Menu")

def show_side_dishes_menu():
    print("\nSide Dishes Menu:")
    print("1. Fries")
    print("2. Salad")
    print("3. Garlic Bread")
    print("4. Back to Food Menu")

def show_drink_menu():
    print("\nDrink Menu:")
    print("1. Soda")
    print("2. Water")
    print("3. Coffee")
    print("4. Back to main menu")

def show_faq():
    print("\nFrequently Asked Questions:")
    print("1. What are your opening hours?")
    print("2. Where are you located?")
    print("3. How can I contact customer support?")
    print("4. Back to main menu")

def get_user_choice():
    choice = input("Enter the number of your choice: ")
    return choice

def handle_main_course_choice():
    while True:
        show_main_course_menu()
        main_course_choice = get_user_choice()
        if main_course_choice in ["1", "2", "3"]:
            print(f"You selected {main_course_choice}. (Placeholder response)")
        elif main_course_choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def handle_side_dishes_choice():
    while True:
        show_side_dishes_menu()
        side_dish_choice = get_user_choice()
        if side_dish_choice in ["1", "2", "3"]:
            print(f"You selected {side_dish_choice}. (Placeholder response)")
        elif side_dish_choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def handle_food_choice():
    while True:
        show_food_menu()
        food_choice = get_user_choice()
        if food_choice == "1":
            handle_main_course_choice()
        elif food_choice == "2":
            handle_side_dishes_choice()
        elif food_choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def handle_drink_choice():
    while True:
        show_drink_menu()
        drink_choice = get_user_choice()

        if drink_choice == "1":
            handle_soda_choice()
        elif drink_choice == "2":
            display_sizes_and_prices("Water", {"Small": 1.00, "Medium": 1.50, "Large": 2.00})
        elif drink_choice == "3":
            display_sizes_and_prices("Coffee", {"Small": 2.00, "Medium": 2.50, "Large": 3.00})
        elif drink_choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def handle_soda_choice():
    sodas = {
        "1": {"name": "Coke", "prices": {"Small": 1.50, "Medium": 2.00, "Large": 2.50}},
        "2": {"name": "Pepsi", "prices": {"Small": 1.50, "Medium": 2.00, "Large": 2.50}},
        "3": {"name": "Sprite", "prices": {"Small": 1.50, "Medium": 2.00, "Large": 2.50}},
        "4": {"name": "Fanta", "prices": {"Small": 1.50, "Medium": 2.00, "Large": 2.50}},
        "5": "Back to Drink Menu"
    }

    while True:
        print("\nSoda Menu:")
        for key, value in sodas.items():
            if key == "5":
                print(f"{key}. {value}")
            else:
                print(f"{key}. {value['name']}")

        soda_choice = get_user_choice()

        if soda_choice in sodas and soda_choice != "5":
            soda = sodas[soda_choice]
            display_sizes_and_prices(soda['name'], soda['prices'])
        elif soda_choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def display_sizes_and_prices(drink_name, prices):
    print(f"\nYou selected {drink_name}.")
    print("Available sizes and prices:")
    for size, price in prices.items():
        print(f"{size}: ${price:.2f}")

    size_choice = input("Please select a size (Small, Medium, Large): ").capitalize()
    if size_choice in prices:
        print(f"You have selected a {size_choice} {drink_name} for ${prices[size_choice]:.2f}.")
    else:
        print("Invalid size choice. Please try again.")

def handle_faq_choice():
    while True:
        show_faq()
        faq_choice = get_user_choice()
        if faq_choice == "1":
            print("Our opening hours are from 9:00 AM to 9:00 PM, Monday to Sunday.")
        elif faq_choice == "2":
            print("We are located in the central Austin area.")
        elif faq_choice == "3":
            print("You can contact customer support by calling 1-234-567-8910 or emailing support@examplestore.com.")
        elif faq_choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def handle_choice(choice):
    if choice == "1":
        handle_food_choice()
    elif choice == "2":
        handle_drink_choice()
    elif choice == "3":
        handle_faq_choice()
    elif choice == "4":
        print("Thank you for chatting with me i hope i was able to help. Goodbye!")
        return False
    else:
        print("Invalid choice. Please select a valid option.")
    return True

def main():
    keep_running = True
    while keep_running:
        show_menu()
        user_choice = get_user_choice()
        keep_running = handle_choice(user_choice)

if __name__ == "__main__":
    main()
