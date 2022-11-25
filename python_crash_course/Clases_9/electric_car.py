from Car import Car

class ElectricCar(Car): # The name of the parent class must be included in parentheses.

    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year): # __init__ method takes in the information required to make an instance.
        """Initialize attributes of the parent class."""
        # This line tells Python to call the __init__() method from parent class,
        # which gives an ElectricCar instance all the attributes of its parent class.
        super().__init__(make, model, year) 
        self.battery = Battery() 
            
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doeosn't need a gas tank!")
        
class Battery():
    """A simple attempt to model a battery for an electri car."""
    
    def __init__(self, battery_size = 85):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
               
    def describe_battery(self):
        """Print a statement descrbing the battery size."""
        print("This car has a " + str(self.battery_size) + " kWh battery.")
        
    def get_range(self):
        """Print a statment about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car go approximately " + str(range)
        message += " miles on a full charger."
        print(message)
    