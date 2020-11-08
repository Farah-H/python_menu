from waitstaff_class import Waitstaff

# This part of the program will actually execute taking an order, saving it, and printing it back to the user

# we need to first display the menu to the user, our waitress Jenny will take do this

orders_list = []

jenny = Waitstaff()

while True:
    category = input('Would you like to see our starters, mains, desserts or drinks? Please enter "nothing" if you do not want to see the menu.').lower()
    jenny.display_menu(category)
    if category == 'nothing':
        take_order = input('Are you ready to make an order?').lower()
        if take_order == 'yes':
            this_order = jenny.get_order()
            jenny.print_order(this_order)

