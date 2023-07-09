import Cards


class Driver:
    program = Cards.Cards()
    program.to_string()
    program.draw_card()
    card = program.draw_card()
    print("You drew: " + card)
    cloned_card = program.clone(card)
    print("Cloned card:  " + cloned_card)
    print(program.equals(cloned_card))
