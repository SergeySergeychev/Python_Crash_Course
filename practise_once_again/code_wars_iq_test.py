
def iq_test(numbers):
    """A function to return "real" index position of a number."""
    # Variables to count quantity of even and odd numbers.
    even_numbers_quantity = 0
    odd_numbers_quantity = 0
    # For loop to count even and odd numbers.
    for i in split_list(numbers):
        if int(i) % 2 == 0:
            even_numbers_quantity +=1
        else:
            odd_numbers_quantity += 1
    # Conditional if odd number is only in example return odd number.
    # Else if return even
    # Else if odd and even number quantatity are equal return None.
    if even_numbers_quantity > odd_numbers_quantity:
        return index_odd_number(numbers)

    elif odd_numbers_quantity > even_numbers_quantity:
        return index_even_number(numbers)
    else:
        return None

def odd_number(numbers):
    """Function to find odd_number in the list."""
    for num in split_list(numbers):
        if int(num) % 2 != 0:
            return num

def even_number(numbers):
    """Function to find even_number in the list."""
    for num in split_list(numbers):
        if int(num) % 2 == 0:
            return num

def split_list(numbers):
    """Split string into list of numbers."""
    splited_list = numbers.split()
    return splited_list

def index_even_number(numbers):
    """Indexing position of the even number in the list."""
    even_number_position = split_list(numbers).index(even_number(numbers)) + 1
    return even_number_position

def index_odd_number(numbers):
    """Indexing position of the odd number in the list."""
    odd_number_position = split_list(numbers).index(odd_number(numbers)) + 1
    return odd_number_position
numbers = "8 6 10 1 7"
print(iq_test(numbers))
