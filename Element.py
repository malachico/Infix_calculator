"""
an abstract class represent an element in the calculator.
such as brackets, numbers, operators and operands
"""


class Element:
    def __init__(self):
        self.symbol = ""

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.symbol == other

    def __ne__(self, other):
        return not self.__eq__(other)
