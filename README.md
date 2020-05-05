# stock_app
Okay, here starts the program!. The first thing to do is running the file “stock_program.py”

Now it is displayed the user interface. During the usage of the program, integer numbers from 0 to 10 are going to be the keys to navigate inside the user interface.

It is always possible to end the program by typing 0.

Every option but number (3) are independent and they have no other sub-options inside of it. But in the 3 option we decided to include three different options to update name, packaging status and the date of the bakery item. This last option is important when the date of production of an item is different to the one when the item was included into database.

There is a small delay ​“time.sleep(0.2)” w​ hen an action is made to make the program more intuitive. Thus, you can visualize for 0.2 seconds the result of the action committed, like, for example, the bakery item introduced through add_new method.
We decided to add one function to visualize all the objects inside the database at any point (option number 5).

The intention of the program is that, once you have added items into database, you save them into a file with option 9 and, if you want to clean session and leave everything clear, you can also call clear_all so it gets clean at all.

The remaining functions have been explained above, you can add, remove, edit and search. Furthermore you can get all the products at one time, the total number of them, get the age of a product and the proportion of those products whose package is broken.

When the user is done it can exit session by typing 0. That’s pretty much it, thanks for using the program!
