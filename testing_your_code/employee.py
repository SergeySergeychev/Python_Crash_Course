class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary=int()):
        """Initialize all atributes of class employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=int(5000)):
        """Function that adds to annual salary 5k."""
        self.annual_salary += raise_amount
