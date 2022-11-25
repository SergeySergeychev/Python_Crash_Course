class User():
    """Description of an user."""
    
    def __init__(self, first_name, last_name, age, height):
        """Infromation about an user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = 0
        
    def describe_user(self):
        """Prints out infromation about user."""
        print("\nFirst name: " + self.first_name.title() + ".")
        print("\nLast name: " + self.last_name.title() + ".")
        print("\nUser's age: " + str(self.age) + ".")
        print("\nUser's height: " + str(self.height) + ".")
        
    def greet_user(self):
        """Greetings to an user."""
        print("\nI want to greet you "  + self.first_name.title() + ' ' + self.last_name.title() + ".")
        
    def increment_login_attempts(self):
        """Increments login attempts by 1."""
        self.login_attempts += 1
        print("The number of login attempts: " + str(self.login_attempts) + ".")
        
    def reset_login_attempts(self):
        """Resetes  login attempts to 0."""
        self.login_attempts = 0 
