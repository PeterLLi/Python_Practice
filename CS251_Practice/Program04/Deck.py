class Deck:
    def __init__(self):
        self.deck = []
        self.cards_dealt = 0

    def get_cards_dealt(self):
        return self.cards_dealt

    def _set_cards_dealt(self, cards_dealt):
        self.cards_dealt = cards_dealt
