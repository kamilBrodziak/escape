import time
import sys
from .list_containing_capital_transformations import *
from .printing import printing_hangman, cls, display_hint, used_letter_before
from .printing import display_test_hint, printing_hint_and_capital


def game_start(hint):
    cls()
    with open('games/hangman/ascii/logo.txt') as logo:
        print(logo.read())
        time.sleep(2)
    with open('games/hangman/countries_and_capitals.txt') as countries:
        capitals = countries.readlines()
    cou_cap = change_random_line_into_list(capitals)
    win = ""
    life = 6
    used_letters = []
    capital_display_on_screen = [" ___"] * len(cou_cap[1])
    capital_guessed_template = change_capital_word_into_capital_guessed_template(cou_cap[1])
    delete_spaces_in_capital_display_on_screen(cou_cap[1], capital_display_on_screen)
    cls()
    while life > 0:
        cls()
        printing_hangman(life, used_letters)
        printing_hint_and_capital(capital_display_on_screen, cou_cap, life, hint)
        life, win = make_guess(
                    life, cou_cap[1], capital_display_on_screen, used_letters)
        if capital_guessed_template == capital_display_on_screen or win == "won":
            break
    cls()
    printing_hangman(life, used_letters)
    time.sleep(1)
    win = False if life < 1 else True
    return win


def make_guess(life, capital, capital_display_on_screen, used_letters):
    while True:
        answer = input("Give me your answer: ").upper()
        if not answer.isalpha() and len(answer) < 2:
            continue
        if answer in capital_display_on_screen or answer in used_letters:
            used_letter_before()
            continue
        if len(answer) > 1:
            if answer == capital:
                return life, "won"
            else:
                return life - 2, ""
        else:
            if answer in capital and answer not in capital_display_on_screen:
                return add_letter_to_capital_display_on_screen(
                    life, capital_display_on_screen, capital, answer)
            else:
                used_letters.append(answer)
                return life - 1, ""
