import unittest

import Compiler


class TestCompiler(unittest.TestCase):
    def test_op_eq(self):
        self.assertEqual(Compiler.compile("i+=1"), ['i=i+(1)'])
        self.assertEqual(Compiler.compile("i-=1"), ['i=i-(1)'])
        self.assertEqual(Compiler.compile("i*=1"), ['i=i*(1)'])
        self.assertEqual(Compiler.compile("i/=1"), ['i=i/(1)'])
        self.assertEqual(Compiler.compile("i^=1"), ['i=i^(1)'])

    def test1(self):
        self.assertEqual(Compiler.compile(""), [''])
        self.assertEqual(Compiler.compile("i=1+2"), ['i=1+2'])
        self.assertEqual(Compiler.compile("i++"), ['i', 'i=i+1'])
