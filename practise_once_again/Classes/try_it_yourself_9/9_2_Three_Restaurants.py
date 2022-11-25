# Start from restaurant class.
# Create three different instances from the class Restaurant.
# For each instance call method describe_restaurant.

class Restaurant():
    """Simple attempt to represent restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initalize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Provide information about restaurant and cuisine type in it."""
        print(f'Restaurant name is {self.restaurant_name.title()}.')
        print(f'Cuisine type is {self.cuisine_type}.')

    def open_restaurant(self):
        """
        Provide information and prints a message:
        'Restaurant is open from 8AM till 8PM '.
        """
        print(f"{self.restaurant_name.title()} is open from 8AM till 8PM.")
hungry_angry = Restaurant('hungry angry', 'street food')

lido = Restaurant('lido', 'home made cuisine')

hesburger = Restaurant('hesburger', 'fast food')

hungry_angry.describe_restaurant()
hungry_angry.open_restaurant()
print("\n")

lido.describe_restaurant()
lido.open_restaurant()
print("\n")

hesburger.describe_restaurant()
hesburger.open_restaurant()
