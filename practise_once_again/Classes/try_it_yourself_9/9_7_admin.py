# Write a class called Admin.
# Class Admin inherits from the User class of ex. 9-5.
# Add an attribute privileges that stores a list of admins privileges.
# Add an arguments to attribute privileges, like "can add post", "can delete
# post", "can ban user" and so on.
# Write a method called show_pirivleges().
# Method show_pirivleges lists the administrators set of privileges.
# Create an instance of Admin class , call it admin
# Call method show_pirivleges.
class User():
    """A simple attempt to represent user."""

    def __init__(self, first_name, last_name, e_mail,
                phone_number,
                ):
        """Initialize attributes of an user."""
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.phone_number = phone_number
        self.login_attempts = 0

    #  Each call adds 1 to login_attempts.
    def increment_login_attempts(self) :
        """Simulate login attempt by one user at the time."""
        self.login_attempts += 1

    # Reset login_attempts to 0.
    def reset_login_attempts(self):
        """Simulate clear history of login attempts  ."""
        self.login_attempts = 0

class Admin(User):
    """A simple attempt to represent admin."""
    def __init__(self, first_name, last_name,
                e_mail, phone_number,
                ):
        """
        Initialize attributes of the User class.
        Then initialize attributes specific to an admin class.
        """
        super().__init__(first_name, last_name,
                        e_mail, phone_number,
                        )
        self.privileges = ["can delete post", "can add post", "can ban user"]

    def show_pirivleges(self):
        print(f'Admin has this list of privileges:' )
        for privilege in self.privileges:
            print(f'-{privilege}.')

admin = Admin('sergey', 'sergeychev', 'ssergeychev','22232224')
admin.show_pirivleges()
