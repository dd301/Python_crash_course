import unittest

class Employee():
    def __init__(self, first, last, ann_salary):
        self.first = first
        self.last = last
        self.ann_salary = ann_salary
    
    def give_raise(self, raise_amount=5000):
        self.ann_salary += raise_amount

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Joe', 'Rogan', 200000)
        
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.ann_salary, 200000 + 5000)
    
    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.ann_salary, 200000 + 10000) 

unittest.main()