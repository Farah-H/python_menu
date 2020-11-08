# task menu

# created a parent class to contain the menu
class Menu:
    def __init__(self):
        
        # two lists in each category, one containing the dish title, and dish price
        # the prices are not used at the moment, but added them so I can display the order total

        self.menu = {
            "Starters":[["soup", "salad", "bread"], 
                        [10.99, 12.99, 7.99]],
            "Mains":[["steak dish", "salmon dish", "chicken dish", "vegan dish"],
                    [25.00, 20.00, 15.00, 20.00],],
            "Dessert":[["ice-cream", "mocchi", "cake", "fruits"], 
                    [7.00, 10.00, 8.00, 5.00]],
            "Drinks": [["cocktail", "beer", "juice", "water"], 
                        [10.00, 6.00, 5.00, 0.00]],
        }


    # display menu in a nice way for user, incremented to only display a category of a user's choice
    def display_menu(self, category):
        for key,value in self.menu.items():
            if key == category.capitalize() :
                print(f'For {key}, we offer a choice of: {", ".join(value[0])}.')
                break
            else:
                continue
        return 'Please try again'


menu_object = Menu()
menu_object.display_menu('starters')