from Operator import Operator


class Multiply(Operator):
    def __init__(self):
        Operator.__init__(self)
        self.symbol='*'
        self.precedence = 2
        self.associative = 'L'

    def evaluate(self, a, b):
        return a * b
