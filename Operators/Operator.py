from abc import abstractproperty, abstractmethod

from Element import Element


class Operator(Element):
    def __init__(self):
        Element.__init__(self)

    @abstractproperty
    def precedence(self):
        pass

    @abstractproperty
    def associative(self):
        pass

    @abstractmethod
    def evaluate(self, a, b):
        pass
