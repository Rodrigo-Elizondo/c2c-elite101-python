print('Hi welcome you out chat room this is our chatbot ')
name = input("What is your name? ")
print("Nice to meet you "+ name)

from datetime import datetime

birthday_YMD = input("Please enter your birthday (YYYY-MM-DD): ")

birthday = datetime.strptime(birthday_YMD, "%Y-%m-%d")

today = datetime.today()

age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

print(f"So you're {age} years old nice, well i hope you are doing well.")


def show_menu():
  print("\nHow can I assist you today? Please choose an option:")
  print("1. Food menu")
  print("2. Drink menu")
  print("3. Frequently Asked Questions")
  print("4. Exit")


def show_food_menu():
  print("\nFood Menu:")
  print("1. Pizza")
  print("2. Burger")
  print("3. Salad")
  print("4. Back to main menu")


def show_drink_menu():
  print("\nDrink Menu:")
  print("1. Water")
  print("2. Soda")
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


def handle_food_choice():
  while True:
    show_food_menu()
    food_choice = get_user_choice()
    if food_choice in ["1", "2", "3"]:
      print(f"You selected {food_choice}. (Placeholder response)")
    elif food_choice == "4":
      break
    else:
      print("Invalid choice. Please select a valid option.")


def handle_drink_choice():
  while True:
    show_drink_menu()
    drink_choice = get_user_choice()
    if drink_choice in ["1", "2", "3"]:
      print(f"You selected {drink_choice}. (Placeholder response)")
    elif drink_choice == "4":
      break
    else:
      print("Invalid choice. Please select a valid option.")


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
    print("Thank you for chatting with me. Goodbye!")
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
