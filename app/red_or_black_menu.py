# Import everything from the module 'red_or_black'
from red_or_black import *

# Function to display the red or black menu and handle user input
def red_or_black_menu():
    print("1. The next card is black")
    print("2. The next card is Red")

    # Get user's choice
    choice = int(input("Choose an option: "))

    # Check user's choice
    if choice == 1:
        # Create a deck of cards
        cards = create_cards()
        
        # Get a card from the deck
        get_card(cards)
        
        # Check if the card is red
        if is_red == True:
            print("You win!")
        else:
            print("You lose!")
    elif choice == 2:
        # Create a deck of cards
        cards = create_cards()
        
        # Get a card from the deck
        get_card(cards)
        
        # Check if the card is red
        if is_red == True:
            print("You win!")
        else:
            print("You lose!")

# Call the red_or_black_menu function to start the game
red_or_black_menu()
