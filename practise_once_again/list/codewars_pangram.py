

# Ex. Pangram.
    # A pangram is a sentence that contains every single letter of the
    # alphabet at least once. For example, the sentence "The quick brown
    # fox jumps over the lazy dog" is a pangram, because it uses the letters
    # A-Z at least once(case is irrelevant).
    # Given a string, detect whether or not it is a pangram. Return True
    # if it is, False if not. Ignore numbers and punctuation.

# Solution:
    # For letter in string:
        # make list and sort it alphabeticly.
        # check if list contains all letter from A - Z.
            # if yes return True.
        # otherwise return False.

import string

def is_pangram(s):
    a_z = []
    for letter in string.ascii_lowercase:
        if letter in s.lower():
            a_z.append(letter)
    if len(a_z) == 26:
        return True
    else:
        return False
    print(a_z)
s = "The quick brown fox jumps over the lazy dog"
print(is_pangram(s))
