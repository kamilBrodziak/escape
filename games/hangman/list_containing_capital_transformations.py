def change_random_line_into_list(unsplited_list):
    import random
    element = random.choice(unsplited_list)
    splited_list_element = element.split(' | ', )
    splited_list_element[1] = splited_list_element[1][:-1].upper()
    return splited_list_element


def change_capital_word_into_capital_guessed_template(capital):
    capital_hidden_template = []
    for char in capital:
        capital_hidden_template.append(" " + char + "  ")
    return capital_hidden_template


def delete_spaces_in_capital_display_on_screen(capital, capital_display_on_screen):
    x = " "
    if x in capital and x not in capital_display_on_screen:
        j = 0
        for char in capital:
            if char == " ":
                capital_display_on_screen[j] = "    "
            j += 1


def add_letter_to_capital_display_on_screen(life, capital_display_on_screen, capital, answer):
    j = 0
    for char in capital:
        if char == answer:
            capital_display_on_screen[j] = " " + answer + "  "
        j += 1
    return life, ""
