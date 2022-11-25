guest_list = ['Alex', 'Alexander', 'Arnis']

# Prinst statement to Alex, who can't be on the dinner.
message_for_alex = "I know you can't join me tonight,"
message_for_alex += " so i hope to see you next time."
print(f'{guest_list[0]}, {message_for_alex}')

# Replacing 'Alex with Maxim'
guest_list[0] = 'Maxim'

# Inform guests that will be a bigger table
inform_guest_list = "I have found a bigger dinner table!"
print(inform_guest_list)

# Make new guest guest list.
new_guest_list = ['Renate', 'Vladimir', 'Tatjana']

# Adding more people to the list.
adding_renate_to_guest_list = guest_list.insert(0,new_guest_list[0])
adding_vladimir_to_guest_list = guest_list.insert(2,new_guest_list[1])
adding_tatjana_to_guest_list = guest_list.append(new_guest_list[2])

# Message to apologize.
message_to_apologize = "Sorry to all of you, i can invite only two of you."
print("\n" + message_to_apologize)

# Removing guests and sending message with apologize to them.
for guest in guest_list[1:5]:
    uninvited_guest = guest_list.pop()
    message_to_uninvite_guest = f"{uninvited_guest}, sorry i can't invite you."
    print("\t" + message_to_uninvite_guest)

# Add new line
print("\n")

# Print message to each person from guest_list.
for guest in guest_list:
    message = f'{guest}, would you like to have dinner with me?'
    print(message)

# Removing all people from guest list.
del guest_list[:]

# Check if someone is in the list.
print(guest_list)
# To be continue on page 47
