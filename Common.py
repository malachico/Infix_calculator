def is_operator(element):
    try:
        return element in "+-*/^"
    except:
        return element.symbol in "+-*/^"


def is_number(element):
    try:
        return element.symbol.isdigit()
    except:
        return element.isdigit()

def is_open_bracket(element):
    return element == "("


def is_close_bracket(element):
    return element == ")"

