# Add an attribute called login_attempts to your User class from ex.9-3.
# Write a method called increment_login_attempts.
# The method increment_login_attempts, increment value of login_attempts by 1.
# Write a method reset_login_attempts.
# The method reset_login_attempts, resets the value of login_attempts to 0.
# Make an instance of the User class, called it user.
# Call method increment_login_attempts() several times.
# Print value of login_attempts.
# Call method reset_login_attempts.
# Print value of  login_attempts.

class User():
    """A simple attempt to represent user."""

    def __init__(self, first_name, last_name, e_mail,
                phone_number, login_attempts=0,
                ):
        """Initialize attributes of an user."""
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.phone_number = phone_number
        self.login_attempts = login_attempts

    #  Each call adds 1 to login_attempts.
    def increment_login_attempts(self) :
        """Simulate login attempt by one user at the time."""
        self.login_attempts += 1

    # Reset login_attempts to 0.
    def reset_login_attempts(self):
        """Simulate clear history of login attempts  ."""
        self.login_attempts = 0

user = User('sergey', 'sergeychev', 'ssergeychev@inbox.lv', 23332444)
user.increment_login_attempts()
print(f'Our webpage has been visited {user.login_attempts} users.')
user.increment_login_attempts()
print(f'Our webpage has been visited {user.login_attempts} users.')
user.reset_login_attempts()
print(f'Our webpage has been visited {user.login_attempts} users.')
