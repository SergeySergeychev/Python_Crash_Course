# Write function sandwich.
# Add to function *parameter(arbitrary number of arguments)
# Print summary of the sandwich that is being ordered.
# Call function tree times with a different number of arguments.

def make_sandwich(*toppings):
    """Making sandwich with requested toppings."""
    print("\nMakind sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('cheese', 'salat', 'chicken meet', 'mustard', 'slice of bread')
make_sandwich('slice of bread', 'cheese', 'coconut oil')
make_sandwich('tomato', 'cheese', 'slice of bread', 'tomato')
