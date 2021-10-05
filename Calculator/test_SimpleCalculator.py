# Import Unit Test module
import unittest

# Import Calculator module
from SimpleCalculator import SimpleCalculator


class Test_Calculator(unittest.TestCase):

    # Init for Unit Test
    def setUp(self):
        self.calculator = SimpleCalculator()

    # Try various functions
    def test_add(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertNotEqual(self.calculator.add(1, 1), 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertNotEqual(self.calculator.subtract(1, 1), 3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(-1, -1), 1)
        self.assertNotEqual(self.calculator.multiply(1, 1), 3)

    def test_divide(self):
        self.assertEqual(self.calculator.multiply(-2, -1), 2)
        self.assertNotEqual(self.calculator.multiply(1, 1), 3)

    def test_divide_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 1, 0)

    def test_add_negative(self):
        self.assertRaises(ValueError, self.calculator.no_negative_add, -1, 0)


if __name__ == '__main__':
    unittest.main()
