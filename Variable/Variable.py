from Element import Element
from Operands.Operand import Operand


class Variable(Element):
    def __init__(self, symbol, value=None):
        Element.__init__(self)
        self.value = value
        self.symbol = str(symbol)

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Operand(self.value + other.value)

    def __sub__(self, other):
        return Operand(self.value - other.value)

    def __div__(self, other):
        return Operand(self.value / other.value)

    def __mul__(self, other):
        return Operand(self.value * other.value)

    def __pow__(self, power, modulo=None):
        return Operand(self.value ** power.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
