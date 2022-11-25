# Write function that stores information about a car in a dictionary.
# In the function must be 2 default arguments as manufacturer and a
# model name.
# Function should accept an arbitrary number of keyword arguments.
# Call the function with two default arguments and two keyword arguments.
# Function should work like this one:
    # car = make_car('subaru', 'outback', color='blue', tow_package=True).
# Print the dictionary

def make_car(manufacturer, model, **option_packages):
    """Building a dictionary contatining everything we know about car"""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in option_packages.items():
        car[key] = value

    return car

car_model = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car_model)
