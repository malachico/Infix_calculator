import Compiler
from Calculator import Calculator


def print_options():
    print "\noptions:"
    print "status : get current variables stauts"
    print "var = expression : for evaluating exp and assign to var"
    print "options : print options"
    print "quit : exit\n"


def calc_exp(exp, c):
    # Compile exps before evaluation
    exps = Compiler.compile(exp)

    # Evaluate each compiled expression
    for exp in exps:
        c.calc(exp)


if __name__ == '__main__':
    # Create a calculator
    c = Calculator()

    print "Welcome to the coolest calculator CLI!"

    print_options()

    while True:
        exp = raw_input("insert a series : ")
        if exp == "status":
            c.get_status()
            continue

        if exp == "options":
            print_options()
            continue

        if exp == "quit":
            exit(0)

        calc_exp(exp, c)
