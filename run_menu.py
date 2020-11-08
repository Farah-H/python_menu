from waitstaff_class import Waitstaff
# This part of the program will actually execute taking an order, saving it, and printing it back to the user



#instantiating the waitstaff class
jenny = Waitstaff()

all_orders = [] # a list to store all orders in (could increment by making this csv output)



# prompting the user for which part of the menu they would like to see

category = input('Would you like to see our starters, mains, desserts or drinks? Please enter "nothing" if you do not want to see the menu.').lower()
# if they are done with (or don't want to read) the menu, they can start to place an order    
if input('Are you ready to make an order?').lower() == 'yes':
    this_order = jenny.get_order()
    print(this_order)
    print(jenny.print_order(this_order))
else: 
    jenny.display_menu(category)
