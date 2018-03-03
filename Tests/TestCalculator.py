import unittest

from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test1(self):
        c = Calculator()

        self.assertEqual(c.calc("1+2"), 3)
        self.assertEqual(c.calc("1-2"), -1)
        self.assertEqual(c.calc("3^2"), 9)
        self.assertEqual(c.calc("5*4"), 20)
        self.assertEqual(c.calc("10/2"), 5)

        self.assertEqual(c.calc("(1+2)"), 3)
        self.assertEqual(c.calc("(1-2)"), -1)
        self.assertEqual(c.calc("(3^2)"), 9)
        self.assertEqual(c.calc("(5*4)"), 20)
        self.assertEqual(c.calc("(10/2)"), 5)

        self.assertEqual(c.calc("10/2+3"), 8)
        self.assertEqual(c.calc("10/(2+3)"), 2)
        self.assertEqual(c.calc("7-(1+1)"), 5)



