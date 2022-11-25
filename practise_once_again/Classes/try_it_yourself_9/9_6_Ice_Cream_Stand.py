# Write a class called IceCreamStand.
# class IceCreamStand inherits from the Restaurant class.
# Add an attribute flavor to IceCreamStand class.
# Attribute flavor is a list of ice cream flavors.
# Write a method called display_flavors
# Method display_flavors should show flavors.
# Create an instance of IcereamStand and call it baskin_robins.
# Fill in an instance icream_basket with delicious ice cream.

class Restaurant():
    """Simple attempt to represent restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initalize the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self,set_number):
        """Sets the number of customers who have been served."""
        self.number_served = set_number

    def increment_number_served(self, increment_number):
        """
        Increments number of served customers to total number.
        Prints out number of customers per lunch time.
        """
        self.number_served += increment_number
        print(f'Per lunch time were served {increment_number} of customers')

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

class IceCreamStand(Restaurant):
    """Attempt to represent stand with different type of ice cream."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Initialize attributes specific to an IcereamStand class.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    # Make a loop for ice cream list.
    def display_flavors(self):
        """Simple attempt to represent variety of ice cream."""
        print(f'Hello, which flavor would you like?')
        for flavor in self.flavors:
            print(f'-{flavor}')

# Creating an instance from IcereamStand class.
baskin_robins = IceCreamStand('baskin robins', 'ice cream shop')
# Filling with different flavors the attribute self.flavors.
baskin_robins.flavors = ['cherry', 'apple', 'vanilla']
# Check does attribute's list has been filled with ice cream flavors.
print(baskin_robins.flavors)
# Print out question statement and ice cream flavors for the instance.
baskin_robins.display_flavors()
