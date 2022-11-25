# Make a class called Restaurant
# Initialize restaurant with attributes as a restaurant_name
# and cuisine_type.
# Make a method describe_restaurant() that prints a message:
# "Restaurant is open"


class Restaurant():
    """Simple attempt to represent restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initalize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Provide information about restaurant and cuisine type in it."""
        print(f'Restaurant name is {self.restaurant_name.title()}.')
        print(f'Cuisine type is {self.cuisine_type.title()}.')

    def open_restaurant(self):
        """
        Provide information and prints a message:
        'Restaurant is open from 8AM till 8PM '.
        """
        print(f"{self.restaurant_name.title()} is open from 8AM till 8PM.")

hungry_angry = Restaurant('hungry angry', 'street food')
print(hungry_angry.restaurant_name)
print(hungry_angry.cuisine_type)
hungry_angry.describe_restaurant()
hungry_angry.open_restaurant()
