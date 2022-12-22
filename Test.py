import unittest
from main import Calculator
class Test(unittest.TestCase):
  def setUp(self):
    self.calculator = Calculator()
  def test_addition(self):
    self.assertEqual(self.calculator.addition(2,2), 4)
  def test_subtraction(self):
    self.assertEqual(self.calculator.subtraction(4,2), 2)
  def test_multiplication(self):
    self.assertEqual(self.calculator.multiplication(3,2), 6)
  def test_division(self):
    self.assertEqual(self.calculator.division(10,2), 5)
  def test_mod(self):
    self.assertEqual(self.calculator.mod(10,3),1)

if __name__ == "__main__":
  unittest.main()