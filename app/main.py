from blackjack import blackjack

def menu():
    print("*** WELCOME TO CESAR PALACE CASINO ***")
    print("¿What do you wanna play now?")
    print("1. - Blackjack")
    

    choice = input("Choice an option -> ")
    return choice

while True:
    choice = menu()

    if choice == "1":
        blackjack()
    else:
        print("Select a valid option")