guest_list = ['Alex', 'Alexander', 'Arnis']

message_for_alex = "I know you can't join me tonight,"
message_for_alex += " so i hope to see you next time."
print(f'{guest_list[0]}, {message_for_alex}')
# Replacing 'Alex with Maxim'
guest_list[0] = 'Maxim'
for guest in guest_list:
    message = f'{guest}, would you like to have dinner with me?'
    print(message)
