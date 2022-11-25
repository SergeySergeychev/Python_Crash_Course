"""Import User class to admin module"""
from user import User

class Privileges():
    """A simple attempt to represent privileges"""
    def __init__(self,privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        print("\nAdministrators set of privileges:")
        for privileges in self.privileges:
            print("- " + privileges)            
        
class Admin(User):
    """A simple attempt to represent Admin"""
    def __init__(self, first_name, last_name, age, height):
        """Initialize attributs from User class."""
        super().__init__(first_name, last_name, age, height)
        self.privileges = Privileges()