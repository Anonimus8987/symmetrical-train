import unittest

class Calculator:
    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def subtract(self, x, y):
        return x - y

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        self.assertEqual(self.calculator.multiply(-2, 5), -10)
        self.assertEqual(self.calculator.multiply(0, 7), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(8, 4), 2)
        self.assertAlmostEqual(self.calculator.divide(5, 3), 1.6666666666666667, places=7)
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(8, 3), 5)
        self.assertEqual(self.calculator.subtract(5, 5), 0)
        self.assertEqual(self.calculator.subtract(-2, 6), -8)


    unittest.main()
