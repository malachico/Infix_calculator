from Operator import Operator


class Division(Operator):
    def __init__(self):
        Operator.__init__(self)
        self.symbol = '/'
        self.precedence = 2
        self.associative = 'L'

    def evaluate(self, a, b):
        return b / a
