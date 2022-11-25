# Start with cod from 8_10_Great_Magicians.property.
# Call the function make_great().
# Make a copy of the list_of_magicians.
# Return new list and save it in a separate list.
list_of_magicians = ['marek', 'kazbek', 'urlala']
def show_magicians(list_of_magicians):
    """Simple attempt to represent magicians."""
    for magician in list_of_magicians:
        print(magician.title())

def make_great(list_of_magicians):
    """Promoting each magician to Great magician."""
    great_magicians = []

    # Make each magician great and add to great_magicians.
    while list_of_magicians:
        magicians = list_of_magicians.pop()
        g_magician = f'{magicians.title()} the Great'
        great_magicians.append(g_magician)

    # Add the great magician back into list_of_magicians.
    for g_magician in great_magicians:
        list_of_magicians.append(g_magician)
    return(list_of_magicians)





list_of_magicians = ['marek', 'kazbek', 'urlala']
great_magicians = make_great(list_of_magicians[:])
show_magicians(list_of_magicians)

print("\nGreat magicians.")
show_magicians(great_magicians)

print("\nOriginal magicians.")
show_magicians(list_of_magicians)
