class Restaurant():
    """A simple attemp to represent restaurant"""
    
    def  __init__(self,restaurant_name,cuisine_type):
        """Initialize attributes to represent restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def number_of_customers(self):
        """Prints statement about customers quantity"""
        print("Number of customers: " + str(self.number_served) + ".")
        
    def set_number_served(self, customer):
        """Counts customers at the moment"""
        self.number_served = customer
    
    def increment_number_served(self, increment_number_of_customers):
        """Increment number of customers to total amount."""
        self.number_served += increment_number_of_customers
       
    
    def describe_restaurant(self):
        """Print a statements showing restaurant's name and cuisine's type."""
        print("Restaurant's name: " + self.restaurant_name.title() + ".")
        print("Restaurant's cuisine: " + self.cuisine_type.title() + ".")
        
    def open_restaurant(self):
        """Simulates sign 'open'"""
        print("Welcome, restaurant is open.")