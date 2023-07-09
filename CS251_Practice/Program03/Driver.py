import Cards


class Driver:
    program = Cards.Cards()
    program.to_string()
    program.draw_card()
    card = program.draw_card()
    print("First card: " + card)
    cloned_card = program.clone(card)
    card = program.draw_card()
    print("Second card: " + card)

    print(program.equals(cloned_card))
