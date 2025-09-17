import unittest
from calc import Calculator
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.calculator = Calculator()
  #Each test method starts with the keyword test_
    def test_add(self):
        self.assertEqual(self.calculator.add(4,7), 11)
        
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10,5), 5)
        
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3,7), 21)
        
    def test_divide(self):
        self.assertEqual(self.calculator.divide(10,2), 5)
        
    def test_koren(self):
        self.assertEqual(self.calculator.koren(64), 8)
        
    def test_stepen(self):
        self.assertEqual(self.calculator.stepen(10,2), 100)
        
    def test_modul(self):
        self.assertEqual(self.calculator.modul(-2), 2)
        self.assertEqual(self.calculator.modul(2), 2)
        
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()