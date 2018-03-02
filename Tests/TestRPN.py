# tests
import unittest

import InfixToRPN


class TestRPN(unittest.TestCase):
    def testsimple(self):
        self.assertEqual(InfixToRPN.convert_infix(["1", "+", "2"]), ["1", "2", "+"])
        self.assertEqual(InfixToRPN.convert_infix([]), [])
        # self.assertEqual(InfixToRPN.convert_infix(["3","+","4", "*", "2", "/", "(", "1", "-", "5", ")", "^", "2", "^", "3"]), [])
        print InfixToRPN.convert_infix(["3","+","4", "*", "2", "/", "(", "1", "-", "5", ")", "^", "2", "^", "3"])
