import Cards


class Driver:
    program = Cards.Cards()
    program.to_string()
    program.draw_card()
    card = program.draw_card()
    print("You drew: " + card)
    new_card = program.clone(card)
    print("Cloned card:  " + new_card)
