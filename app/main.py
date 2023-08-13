from blackjack import blackjack
from roulette_menu import roulette_menu

def menu():
    print("*** WELCOME TO CESAR PALACE CASINO ***")
    print("¿What do you wanna play now?")
    print("1. - Blackjack")
    print("2. - Roulette")
    

    choice = input("Choice an option -> ")
    return choice

while True:
    choice = menu()

    if choice == "1":
        blackjack()
    elif choice == '2':
        roulette_menu()
    else:
        print("Select a valid option")