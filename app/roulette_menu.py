from roulette import generate_roulette, spin_roulette, is_red, is_black, is_zero, choice_number

def roulette_menu():
    print("1. Play is_red")
    print("2. Play is_black")
    print("3. Play is_zero")
    print("4. Choose a number")

    choice = int(input("Choose an option: "))

    

    if choice == 1:
        is_red(roulette_number)
        roulette = generate_roulette()
        roulette_number = spin_roulette(roulette)
    elif choice == 2:
        is_black(roulette_number)
        roulette = generate_roulette()
        roulette_number = spin_roulette(roulette)
    elif choice == 3:
        is_zero(roulette_number)
        roulette = generate_roulette()
        roulette_number = spin_roulette(roulette)
    elif choice == 4:
        user_number = int(input("Choose a number between 0 and 36: "))
        roulette = generate_roulette()
        roulette_number = spin_roulette(roulette)
        choice_number(user_number, roulette_number)
    else:
        print("Invalid choice")