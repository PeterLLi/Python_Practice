class MyDeck:
    def __init__(self):
        self.deck = []

    def fill_deck(self):
        for i in range(52):
            self.deck[i] = True

    def printer(self):
        for i in range(len(self.deck)):
            print(self.deck[i])

