# Find the missing letter
    # Write a method that takes an array of consecutive letters as input and
    # that returns the missing letter in the array.

    # You will always get an valid array. And it will be always exactly
    # one letter be missing. The length of the array will always be at least
    # two character.

# Example:
    #['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

# Solution
    # Starting point should be first letter in array and end point last letter
    #  Check given array in range of given array with alphabetic array.
        # if letter is missing return letter
        # else letter True
"""
    for letters in array:
        if array missing consecutive letter:
            return letter
        else:
            return True
"""
"""


def make_sum_of_chars(chars):
    return sum(map(ord, chars))
def convert_first_letter_to_ascii(chars):
    convert_first_letter_to_ascii = ord(chars[0])
    return convert_first_letter_to_ascii

def make_sum_of_consecutive_list(chars):
    number_of_characters = len(chars)
    sum_of_consecutive_list = convert_first_letter_to_ascii(chars)
    consecutive_list = [convert_first_letter_to_ascii(chars)]
    for char in range(number_of_characters):
        sum_of_consecutive_list += 1
        consecutive_list.append(sum_of_consecutive_list)
    return sum(consecutive_list)
def find_missing_letter(chars):
    missing_letter = chr(make_sum_of_consecutive_list(chars) -
                      make_sum_of_chars(chars))
    return missing_letter

chars =['a','b','c','d','f']

print(make_sum_of_chars(chars))
print(make_sum_of_consecutive_list(chars))
print(find_missing_letter(chars))
"""
"""
def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1 + ord(chars[n]))
chars =['a', 'c']
print(find_missing_letter(chars))

"""
"""
def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
"""
