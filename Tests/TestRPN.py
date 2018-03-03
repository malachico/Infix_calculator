import unittest

import InfixToRPN
from Calculator import Calculator
from Operators.Division import Division
from Operators.Minus import Minus
from Operators.Multiply import Multiply
from Operators.Plus import Plus
from Operators.Power import Power


class TestRPN(unittest.TestCase):
    def testsimple(self):
        c= Calculator()

        self.assertEqual(InfixToRPN.convert_infix("", c.v_manager),  [])
        self.assertEqual(InfixToRPN.convert_infix("1+2",c.v_manager), [1, 2, Plus()])

        self.assertEqual(
            InfixToRPN.convert_infix("3 +4*2/ (1-5)^2^3", c.v_manager),
            [3, 4, 2, Multiply(), 1, 5, Minus(), 2, 3, Power(), Power(), Division(), Plus()])

        self.assertEqual(InfixToRPN.convert_infix("10 /2",c.v_manager), [10, 2, Division()])

    def test_split(self):
        self.assertEqual(InfixToRPN.split_elements(""), [])
        self.assertEqual(InfixToRPN.split_elements("1+2"), ["1", "+", "2"])
        self.assertEqual(InfixToRPN.split_elements("1^2"), ["1", "^", "2"])
        self.assertEqual(InfixToRPN.split_elements("1*2"), ["1", "*", "2"])
        self.assertEqual(InfixToRPN.split_elements("1/2"), ["1", "/", "2"])
        self.assertEqual(InfixToRPN.split_elements("(1/2)"), ["(", "1", "/", "2", ")"])
        self.assertEqual(InfixToRPN.split_elements("1+2-3 ^ 4 - 6"), ['1', '+', '2', '-', '3', "^", "4", "-", "6"])
