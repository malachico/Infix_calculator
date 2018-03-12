from Element import Element


class Operand(Element):
    def __init__(self, value):
        Element.__init__(self)
        self.value = int(value)
        self.symbol = str(value)

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
