# Write separate Privileges class.
# The class should have one attribute, privileges.
# Attributes stores a list of admin's privileges.
# Write method show_pirivleges()
# Method show_pirivleges has to show all privileges of an admin.
# Make a Privileges instance as an attribute in the Admin class
# Create a new instance of Admin and use your method to show its privileges.
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
        # Privileges instance is an attribute of the Admin class.
        self.privileges = Privileges()


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        """Initialize attributes of the Privilegs class"""
        self.privileges = privileges

    def show_privileges(self):
        """
        Check does the list if full or empty.
        If list if full, print out privilegs.
        If listt is empty, print out statement , that list is empty.
        """
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f'- {privilege}')
        else:
            print("- This user has no privileges.")

eric = Admin('eric','matthes','e_matthes@example.com', '22232224' )\
# Checking does eric as admin has any privilegs...
eric.privileges.show_privileges()
# Create variable with list of strings
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
