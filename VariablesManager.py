from Variable.Variable import Variable


class VariablesManager:
    """
    This class keep track of variables and their values
    """

    def __init__(self):
        self.variables = []

    def is_variable(self, var):
        return var in map(lambda x: x.symbol, self.variables)

    def assign_variable(self, variable, result):
        """
        assign or update variable
        :param variable: variable to assign / update
        :param result:
        """
        # If the variable already exists
        if not self.is_variable(variable):
            var = Variable(variable, result)
            self.variables.append(var)
        else:
            var = filter(lambda x: x.symbol == variable, self.variables)[0]
            var.value = result

    def get_var_val(self, variable):
        """
        :param variable:
        :return: value of variable
        """
        var = filter(lambda v: v.symbol == variable, self.variables)
        if not var:
            Exception("no variable " + variable)
        return var[0].value
