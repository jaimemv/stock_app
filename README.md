# Stock app
This is one of the first modules I wrote in Python. It was the final project of a Python course in the University. Its aim is to keep track of the stock of a Bakery store.

# Guide
Okay, here starts the program!. The first thing to do is running the file “stock_program.py”
Now it is displayed the user interface. During the usage of the program, integer numbers from 0 to 10 are going to be the keys to navigate inside the user interface.

It is always possible to end the program by typing 0.

Every option but number (3) are independent and they have no other sub-options inside of it. But in the 3 option we decided to include three different options to update name, packaging status and the date of the bakery item. This last option is important when the date of production of an item is different to the one when the item was included into database.

There is a small delay *“time.sleep(0.2)”* when an action is made to make the program more intuitive. Thus, you can visualize for 0.2 seconds the result of the action committed, like, for example, the bakery item introduced through add_new method.

We decided to add one function to visualize all the objects inside the database at any point (option number 5).

The intention of the program is that, once you have added items into database, you save them into a file with option 9 and, if you want to clean session and leave everything clear, you can also call clear_all so it gets clean at all.

The remaining functions have been explained above, you can add, remove, edit and search. Furthermore you can get all the products at one time, the total number of them, get the age of a product and the proportion of those products whose package is broken.
When the user is done it can exit session by typing 0.


# Class BakeryItem

Here we define the attributes that a bakery item should have.
- name. reference to the name of the bakery item
- note: reference to notes the user might introduce describing the product.
- status: boolean (2 possible values) input to define whether the product packaging is
broken or it is not
- value: price in SEK of the product
- date: this attribute is optional. Even it is not asked to be introduced when adding a new
product for not making the program too slow. We want the user to waste too many time.


# Class UserStock
This class is used as a dictionary. It calls class BakeryItem and stores its instances into the dictionary.
It only has one attribute self.stock, where the dictionary is located.
Furthermore, we will use the attribute BakeryItem.name as key of the dictionary.

## __init__(self)
It initializes the attribute self.stock of the function. It is the only attribute the class has, but still it provides a lot of information.
The attribute self.stock is a dictionary object, which will be very useful for us to perform the tasks required.

## Create and delete functions
### add_new(self, bakeryitem):
This function creates a new instance of BakeryItem and stores it at dictionary of the lonely attribute of class UserStock which is UserStock.stock.

For the status of the packaging (broken or not broken) we previously created a function to assure we get information required. Otherwise, if we don’t get boolean value (“y” or “n” in this case) we cannot calculate properly the proportion of broken/non-broken items. We do the same with value attribute to get a float.

Finally we update the dictionary with data inputted by the user which consist of the name of the product (key) and 4 different values inside: name, notes, packaging and value.

## def remove(self):
This function removes an instance of BakeryItem. If it gets an error it basically returns an error.

## Mutators
### Change_name(self, bakeryitem, new)
This function updates the name of an existing bakery item. First it copies the old element but using the new key called “new”. After, the old element is deleted.
Since the key and the attribute .name are the same, the attribute .name is also updated.

### change_status(self, bakeryitem, new)
This function update the status of the packaging of an existing bakery item. It basically gets input of the item to search and the new status (no matter what the previous status was) and are passed as arguments for the function.

### set_age(self)
Since products are supposed to be stored into database at the time they are introduced, default date of production will be current date of creation. If this date is not correct, we provide the opportunity to modify with this function. It is asked the year, month and date to the user.


## Accessors
### get_item(self, bakeryitem)
This function searches the name of the item introduced by the user and displays the information of it. For this, a boolean logic is used. It iterates the dictionary until it find the name.
### get_len(self)
This function is an accessor that prints the length UserStock.stock, or, what is the same, the amount of products stored into database.
### get_items(self)
This function was not required, but since it is not supposed to be a huge amount of data, I find really useful a function that orderly prints every item.
### get_age(self)
This function subtracts the production date already set (which is by default current date of creation) to current date “date.today()” and returns the number of days it has passed since production to current date.
### write_file(self, file)
This function writes the total value of the stock to a new file. The name of the file is typed by the user. It is possible thanks to method “dump” of “pickle” library.
### clear_all(self)
This function basically wipes out everything, even the default value settled in the code. It is make with method “del”.
Since it is a radical method it is asked before the method is executed to introduce a “y”.

## main(self)
First of all it is assigned a variable for each main menu options (from 0 to 10).
After that we create an instance of UserStock class called “cookie1” and we establish a production date for it.
Then it comes the tricky part. For every value introduced by the user in the variable “choice” we call a different function (those previously explained.

# Static code
Outside these two classes explained above I have also written different functions and calls to them.
Inside “bakeryclass” module we can find two static functions:
## Functions
### pck()
It is a validator for the packaging status input. Basically it just accept two different values: ‘y’ and ‘n’.
### val()
It is also a validator to get a floating number for the price of the bakery item.
### display_menu()
Here we assign an integer value to each option inside the main menu.
## Calls to functions and objects
At the end of the module program we can find two code lines:
**menu = UserStock()** 
**menu.main()**
Create an object of UserStock class and then we call the method main which, as it has been mentioned above, it runs the program





