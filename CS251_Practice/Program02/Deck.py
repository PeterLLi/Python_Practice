class MyDeck:
    def __init__(self):
        self.deck = []

    def fill_deck(self):
        self.deck = [True for i in range(52)]

    def printer(self):
        for i in range(len(self.deck)):
            print(i)
