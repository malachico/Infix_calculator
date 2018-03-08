import re
from collections import deque

from Brackets.OpenBracket import OpenBracket
from Common import *
from Operands.Operand import Operand
from Operators.Division import Division
from Operators.Minus import Minus
from Operators.Multiply import Multiply
from Operators.Plus import Plus
from Operators.Power import Power


def create_operator(element):
    operators_creators = {
        "+": Plus(),
        "-": Minus(),
        "*": Multiply(),
        "/": Division(),
        "^": Power(),
    }
    return operators_creators[element]


def split_elements(infix):
    # Remove spaces
    infix = infix.replace(" ", "")

    splitted = re.split(r'(\+|\-|\*|\/|\(|\)|\^)', infix)

    # Remove emptys
    splitted = filter(None, splitted)

    return splitted


def convert_infix(infix, vars):
    stack = []
    queue = deque()

    splitted = split_elements(infix)
    for element in splitted:

        if is_number(element):
            queue.append(Operand(element))
            continue

        if vars.is_variable(element):
            operand = vars.get_var_val(element)
            queue.append(operand)
            continue

        if is_operator(element):
            operator = create_operator(element)
            if len(stack):
                top = stack[-1]

                while (is_operator(top) and top.precedence > operator.precedence) or (
                                is_operator(
                                    top) and top.precedence == operator.precedence and operator.associative == 'L') and (
                            top.symbol != ')'):
                    queue.append(stack.pop())
                    if not stack:
                        break
                    top = stack[-1]

            stack.append(operator)
            continue

        if is_open_bracket(element):
            stack.append(OpenBracket())
            continue

        if is_close_bracket(element):
            while stack[-1].symbol != '(':
                queue.append(stack.pop())
            stack.pop()

    while stack:
        queue.append(stack.pop())

    return list(queue)
