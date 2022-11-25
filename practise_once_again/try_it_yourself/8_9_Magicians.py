# Make a list of magician's names
# Pass the list to the function show_magicians()
# Function print out all magicians names.

list_of_magicians = ['marek', 'kazbek', 'urlala']

def show_magicians(list_of_magicians):
    for magician in list_of_magicians:
        print(magician.title())

show_magicians(list_of_magicians)
