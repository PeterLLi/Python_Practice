class Deck:
    def __init__(self):
        self.deck = []
        self.cards_dealt = 0

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
