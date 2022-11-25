"""
chars = ['a', 'b', 'c']
ascii_character = map(ord, chars)
list_of_ascii_caharacter = list(ascii_character)
print(list_of_ascii_caharacter)

def square(number):
    return number **  2

numbers = [1, 2, 3, 4, 5]
squared = map(squared, numbers)
list(squared)

str_nums = ["4", "2", "3"]
int_nums = map(int, str_nums)
list_of_in_nums = list(int_nums)
print(list_of_in_nums[0])

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda num: num ** 2, numbers))
print(squared)

first_it = [1, 2, 3]
second_it = [4, 5, 7, 6]
print(list(map(pow, first_it, second_it)))
"""
"""
print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))
print(list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8])))
"""
"""
string_it = ["processing", "strings", "with", "map"]
print(list(map(str.capitalize, string_it)))
print(list(map(str.upper, string_it)))
print(list(map(str.lower, string_it)))
"""
"""
with_dots = ['processing...', '..strings.', '..wi.th...']
print(list(map(lambda s: s.strip("."), with_dots)))
"""
"""
with_spaces = ["processing", "  strings", "with  ", " map "]
print(list(map(str.strip, with_spaces)))
"""
"""
import re
def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)

print(remove_punctuation("...Python!"))
"""
"""
def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace.
    if c not in alphabet:
        return c

    rotated_post = ord(c) + rot_by
    # If the rotation is inside the alphabet.
    if rotated_post <= ord(alphabet[-1]):
        return chr(rotated_post)
    # If the rotation goes beyond the alphabet.
    return chr(rotated_post - len(alphabet))

caesar_alg = "".join(map(rotate_chr, "My secret message goes here." ))
print(caesar_alg)
"""
def powers(x):
    return x ** 2, x ** 3

numbers = [1, 2, 3, 4]
print(list(map(powers, numbers)))
