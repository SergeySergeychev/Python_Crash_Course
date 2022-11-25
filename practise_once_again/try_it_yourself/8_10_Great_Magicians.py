# Start with a cope of 8_9_Magicians.py.
# Write function make_great().
# Function modifies magicians names by adding Great.
# Call the function show_magicians().

list_of_magicians = ['marek', 'kazbek', 'urlala']
def show_magicians(list_of_magicians):
    """Simple attempt to represent magicians."""
    for magician in list_of_magicians:
        print(magician.title())

def make_great(list_of_magicians,great_magician):
    """Promoting each magician to Great magician."""
    # Make each magician great and add to great_magicians.
    while list_of_magicians:
        magicians = list_of_magicians.pop()
        g_magician = f'Great {magicians}'
        great_magician.append(g_magician)
    # Add the great magician back into list_of_magicians.
    for g_magician in great_magician:
        list_of_magicians.append(g_magician)






list_of_magicians = ['marek', 'kazbek', 'urlala']
great_magician = []
make_great(list_of_magicians[:],great_magician)
show_magicians(list_of_magicians)
print(great_magician)
