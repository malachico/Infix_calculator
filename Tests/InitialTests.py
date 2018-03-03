import unittest

import Main
from Calculator import Calculator


class TestVariables(unittest.TestCase):
    def testAssign(self):
        c= Calculator()
        Main.calc_exp("i=0", c)
        Main.calc_exp("j= ++i", c)
        Main.calc_exp("x= i++ + 5", c)
        Main.calc_exp("y=5+3*10", c)
        Main.calc_exp("i+=y", c)

        self.assertTrue(c.v_manager.is_variable("i"))
        self.assertEqual(c.v_manager.get_var_val("i"), 37)

        self.assertTrue(c.v_manager.is_variable("j"))
        self.assertEqual(c.v_manager.get_var_val("j"), 1)

        self.assertTrue(c.v_manager.is_variable("x"))
        self.assertEqual(c.v_manager.get_var_val("x"), 6)

        self.assertTrue(c.v_manager.is_variable("y"))
        self.assertEqual(c.v_manager.get_var_val("y"), 35)



