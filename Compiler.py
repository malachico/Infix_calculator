from operator import attrgetter


class Expression:
    def __init__(self, expression, precedence=0):
        self.expression = expression
        self.precedence = precedence


def handle_inc(exp):
    exps = []
    if "++" in exp:
        elements = exp.split(" ")
        elements = filter(lambda x: '++' in x, elements)
        for elem in elements:
            reduced = elem.replace("++", "")
            e = Expression(reduced + "=" + reduced + "+1")
            if elem.startswith("++"):
                e.precedence = -1
            elif elem.endswith("++"):
                e.precedence = 1
            else:
                Exception("++ : incorrect format")

            exps.append(e)

    return exps


def handle_sub(exp):
    exps = []
    if "--" in exp:
        elements = exp.split(" ")
        elements = filter(lambda x: '--' in x, elements)
        for e in elements:
            reduced = e.replace("--", "")
            e = Expression(reduced + "=" + reduced + "-1")
            if e.expression.startswith("--"):
                e.precedence = -1
            elif e.expression.endswith("--"):
                e.precedence = 1
            else:
                Exception("-- : incorrect format")

            exps.append(e)

    return exps


def handle_plus_eq(exp):
    ops = "+-*/^"

    for op in ops:
        if op + "=" in exp:
            splitted = exp.split(op + "=")
            exp = splitted[0] + "=" + splitted[0] + op + "(" + splitted[1] + ")"

    return exp


def compile(exp):
    # Handle +=
    exp = handle_plus_eq(exp)

    e = Expression(exp, 0)

    exps = [e]
    # Handle ++ and -- expressions
    exps += handle_inc(exp)
    exps += handle_sub(exp)

    # Remove after handling
    for e in exps:
        e.expression = e.expression.replace("++", "")
        e.expression = e.expression.replace("--", "")

    # sort by precedence
    exps = sorted(exps, key=attrgetter('precedence'))

    return map(lambda e: e.expression, exps)
