import Program02_Deck


class Driver:
    program = Program02_Deck.MyDeck()
    print(program.empty_deck())
    program.init_deck()
    # program.printer()
    program.deal_card()
