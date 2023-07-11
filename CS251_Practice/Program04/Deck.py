import itertools


class Deck:
    suits = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
    ranks = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

    def __init__(self):
        self.deck = []
        self.cards_dealt = 0
        self._init_deck()

    def _init_deck(self):
        self.deck = list(itertools.product(Deck.ranks, Deck.suits))

    def get_cards_dealt(self):
        return self.cards_dealt

    def _set_cards_dealt(self, cards_dealt):
        self.cards_dealt = cards_dealt

    def is_empty_deck(self):
        if not self.deck:
            print("Empty")
            return True
        else:
            print("Not empty")
            return False

    def collect_all_cards(self):
        self.cards_dealt = 0

    def deal_card(self):
