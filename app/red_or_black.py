import random

# Define the suits and ranks for the card deck
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Function to create a deck of cards
def create_cards(): 
    card = []
    for suit in SUITS:
        for rank in RANKS:
            card.append((suit, rank))
    return card
    
# Function to get a card from the deck
def get_card(cards, size_hand=1):
    card = random.sample(cards, size_hand)
    print(card)
    return card

# Function to evaluate if a card is red
def is_red(card):
    for i in card:
        if "Hearts" in i or "Clubs" in i:
            return True
        else:
            return False
        
# Function to evaluate if a card is black
def is_black(card):
    for i in card:
        if "Diamonds" in i or "Spades" in i:
            return True
        else:
            return False
        
def red_black_main():
    while True:
        choice = input("Do you want to play? (yes/no): ").lower()
        
        if choice == "yes":
            cards = create_cards()
            card = get_card(cards)
            
            if is_red(card):
                print("The card is red!")
            else:
                print("The card is black!")
        elif choice == "no":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
