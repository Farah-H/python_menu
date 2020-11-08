from menu_class import Menu


class Waitstaff(Menu):

    def __init__(self): # initialising the child class using super()
        super().__init__()
    
    # this function prompts the user for the items they would like to order 
    def get_order(self):
        self.order_items = []
        while True:
            self.item = ('What would you like to order? enter "nothing" if you want nothing.')
            if item == 'nothing':
                return self.order_items
            else:
                self.order_items.append(self.item)

    def print_order(self, orders_list):
        print(f'Thank you for ordering the {", ".join(items for items in self.orders_list)}. Your order will arrive shortly.')
