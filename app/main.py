from blackjack import blackjack
from roulette_menu import roulette_menu
from red_or_black_menu import red_or_black_menu

def menu():
    print("*** WELCOME TO CESAR PALACE CASINO ***")
    print("¿What do you wanna play now?")
    print("1. - Blackjack")
    print("2. - Roulette")
    print("3. - Red or black")
    

    choice = input("Choice an option -> ")
    return choice

while True:
    choice = menu()

    if choice == "1":
        blackjack()
    elif choice == '2':
        roulette_menu()
    elif choice == '3':
        red_or_black_menu()

    else:
        print("Select a valid option")