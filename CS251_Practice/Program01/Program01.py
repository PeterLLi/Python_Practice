import itertools
import random


class Cards:
    max_display_length = 7

    def __init__(self):
        self.deck = []
        self.card_attributes = []
        self.card = ''
        self.fill_deck()

    def fill_deck(self):
        updated_deck = []
        self.deck = list(itertools.product(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], ['S', 'C', 'D', 'H']))
        # self.deck = list(itertools.product(range(1, 13), ['S', 'C', 'D', 'H']))
        for i in range(len(self.deck)):
            self.card_attributes = list(self.deck[i])
            for j in range(len(self.card_attributes)):
                self.card += (str(self.card_attributes[j]))
            updated_deck.append(self.card)
            self.card = ''
        self.deck = updated_deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck_formatted(self):
        counter = 0
        for i in range(len(self.deck)):
            if counter < Cards.max_display_length:
                print(self.deck[i] + " ", end="")
                counter += 1
            else:
                print(self.deck[i] + " ")
                counter = 0
