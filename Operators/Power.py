from Operator import Operator


class Power(Operator):
    def __init__(self):
        Operator.__init__(self)
        self.symbol='^'
        self.precedence = 4
        self.associative = 'R'

    def evaluate(self, a, b):
        return a ^ b
