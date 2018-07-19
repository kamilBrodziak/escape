import os
import sys
import random
from common import getChar, cls, Printing
from termcolor import cprint
from math import ceil
import time


class Inv:
    def __init__(self, items_per_page, gamer):
        self.inventory = []  # list of lists

        # dict which keys are types of item equiped, and values are list containing item
        self.temp_equiped = {}

        self.gamer = gamer
        self.items_per_page = items_per_page
        self.display_inv = DisplayInv(self.inventory, self.items_per_page, self.gamer.equiped, self.gamer)
        self.actual_pos = 0  # actual position of our cursor in inventory
        self.actual_page = 1

    def add_rand(self, filename, how_much):
        # how_much - how much random generated item we want to add to inv
        with open(filename) as filename:
            items = filename.readlines()

        for i in range(how_much):
            item = random.choice(items)
            item = item[:-1].split(";")  # separate string by ";" and delete "\n" ending
            # item[0] - id, item[1] - what_it_is, 2 - value, 3 - name, 4 - description
            # value - what value add for example to boots defence

            # to know if item is in inventory already in order to increase value or add item to inv
            # there is another value, item[5] - amount of items of this type
            ids_list = [el[0] for el in self.inventory]
            if item[0] in ids_list:
                # need to create a list with elements of inv without the amount, in order to get index of item
                inv_temp = [el[:-1] for el in self.inventory]
                self.inventory[inv_temp.index(item)][5] += 1
            else:
                item.extend([1])  # adding amount to item
                self.inventory.append(item)  # adding item to inventory

    def run_inv(self):
        self.max_page = ceil(len(self.inventory) / self.items_per_page)
        char = ""  # key pressed
        if self.max_page == 0:  # exception when we don't have any item in inv
            self.max_page = 1
        while char.lower() != 'i':
            self.display_inv.print_table(self.actual_pos, self.actual_page, self.max_page)
            char = getChar(1)
            if char == '\x1b':
                self.arrows_move()
            elif char == '\n':
                self.use_item()

    def arrows_move(self):
        char = getChar(2)
        if char == '[A' and self.actual_pos > (self.actual_page-1) * self.items_per_page:
            self.actual_pos -= 1
        elif char == '[B' and self.actual_pos < self.actual_page * self.items_per_page - 1 and \
                self.actual_pos < len(self.inventory) - 1:
            self.actual_pos += 1
        elif char == '[C' and self.actual_page < self.max_page:
            self.actual_page += 1
            self.actual_pos = (self.actual_page - 1) * self.items_per_page
        elif char == '[D' and self.actual_page > 1:
            self.actual_page -= 1
            self.actual_pos = (self.actual_page - 1) * self.items_per_page

    def use_item(self):
        # value in inv - what value add to for example boots defence
        value = self.inventory[self.actual_pos][2]
        item_type = self.inventory[self.actual_pos][1]

        if self.inventory != {}:
            if item_type in self.gamer.equiped.keys():
                self.equip(item_type, value)
                self.display_inv.change_names_equiped(self.temp_equiped[item_type])
            elif item_type == "hunger":
                self.gamer.hunger += float(value)
                self.change_item_amount()
                if self.gamer.hunger > 100:
                    self.gamer.hunger = 100.0
            self.gamer.update_stats()

    def equip(self, item_type, value):
        # if we have something of this item_type equiped, take off it and add to inv
        if self.gamer.equiped[item_type] != 0:
            self.add_item(self.temp_equiped[item_type])

        # add item to temporary dict in order to know what in future we want to take off
        self.temp_equiped[item_type] = self.inventory[self.actual_pos][:-1]

        # add item stat to gamer stat
        self.gamer.equiped[item_type] = int(value)
        self.change_item_amount()

    def change_item_amount(self):
        self.inventory[self.actual_pos][5] -= 1
        if self.inventory[self.actual_pos][5] == 0:
            del self.inventory[self.actual_pos]

            # if our cursor is on len(inv) so it is out of range, do:
            if self.actual_pos > len(self.inventory) - 1:
                self.change_page_display()

    def change_page_display(self):
        self.actual_pos -= 1
        self.actual_page = ceil(self.actual_pos / self.items_per_page)
        self.max_page = ceil(len(self.inventory) / self.items_per_page)

    def add_item(self, item):
        # to know if item is in list or not
        ids_list = [el[0] for el in self.inventory]
        if item[0] in ids_list:
            inv_temp = [el[:-1] for el in self.inventory]
            self.inventory[inv_temp.index(item)][5] += 1
        else:
            item.extend([1])
            self.inventory.append(item)


class DisplayInv:
    def __init__(self, inventory, items_per_page, equiped, gamer):
        self.gamer = gamer
        self.inv = inventory
        self.title = 'Inventory'
        self.headings = ['Name', 'Description', 'Amount']
        self.items_per_page = items_per_page
        self.names_equiped = {}
        self.col_lengths = [50, 40, 20]
        self.table_length = sum(self.col_lengths) + len(self.col_lengths) - 1  # without outer frames
        self.stats = equiped
        self.printing = Printing(self.col_lengths, self.table_length, self.title)

    def change_names_equiped(self, temp_equiped):
        self.names_equiped[temp_equiped[1]] = temp_equiped[3]

    def print_table(self, actual_pos, actual_page, max_page):
        cls()
        self.printing.print_title()
        self.printing.print_row(self.headings, header=True)

        # define row_ids which we want to display and decide, if
        # it is full page of items or not
        if actual_page * self.items_per_page < len(self.inv):
            row_ids = range((actual_page - 1) * self.items_per_page, actual_page * self.items_per_page)
        else:
            row_ids = range((actual_page - 1) * self.items_per_page, len(self.inv))

        for row_id in row_ids:
            fillchar = "O" if actual_pos == row_id else " "
            self.printing.print_row(self.inv[row_id][3:], fillchar)
        self.print_footer(actual_page, max_page)

    def print_footer(self, actual_page, max_page):
        cprint("|" + self.table_length * "|" + "|", "grey", "on_white", attrs=['bold'])
        cprint("|" + self.table_length * " " + "|", "grey", "on_white", attrs=['bold'])
        which_page = str(actual_page) + " / " + str(max_page)
        cprint("|" + which_page.center(self.table_length, " ") + "|", "grey", "on_white", attrs=['bold'])
        cprint("|" + self.table_length * "_" + "|", "grey", "on_white", attrs=['bold'])
        self.print_stats()
        self.print_equiped()

    def print_stats(self):
        string = "|"
        for el in self.stats:
            string += " " + el + ": " + str(self.stats[el]) + " |"
        string += " key: " + str(self.gamer.key)
        string = string + (self.table_length - len(string) + 1) * " " + "|"
        cprint(string, "white", "on_grey", attrs=['bold'])
        cprint("|" + self.table_length * "_" + "|", "white", "on_grey", attrs=['bold'])

    def print_equiped(self):
        cprint("/" + self.table_length * "-" + "\\", 'white', 'on_grey', attrs=['bold'])
        cprint("|" + "Equiped".center(self.table_length, " ") + "|", 'white', 'on_grey', attrs=['bold'])
        cprint("|" + self.table_length * "_" + "|", 'white', 'on_grey', attrs=['bold'])

        for key in self.names_equiped:
            string = key + ":  " + self.names_equiped[key]
            print("| ", string, " " * (self.table_length - 1), "|")

        cprint("|" + self.table_length * "_" + "|", 'white', 'on_grey', attrs=['bold'])
