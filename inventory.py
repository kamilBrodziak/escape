import os
import sys
import random
from common import getChar, cls
from termcolor import cprint
from math import ceil


class Inv:
    def __init__(self, items_per_page, equiped):
        self.inventory = {}
        # {'id': ["Name", "Desc", "what_it_is", "how_much_change", "amount"]}
        self.equiped = equiped  # list of ids
        self.amount_pos = 4
        self.items_per_page = items_per_page
        self.display_inv = DisplayInv(self.inventory, self.items_per_page)

    def add_to_inv(self, filename, how_much):
        with open(filename) as filename:
            items = filename.readlines()
        for i in range(how_much):
            item = random.choice(items)
            item = item[:-1].split(";")
            if item[0] in self.inventory.keys():
                self.inventory[item[0]][self.amount_pos] += 1
            else:
                self.inventory[item[0]] = item[1:]
                self.inventory[item[0]].extend([1])  # item[0] - id, so we must skip this by item[1:]
        self.display_inv.change_inv(self.inventory)

    def run_inv(self):
        char = ""
        actual_pos = 0
        actual_page = 1
        max_page = ceil(len(self.inventory) / self.items_per_page)
        if max_page == 0:
            max_page = 1
        while char.lower() != 'i':
            self.display_inv.print_table(actual_pos, actual_page, max_page)
            char = getChar(1)
            if char == '\x1b':
                actual_pos, actual_page = self.arrows_move(actual_pos, actual_page, max_page)
            # elif char == '\n':
            #     self.equip(self.inventory[actual_pos])

    def arrows_move(self, actual_pos, actual_page, max_page):
        char = getChar(2)
        if char == '[A' and actual_pos > (actual_page-1) * self.items_per_page:
            actual_pos -= 1
        elif char == '[B' and actual_pos < actual_page * self.items_per_page - 1 and \
                actual_pos < len(self.inventory) - 1:
            actual_pos += 1
        elif char == '[C' and actual_page < max_page:
            actual_page += 1
            actual_pos = (actual_page - 1) * self.items_per_page
        elif char == '[D' and actual_page > 0:
            actual_page -= 1
            actual_pos = (actual_page - 1) * self.items_per_page
        return actual_pos, actual_page


class DisplayInv:
    def __init__(self, inventory, items_per_page):
        self.inv = inventory
        self.title = 'Inventory'
        self.headings = ['Name', 'Description', 'Amount']
        self.items_per_page = items_per_page
        self.additional_spaces = 6
        self.col_lengths = [30 + self.additional_spaces, 50 + self.additional_spaces, 10 + self.additional_spaces]
        self.table_length = sum(self.col_lengths) + len(self.col_lengths) - 1  # without outer frames

    def change_inv(self, inventory):
        self.inv = inventory

    def print_table(self, actual_pos, actual_page, max_page):
        cls()
        self.print_title()
        self.print_row(self.headings)
        if actual_page * self.items_per_page < len(self.inv):
            row_ids = range((actual_page - 1) * self.items_per_page, actual_page * self.items_per_page)
        else:
            row_ids = range((actual_page - 1) * self.items_per_page, len(self.inv))
        for row_id in row_ids:
            fillchar = "O" if actual_pos == row_id else " "
            self.print_row(self.inv[list(self.inv.keys())[row_id]][2:], fillchar)
        self.print_footer(actual_page, max_page)

    def print_title(self):
        print("/" + self.table_length * "-" + "\\")
        print("|" + self.table_length * " " + "|")
        print("|" + self.title.center(self.table_length, " ") + "|")
        print("|" + self.table_length * "_" + "|")

    def print_row(self, row, fillchar=" "):
        col_amount = len(row)
        self.print_decor(fillchar, col_amount)
        print("|", end="")
        for i, el in enumerate(row):
            print((" " + str(el) + " ").center(self.col_lengths[i], fillchar) + "|", end="")
        print("")
        self.print_decor(fillchar, col_amount)
        self.print_decor("-", col_amount)

    def print_decor(self, fillchar, length):
        print("|", end="")
        for i in range(length):
            print(fillchar * self.col_lengths[i] + "|", end="")
        print("")
    
    def print_footer(self, actual_page, max_page):
        print("|" + self.table_length * "|" + "|")
        print("|" + self.table_length * " " + "|")
        which_page = str(actual_page) + " / " + str(max_page)
        print("|" + which_page.center(self.table_length, " ") + "|")
        print("|" + self.table_length * "_" + "|")
