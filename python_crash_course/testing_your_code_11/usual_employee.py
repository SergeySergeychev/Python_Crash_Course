
class Employee():
    """A simple attempt to represent life of an employee."""
    
    def __init__(self, f_name, l_name,annual_salary):
        """Initialize attributes to describe employee"""
        self.f_name = f_name
        self.l_name = l_name
        self.annual_salary = annual_salary 
        
    def give_raise(self, custom_raise=0):
        """A simple attempt to represent raising of an annual salary"""
        default_raise = 5000
        self.annual_salary+= custom_raise + default_raise
        print("Congrtulations, your salary now is " + 
              str(self.annual_salary) + "$"
             )