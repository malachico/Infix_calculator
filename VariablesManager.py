from Variable.Variable import Variable


class VariablesManager():
    def __init__(self):
        self.variables = []

    def is_variable(self, var):
        return var in map(lambda x: x.symbol, self.variables)

    def assign_variable(self, variable, result):
        # If the variable already exists
        if not self.is_variable(variable):
            var = Variable(variable, result)
            self.variables.append(var)
        else:
            var = filter(lambda x: x.symbol == variable, self.variables)[0]
            var.value = result

    def get_var_val(self, variable):
        var = filter(lambda v: v.symbol == variable, self.variables)
        if not var:
            Exception("no variable " + variable)
        return var[0].value