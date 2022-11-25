# Create list of numbers
list_of_numbers = [5, 11, 2, 2, 3, 3, 3]
# An empty dictionary


def find_integer(list_of_numbers):
    # Count integers and move integer and its count number to dict_of_numbers.
    dict_of_numbers = {}
    for number in list_of_numbers:
        count_number = list_of_numbers.count(number)
        dict_of_numbers[number] = count_number


    # Check if integer count number is odd and return , key to function.
    for key, value in dict_of_numbers.items():
        if value % 2 != 0:
            return key


odd_number = find_integer(list_of_numbers)
# print(odd_number)
seq = [1, 1, 2, 2, 3, 4]

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

odd_number = find_it(seq)
# print(odd_number)
