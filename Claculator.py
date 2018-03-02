def format_input(user_input):
    pass


def build_tree(user_input):
    t = InfixTree(user_input)


class Calculator():

    def __init__(self):
        self.variables ={}

    def print_status(self):
        pass

    def calc(self, user_input):
        user_input = format_input(user_input)
        tree = build_tree(user_input)



