print("Welcome to the Launch Console!")
name = input("Enter your name here: ")
print(f"Welcome, {name}!")
menu = (
    "About me",
    "My goals",
    "Fun fact",
    "Exit"
)

def print_menu():
    print("Here are your options:")
    for index, item in enumerate(menu):
        print(f"{index + 1}: {item}")

while True:
    print_menu()
    choice = int(input("Pick a number(1-4): "))
    if choice == 1:
        print("My name is Mason and I am a junior at Hendrickson High school.")
    elif choice == 2:
        print("This year, I want to focus on getting better at using journaling.")
    elif choice == 3:
        print("This year is my fourth year of using Computer Aided Design(CAD)!")
    elif choice == 4:
        print("You've choosen to exit the program.")
        break
    else:
        print("Invalid input. Please try again.")

print("Goodbye.")