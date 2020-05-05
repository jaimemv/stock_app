from datetime import date


class BakeryItem:
    def __init__(self, name, note, status, value):
        self.name = name
        self.note = note
        self.status = status
        self.value = value
        self.date = date.today()


# Function to filter the data introduced in package status
def pck():
    while True:
        package = input('Is the package broken? type y/n: ')
        if package == 'y' or package == 'n':
            return package
        else:
            print('Type error. Please type again.')


def val():
    while True:
        try:
            value = float(input('Please, enter the price of the item: '))
        except ValueError:
            print("Not an correct value. Try again.")
            continue
        else:
            return value


