# Start with program from ex. 9-1.
# Add an attribute with a default value of 0, call number_served.
# Create an instance callled resaurant from class.
# Print the number of customer the restaurant has served.
# Change the value of attribute number_served .
# Print the number of customer the restaurant has served.
# Add a method called set_number_served().
# Method set_number_served adds customers to the number_served.
# Call method set_number_served with number 10 customers.
# Print the number of customer the restaurant has served.
# Add a method increment_number_served().
# Method increment_number_served increments served customers to number_served.
# Call method increment_number_served with number 10.
# Make print statement  for increment_number_served:
# "In a day we have served (number_served)"

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

restaurant = Restaurant('hungry_angry','street food')
restaurant.set_number_served(10)
restaurant.increment_number_served(10)
print(f'In the restaurant we have served {restaurant.number_served} tables')
