
# All elements of list are True
l = [4, 5, 1]
print(all(l))

# All elements of list are false.
l = [0, 0, False]
print(all(l))

# Some elements of list are true, while others are False.
l = [1, 0, 6, 7, False]
print(all(l))

# Empty list.
l = []
print(all(l))
