import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def create_card(): 
    card = []
    for suit in SUITS:
        for rank in RANKS:
            card.append((suit, rank))
    return card

def get_hand(cards, size_hand=2):
    hand = random.sample(cards, size_hand )
    return hand

def card_value(card):
    value = card[1]
    if value in ['J', 'Q', 'K']:
        return 10
    elif value == 'as':
        return 11
    else:
        return int(value)
    
def calculate_hand_sum(hand):
    total = sum(card_value(card) for card in hand)
    # Adjust the value of Ace if needed (to avoid exceeding 21)
    for card in hand:
        if card[1] == 'as' and total > 21:
            total -= 10
    return total

def crupier_hand(cards):
    hand = []
    while calculate_hand_sum(hand) < 17:   #Rule in the casinos: the crupier takes cards to 17 o more
        hand.append(random.choice(cards))
    return hand

def blackjack():
    cards = create_card()

    player_cards = get_hand(cards)
    crupier_cards = crupier_hand(cards)

    print("Your initial two cards:")
    for card in player_cards:
        print(f"{card[1]} of {card[0]}")
    print(f"Sum: {calculate_hand_sum(player_cards)}\n")

    print("Crupier's face-up card:")
    print(f"{crupier_cards[0][1]} of {crupier_cards[0][0]}\n")

    # Crupier's turn
    while calculate_hand_sum(crupier_cards) < 17:
        new_card = random.choice(cards)
        crupier_cards.append(new_card)

    print("Crupier's final hand:")
    for card in crupier_cards:
        print(f"{card[1]} of {card[0]}")
    print(f"Sum: {calculate_hand_sum(crupier_cards)}\n")

blackjack()
