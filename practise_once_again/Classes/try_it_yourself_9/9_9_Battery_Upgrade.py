# Use the final version of electric_car.py.
# Add a method to Battery class called upgrade_battery().
# This method should check battery size and set the capacity to 85.
# Make an electric car with a default battery size.
# Call get_range() once.
# Call upgrade_battery method.
# Call get_range().
class Car():
    """ A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def incriment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Filling gas tank with a petrol."""
        print(f'Filling cars gas tank.')

    def read_odometer(self):
        """Print a statement showing a car's mileage."""
        print(f'This car has {self.odometer_reading} miles on it.')

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 240
        elif self.battery_size == 85:
            range =270

        message = "This car can go aproximately " + str(range)
        message +=" miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """
        Check battery size.
        If battery size is smaller than 85,than upgrade battery to 85 kWh.
        Print statement of upgraded battery.
        Else print statement: "The battery is already upgraded".
        """
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("Electric car has battery with capacity of 85 kWh")



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar ('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
