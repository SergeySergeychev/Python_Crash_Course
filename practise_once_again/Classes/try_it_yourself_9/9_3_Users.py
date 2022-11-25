# Make a class called User.
# Create attributes called first_name, last_name, e_mail, phone_number.
# Make a method called describe_user().That prints a summary of the
# users information.
# Make a method called greet_user() that prints a personalized greeting.
# Create several instances.
# Call both methods for each user.

class User():
    """A simple attempt to represent user."""

    def __init__(self, first_name, last_name, e_mail, phone_number):
        """Initialize attributes of an user."""
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.phone_number = phone_number

    def describe_user(self):
        """Prints out information about an user."""
        user_information = "User information:"
        user_information +="\n\tFirst name is: " + self.first_name.title()
        user_information +="\n\tLast name is: " + self.last_name.title()
        user_information +="\n\tEmail is: " + self.e_mail
        user_information +="\n\tPhone number is: " + self.phone_number
        print(user_information)


    def greet_user(self):
        """Simulates greeting of an user."""
        print("Welcome back - " +
              self.first_name.title() +
              ' ' + self.last_name.title() + "."
              )

my_instance = User('sergey', 'sergeychev', 'ssergeychev@inbox.lv', '28882999')

friends_instance = User('arnis', 'raudive', 'arauda@gmail.com', '23332444')

friends_instance.describe_user()
friends_instance.greet_user()
print("\n")

my_instance.describe_user()
my_instance.greet_user()
