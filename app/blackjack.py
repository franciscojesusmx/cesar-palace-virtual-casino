import random

# Define the suits and ranks for the card deck
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Function to create a deck of cards
def create_card(): 
    card = []
    for suit in SUITS:
        for rank in RANKS:
            card.append((suit, rank))
    return card

# Function to get a hand of cards
def get_hand(cards, size_hand=2):
    hand = random.sample(cards, size_hand)
    return hand

# Function to determine the value of a card
def card_value(card):
    value = card[1]
    if value in ['J', 'Q', 'K']:
        return 10
    elif value == 'as':
        return 11
    else:
        return int(value)
    
# Function to calculate the sum of a hand
def calculate_hand_sum(hand):
    total = sum(card_value(card) for card in hand)
    # Adjust the value of Ace if needed (to avoid exceeding 21)
    for card in hand:
        if card[1] == 'as' and total > 21:
            total -= 10
    return total

# Function for the crupier's behavior to get a hand of cards
def crupier_hand(cards):
    hand = []
    while calculate_hand_sum(hand) < 17:   # Rule in the casinos: the crupier takes cards to 17 or more
        hand.append(random.choice(cards))
    return hand

# Function to display a player's or crupier's cards
def display_cards(cards, title):
    print(f"{title} Cards:")
    for card in cards:
        print(f"{card[1]} of {card[0]}")
    print("")

# Function to handle a user's decision to take additional cards
def user_hit(cards, deck):
    while True:
        choice = input("Do you want another card? (yes/no): ")
        if choice.lower() == 'yes':
            new_card = random.choice(deck)
            cards.append(new_card)
            display_cards(cards, "Your")
            if calculate_hand_sum(cards) > 21:
                print("Bust! Your hand value is over 21.")
                break
        else:
            break

# Main function to simulate the blackjack game
def blackjack():
    cards = create_card()

    player_cards = get_hand(cards)
    crupier_cards = crupier_hand(cards)

    print("Your initial two cards:")
    display_cards(player_cards, "Your")
    print(f"Sum: {calculate_hand_sum(player_cards)}\n")

    print("Crupier's face-up card:")
    print(f"{crupier_cards[0][1]} of {crupier_cards[0][0]}\n")

    user_hit(player_cards, cards)  # Allow the user to take additional cards

    print("Crupier's turn")
    while calculate_hand_sum(crupier_cards) < 17:
        new_card = random.choice(cards)
        crupier_cards.append(new_card)

    print("Crupier's final hand:")
    display_cards(crupier_cards, "Crupier")
    print(f"Sum: {calculate_hand_sum(crupier_cards)}\n")


