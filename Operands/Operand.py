from Element import Element


class Operand(Element):
    def __init__(self, value):
        Element.__init__(self)
        self.value = value
        self.symbol = str(value)