import itertools


class Cards:
    suits = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
    ranks = ('Ace', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

    def __init__(self):
        self.my_deck = []
        self.init_deck()

    def init_deck(self):
        self.my_deck = list(itertools.product(Cards.ranks, Cards.suits))
