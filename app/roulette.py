import random

# Function to generate a list representing a roulette with numbers 0 to 36
def generate_roulette():
    return list(range(0, 36 + 1))

# Function to simulate spinning the roulette and return the spun number
def spin_roulette(roulette_list):
    number = random.choice(roulette_list)
    return number

# Function to check if the spun roulette number is red
def is_red(roulette_number):
    print("The roulette number is", roulette_number)
    if roulette_number % 2 != 0:
        print("The number in the roulette is red, you win!")
    else:
        print("The number in the roulette isn't red, you lose")

# Function to check if the spun roulette number is black
def is_black(roulette_number):
    print("The roulette number is", roulette_number)
    if roulette_number % 2 == 0:
        print("The number in the roulette is black")

# Function to check if the spun roulette number is zero
def is_zero(roulette_number):
    print("The roulette number is", roulette_number)
    if roulette_number == 0:
        print("The number in the roulette is 0 you win ")
    elif roulette_number != 0:
        print("The number in the roulette isn't 0 you lose ")

# Function to check if the user's chosen number matches the spun roulette number
def choice_number(number, roulette_number):
    print(f'The number in the roulette is {roulette_number}')
    if number == roulette_number:
        print("The number in the roulette is the same as the one you chose, you win!")
    elif number != roulette_number:
        print("The number in the roulette isn't the same as the one you chose, you lose!")


# Function to display the roulette game menu and handle user input
def roulette_menu():
    while True:
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
