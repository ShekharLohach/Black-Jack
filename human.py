import random
from itertools import permutations, repeat
# class Deck():

cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
# cards_colors=['Red', 'Black']
cards_suits=['Hearts', 'Diamond', 'Spades', 'Club']
all_cards=['A of Hearts','A of Diamond','A of Spades','A of Club','1 of Hearts','1 of Diamond','1 of Spades',
    '1 of Club', '2 of Hearts','2 of Diamond','2 of Spades','2 of Club','3 of Hearts','3 of Diamond','3 of Spades',
    '3 of Club', '4 of Hearts','4 of Diamond','4 of Spades','4 of Club','5 of Hearts','5 of Diamond','5 of Spades',
    '5 of Club', '6 of Hearts','6 of Diamond','6 of Spadesv','6 of Club','7 of Hearts','7 of Diamond','7 of Spades',
    '7 of Club', '8 of Hearts','8 of Diamond','8 of Spades','8 of Club','9 of Hearts','9 of Diamond','9 of Spades',
    '9 of Club', '10 of Hearts','10 of Diamond','10 of Spades','10 of Club','J of Hearts','J of Diamond','J of Spades',
    'J of Club', 'K of Hearts','K of Diamond','K of Spades','K of Club','Q of Hearts','Q of Diamond','Q of Spades',
    'Q of Club',
]


# print((random.choice(all_cards)))
class Deck():

    def __init__(self):
        pass

