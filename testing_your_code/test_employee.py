import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee. """

    def setUp(self):
        """
        Create an object employee and use it's attributes in all instances.
        """
        fname, lname, annual_salary = 'Sergey', 'Sergeychev', 20000
        self.employee = Employee(fname, lname, annual_salary)

    def test_give_default_raise(self):
        """Check if give_raise() adds +5k to annual_salary."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 25000)
    def test_give_custom_raise(self):
        """
        Check if give_raise() accepts raise parameter.
        Parameters value should be added to annual_salary.
        """
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 30000)
unittest.main()
