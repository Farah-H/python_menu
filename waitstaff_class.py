from menu_class import Menu


# allow user to order 3 times 
# have orders added to a list so they're not forgotten
# read order back to the user in a nice way


class Waitstaff(Menu):

    def __init__(self, order): # takes in the user's order, which will be a list of items
        super().__init__()
        self.order = order

    # function to display the user's order in a nice way
    def print_order(self):
        print('Thank you for ordering the following items:')
        for item in self.order:
            print(item) 
    
    # function to ask the user


# testing that the classes are linked fine, and that the function works using an example list

# order = ['fruits', 'steak']
# jenny = Waitstaff(order)
# jenny.display_menu
# jenny.print_order()