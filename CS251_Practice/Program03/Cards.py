import copy
import itertools
import random


class Cards:
    suits = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
    ranks = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

    def __init__(self, card=None):
        if card is None:
            card = ('Ace', 'Spades')

        self.my_deck = []
        self.init_deck()
        self.card = card
        self._shuffle_deck()

    def init_deck(self):
        self.my_deck = list(itertools.product(Cards.ranks, Cards.suits))

    def to_string(self):
        print(str(self.card[0] + ' of ' + str(self.card[1])))

    def _shuffle_deck(self):
        random.shuffle(self.my_deck)

    @staticmethod
    def clone(card):
        new_card = copy.deepcopy(card)
        return new_card

    def draw_card(self):
        self.card = str(self.my_deck[0][0]) + ' of ' + str(self.my_deck[0][1])
        self.my_deck = self.my_deck[1:]
        return self.card

    def equals(self, card):
        if card == self.card:
            return True
        else:
            return False
