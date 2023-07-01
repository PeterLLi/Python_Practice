import itertools
import random


class MyDeck:
    available_cards = list(range(0, 51))
    my_deck = list(itertools.product(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], ['S', 'C', 'D', 'H']))

    @staticmethod
    def _corrected_deck():
        updated_deck = []
        card = ''
        for i in range(len(MyDeck.my_deck)):
            card_attributes = list(MyDeck.my_deck[i])
            for j in range(len(card_attributes)):
                card += str(card_attributes[j])
            updated_deck.append(card)
            card = ''
        MyDeck.my_deck = updated_deck

    @staticmethod
    def card_to_string(card):
        print(MyDeck.my_deck[card])
        return MyDeck.my_deck[card]

    def __init__(self, deck=None):
        self.deck = deck or []
        MyDeck._corrected_deck()

    def init_deck(self):
        if self.deck is None:
            self.deck = []

        for i in range(52):
            self.deck.append(True)

    def empty_deck(self):
        if self.deck is None or self.deck == []:
            return True
        else:
            return False

    def deal_card(self):
        random.shuffle(MyDeck.available_cards)
        card = MyDeck.available_cards.pop(0)
        self.deck[card] = False
        print(MyDeck.my_deck[card])

    def printer(self):
        for i in range(len(self.deck)):
            print(self.deck[i])

