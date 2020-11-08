from menu_class import Menu


class Waitstaff(Menu):

    def __init__(self): # initialising the child class using super()
        super().__init__()
    
    # this function prompts the user for the items they would like to order 
    def get_order(self):

        order_items = []
        while True:
            order_item = input('What would you like to order? please enter "nothing" if you have completed your order.').lower()
            if order_item == 'nothing':
                return order_items
            else:
                order_items.append(order_item)
            return order_items

    def print_order(self, orders_list):
        print(f'Thank you for ordering the {" ".join(items for items in orders_list)}.')
