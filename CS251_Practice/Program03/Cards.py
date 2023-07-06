import itertools
import random


class Cards:
    suits = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
    ranks = ('Ace', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

    def __init__(self):
        self.my_deck = []
        self.init_deck()
        self._shuffle_deck()

    def init_deck(self):
        self.my_deck = list(itertools.product(Cards.ranks, Cards.suits))

    def to_string(self):
        for i in range(len(self.my_deck)):
            print(str(self.my_deck[i][0]) + ' of ' + str(self.my_deck[i][1]))

    def _shuffle_deck(self):
        random.shuffle(self.my_deck)