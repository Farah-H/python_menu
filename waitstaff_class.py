from menu_class import Menu


# allow user to order 3 times 
# have orders added to a list so they're not forgotten
# read order back to the user in a nice way


class Waitstaff(Menu):

    def __init__(self): # takes in the user's order, which will be a list of items
        super().__init__()

    # function to display the user's order in a nice way
    def print_order(self):
        print('Thank you for ordering the following items:')
        for item in self.order:
            print(item) 
    
    # function to ask the user what they would like to order
    # would like to add more options to this if i have time, split it up by catagories
    
    def get_order(self):
        self.order = []

        while True:
            order_item = input('What would you like to order? please enter "nothing" if you do not want anyhting(else)').lower()
            if order_item == 'nothing':
                break
            else:
                self.order.append(order_item)
        return self.order




# testing that the classes are linked fine, and that the function works using an example list

# jenny = Waitstaff()
# jenny.display_menu()
# print(jenny.get_order())
# jenny.print_order()