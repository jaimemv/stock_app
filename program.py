import bakeryclass
import time
from datetime import date
from datetime import datetime
import pickle

print('-------------------------------------------\n||| WELCOME TO THE BAKERY STOCK PROGRAM |||')
print('-------------------------------------------')


def display_menu():
    print('------------')
    print('1) Add new bakery item')
    print('2) Remove an item')
    print('3) Edit an item')
    print('4) Search Item')
    print('5) Show all')
    print('6) Number of stock')
    print('7) Check item age')
    print('8) Proportion of broken items')
    print('9) Write information to file')
    print('10) Clear all')
    print('0) Quit')


class UserStock:

    def __init__(self):
        self.stock = {}

    def main(self):

        choice = 999
        add_new_item = 1
        remove_item = 2
        edit_item = 3
        search = 4
        show_all = 5
        number_stock = 6
        item_age = 7
        proportion_broken = 8
        write_file = 9
        clear_all = 10
        quit_choice = 0

        self.stock['cookie1'] = bakeryclass.BakeryItem('cookie1', 'no sugar', 'n', '5')
        self.stock['cookie1'].date = date(2019, 9, 11)

        while choice != " ":
            display_menu()
            print('------------')
            try:
                choice = int(input('Enter your choice: '))
            except ValueError:
                print('Error. Please, introduce a menu option.')
                time.sleep(2)

            # Here it starts the program:

            # Option 1
            if choice == add_new_item:
                name = input('Please, introduce the name of the product: ')
                UserStock.add_new(self, name)
                print('Item added successfully!')
                print(' name: ', self.stock[name].name, ' | notes: ', self.stock[name].note,
                      ' | Packaging status: ',
                      self.stock[name].status, ' | Value: ', '$', self.stock[name].value, sep='')
                time.sleep(2)
            # Option 2
            elif choice == remove_item:
                UserStock.remove(self)
            # Option 3
            elif choice == edit_item:
                print('1) Update name of an item')
                print('2) Update status of an item')
                print('3) Update date of an item')

                try:
                    choice = int(input('Enter your choice: '))
                    if choice == 1:
                        UserStock.change_name(self)
                    elif choice == 2:
                        UserStock.change_status(self)
                    elif choice == 3:
                        UserStock.set_age(self)
                except ValueError:
                    print('Value error, please introduce a valid option (1, 2 or 3)')

            # Option 4
            elif choice == search:
                bakeryitem = input('Please introduce the item to search: ')
                UserStock.get_item(self, bakeryitem)
            # Option 5
            elif choice == show_all:
                UserStock.get_items(self)
            # Option 6
            elif choice == number_stock:
                UserStock.get_len(self)
            # Option 7
            elif choice == proportion_broken:
                UserStock.get_broken(self)
            # Option 8
            elif choice == item_age:
                UserStock.get_age(self)
            # Option 9
            elif choice == write_file:
                filename = input('Enter a filename to store the menu (skip extension): ')
                self.write_file(filename + '.pkl')
            # Option 10
            elif choice == clear_all:
                UserStock.clear_all(self)
            # Option 0
            elif choice == quit_choice:
                print('The program has ended')
                break

        # Creation and remove functions

    def add_new(self, bakeryitem):
        notes = input('Please, introduce notes: ')
        package = bakeryclass.pck()
        value = float(bakeryclass.val())
        self.stock[bakeryitem] = bakeryclass.BakeryItem(bakeryitem, notes, package, value)

    def remove(self):
        bakeryitem = input('Please type the name of the article that you want to remove from the stock list: ')
        try:
            del self.stock[bakeryitem]
            print('The item "', bakeryitem, '" has been deleted', sep='')
        except:
            print('Sorry, the item is not currently in stock.')
        time.sleep(2)

    # Mutators

    def change_name(self):
        while True:
            bakeryitem = input('Introduce the name of the item to update: ')
            if bakeryitem not in self.stock:
                print('The name is not in the list. Please try another name')
            else:
                break
        new = input('Please introduce the new name of the item: ')
        self.stock[new] = self.stock[bakeryitem]
        del self.stock[bakeryitem]
        self.stock[new].name = new
        print('The name of the product has been updated sucessfully')
        time.sleep(2)

    def change_status(self):
        while True:
            bakeryitem = input('Introduce the name of the item to update: ')
            if bakeryitem not in self.stock:
                print('The name is not in the list. Please try another name')
            else:
                break
        new = bakeryclass.pck()
        self.stock[bakeryitem].status = new
        print('The status has been updated sucessfully')
        time.sleep(2)

    def set_age(self):
        bakeryitem = input('Please introduce the name of the object to set his production date: ')
        year = int(input('Enter the year: '))
        month = int(input('Enter the month: '))
        day = int(input('Enter the day: '))
        self.stock[bakeryitem].date = date(year, month, day)
        print('Thanks! The production date has been set successfully.')
        time.sleep(2)

    # Accessors

    def get_item(self, bakeryitem):  # Search an item and displays its attributes
        if bakeryitem in self.stock:
            print('// ', 'Item: "', self.stock[bakeryitem].name, '" //')
            print(' Name: ', self.stock[bakeryitem].name, ' | Notes: ',
                  self.stock[bakeryitem].note, ' | Packaging status: ',
                  self.stock[bakeryitem].status, ' | Value: ',
                  '$', self.stock[bakeryitem].value, sep='')
            time.sleep(2)
        else:
            print('The name introduced is not in the list')
            time.sleep(2)

    def get_len(self):  # Gets the total number of items
        n_stock = len(self.stock)
        print('The number of items in stock is:', n_stock, 'item(s)')
        time.sleep(2)

    def get_broken(self):  # Gets the percentage of broken packagings
        broken_sum = 0
        for key in self.stock:
            if self.stock[key].status == 'y':
                broken_sum += 1
        proportion = (broken_sum / len(self.stock)) * 100
        print('The proportion of broken packaging is: ', proportion, '% broken', sep='')
        time.sleep(2)

    def get_items(self):  # Prints all the stock
        try:
            for key in self.stock:
                print('//', 'Item: "', self.stock[key].name, '" //')
                print(' Name: ', self.stock[key].name, ' | Notes: ', self.stock[key].note, ' | Packaging status: ',
                      self.stock[key].status, ' | Value: ', '$', self.stock[key].value, sep='')
        except:
            print('Sorry, the stock data seem to be empty')
        time.sleep(2)

    def get_age(self):  # Gets the age (date) of the product
        bakeryitem = input("Please introduce the name of the item to get the time since it was produced: ")
        current_date = date.today()
        product_date = self.stock[bakeryitem].date
        age = current_date - product_date
        if age == 0:
            print("The age of the product is 0 or it hasn't been setted yet.")
        else:
            print('The age of the bakery item is:', age.days)
        time.sleep(2)

    # Extra functions

    def write_file(self, file):
        file = open(file, 'wb')
        pickle.dump(self.stock, file)
        f.close()

    def clear_all(self):
        while True:
            clear = input('You are about to delete all the stock information, are you sure? type "y" for yes or "n" for no: ')
            if clear == 'y':
                del self.stock
                print('Done! The stock has been wiped out')
                break
            elif clear == 'n':
                print('OK! The wipe out has been cancelled')

            else:
                print('Type Error, getting back to main menu')
                break
        time.sleep(2)


menu = UserStock()
menu.main()
