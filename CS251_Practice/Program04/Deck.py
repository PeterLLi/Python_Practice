import itertools
import random


class Deck:
    suits = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
    ranks = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

    def __init__(self):
        self.deck = []
        self.cards_dealt = 0
        self._init_deck()
        self._shuffle_deck()

    def _init_deck(self):
        self.deck = list(itertools.product(Deck.ranks, Deck.suits))

    def _shuffle_deck(self):
        random.shuffle(self.deck)

    def get_cards_dealt(self):
        return self.cards_dealt

    def _set_cards_dealt(self, cards_dealt):
        self.cards_dealt = cards_dealt

    def is_empty_deck(self):
        if not self.deck:
            return True
        else:
            return False

    def collect_all_cards(self):
        self.cards_dealt = 0

    def deal_card(self):
        if self.is_empty_deck() is False:
            print(self.is_empty_deck())
            card = str(self.deck[0][0]) + ' of ' + str(self.deck[0][1])
            self.deck = self.deck[1:]
            return card
        else:
            return None
