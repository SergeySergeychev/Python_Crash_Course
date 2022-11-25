magicians = ['Harry Houdini', 'David Blaine', 'Teller']

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great magicians.
    great_magicians = []

    # Make each magician great and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " The Great"
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

show_magicians(magicians)
print("\n")
make_great(magicians)
show_magicians(magicians)
