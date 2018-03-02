from Operator import Operator

class Minus(Operator):
    def __init__(self):
        Operator.__init__(self)
        self.symbol='-'
        self.precedence = 1
        self.associative = 'L'

    def evaluate(self, a, b):
        return a - b
