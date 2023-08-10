import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def create_card(): 
    card = []
    for suit in SUITS:
        for rank in RANKS:
            card.append((suit, rank))
    return card

def get_hand(cards, size_hand):
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