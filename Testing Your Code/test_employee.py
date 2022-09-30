import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """An employee to be used in tests"""
        self.employee1 = Employee('bruce', 'wayne', 420000)


    def test_give_default_raise(self):
        """Test the default raise amount"""
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary, 425000)

    
    def test_give_custom_raise(self):
        """Test the custom raise amount"""
        self.employee1.give_raise(69000)
        self.assertEqual(self.employee1.annual_salary, 489000)


if __name__ == '__main__':
    unittest.main()