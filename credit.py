from common import cls, Printing, print_back_to_menu


def credit():
    cls()
    creditsy = Printing([30, 50], 81, 'Who made this game')
    creditsy.print_title()
    creditsy.print_row(['Author name', 'Email'], header=True)
    authors = [['Kamil Brodziak', 'Kamil98Brodziak@gmail.com'], ['Andrzej Rzeszut', '']]
    for author in authors:
        creditsy.print_row(author)
    print("\n\n\n *This game was made in 4 days.")
    print("**New menu design, new highscores design and credits in 5th day.\n")
    print("Arrows - movement, i - inventory, e - in inventory pressed show equiped items.")
    print("Enter - in inventory equip, c - character statistics.\n")
    print("Always check hunger, if it is < 1 you die. If you lose battle - you die.")
    print("You must collect key from boss to launch minigame, which winning is necessary to enter next level.")
    print("Score: after winning battle + mob hp, after winning mini game +1000, after losing mini game -100.")
    print("Some cheats are implemented, but don't cheat!")
    print_back_to_menu()
