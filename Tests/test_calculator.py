# tests
import unittest

from Claculator import Calculator


class ArraysAndStringsTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(Calculator.calc("i++"))