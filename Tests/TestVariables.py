import unittest

import Main
from Calculator import Calculator


class TestVariables(unittest.TestCase):
    def TestAssign(self):
        c = Calculator()

        Main.calc_exp("i=1", c)
        self.assertTrue(c.v_manager.is_variable("i"))
        self.assertEqual(c.v_manager.get_var_val("i"), 1)

        Main.calc_exp("i=i+1", c)
        self.assertTrue(c.v_manager.is_variable("i"))
        self.assertEqual(c.v_manager.get_var_val("i"), 2)

    def test_inc(self):
        c = Calculator()

        Main.calc_exp("j=1", c)
        Main.calc_exp("j++", c)

        self.assertTrue(c.v_manager.is_variable("j"))
        self.assertEqual(c.v_manager.get_var_val("j"), 2)

        Main.calc_exp("++j", c)

        self.assertEqual(c.v_manager.get_var_val("j"), 3)

    def test_sub(self):
        c = Calculator()

        Main.calc_exp("j=1", c)
        Main.calc_exp("j--", c)

        self.assertTrue(c.v_manager.is_variable("j"))
        self.assertEqual(c.v_manager.get_var_val("j"), 0)

        Main.calc_exp("--j", c)

        self.assertEqual(c.v_manager.get_var_val("j"), -1)

    def test_multiple_vars(self):
        c = Calculator()

        Main.calc_exp("j=1", c)
        Main.calc_exp("i=j", c)
        Main.calc_exp("i++", c)
        Main.calc_exp("t=3", c)
        Main.calc_exp("c=5", c)
        Main.calc_exp("j++", c)
        Main.calc_exp("k=j^(c+t)-i", c)

        self.assertTrue(c.v_manager.is_variable("k"))
        self.assertEqual(c.v_manager.get_var_val("k"), 254)
