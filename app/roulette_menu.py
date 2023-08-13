from roulette import generate_roulette, spin_roulette, is_red, is_black, is_zero, choice_number

# Function to display the roulette game menu and handle user input
def roulette_menu():
    print("1. Play is_red")
    print("2. Play is_black")
    print("3. Play is_zero")
    print("4. Choose a number")

    # Get user's choice
    choice = int(input("Choose an option: "))

    # Check user's choice and perform corresponding action
    if choice == 1:
        # Generate the roulette and spin it
        roulette = generate_roulette()
        roulette_number = spin_roulette(roulette)
        
        # Check if the spun number is red
        is_red(roulette_number)

    elif choice == 2:
        # Generate the roulette and spin it
        roulette = generate_roulette()
        roulette_number = spin_roulette(roulette)
        
        # Check if the spun number is black
        is_black(roulette_number)
        
    elif choice == 3:
        # Generate the roulette and spin it
        roulette = generate_roulette()
        roulette_number = spin_roulette(roulette)
        
        # Check if the spun number is zero
        is_zero(roulette_number)
        
    elif choice == 4:
        # Get user's chosen number
        user_number = int(input("Choose a number between 0 and 36: "))
        
        # Generate the roulette and spin it
        roulette = generate_roulette()
        roulette_number = spin_roulette(roulette)
        
        # Check if the user's chosen number matches the spun number
        choice_number(user_number, roulette_number)
    else:
        print("Invalid choice")
