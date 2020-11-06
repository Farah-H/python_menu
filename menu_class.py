# task menu

# created a parent class to contain the menu
class Menu:
    def __init__(self):
        self.menu = {
            "Starters":[["soup", "salad", "bread"], 
                        [10.99, 12.99, 7.99]],
        # two lists in each category, one containing the dish title, and dish price
            "Mains":[["steak dish", "salmon dish", "chicken dish", "vegan dish"],
                    [25.00, 20.00, 15.00, 20.00],],

            "Dessert":[["ice-cream", "mocchi", "cake", "fuits"], 
                    [7.00, 10.00, 8.00, 5.00]],

            "Drinks": [["cocktail", "beer", "juice", "water"], 
                        [10.00, 6.00, 5.00, 0.00]],
        }

    # function to display the menu
    # can increment this by asking the user to input what category they would like to see 
    def display_menu(self):
        for key, value in self.menu.items():
            print(f'{key} = {value[0]}')
            print(f'Prices: {value[1]}')

# display menu in a nice way for user
#menu_object = Menu()
#menu_object.display_menu()