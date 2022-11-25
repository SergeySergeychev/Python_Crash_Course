# At start we start with parent class. When we create a child class, the paret class must be part of current file
# and must appear before the child class in the file.

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Print a neatly formatted descriptive name."""
        long_name =str(self.year) + ' ' + self.make + ' ' + self.model + "."
        return long_name.title()
    
    def read_odometer(self):
        """Print a statetment showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
              
    def update_odometer(self, milage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back. 
        """
        if milage >= self.odometer_reading:              
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")
              
    def increment_odometer(self, mile):
        """Add the given amount to the odometer reading"""
        self.odometer_reading +=mileS
            
    def fill_gas_tank(self):
        """Simulating car filling on a gasoline station"""
        print("Filling car with gasoline.") 
        