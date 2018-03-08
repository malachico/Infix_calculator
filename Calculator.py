import InfixToRPN
import RPNCalculator
from VariablesManager import VariablesManager


class Calculator:
    def __init__(self):
        self.v_manager = VariablesManager()

    def calc(self, exp):
        variable = None

        if "=" in exp:
            variable, exp = exp.split("=")

        RPN = InfixToRPN.convert_infix(exp, self.v_manager)

        result = RPNCalculator.calc_expression(RPN, self.v_manager, [])

        if variable:
            self.v_manager.assign_variable(variable, result)

        else:
            return result

    def get_status(self):
        for var in self.v_manager.variables:
            print var.symbol, "=", var.value
