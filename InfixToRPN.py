from collections import deque

from Brackets.OpenBracket import OpenBracket
from Operands.Operand import Operand
from Operators.Division import Division
from Operators.Minus import Minus
from Operators.Multiply import Multiply
from Operators.Plus import Plus
from Operators.Power import Power


def is_operator(element):
    return element in "+-*/^"


def create_operator(element):
    operators_creators = {
        "+": Plus(),
        "-": Minus(),
        "*": Multiply(),
        "/": Division(),
        "^": Power(),
    }
    return operators_creators[element]


def is_number(element):
    return element.isdigit()


def is_open_bracket(element):
    return element == "("


def is_close_bracket(element):
    return element == ")"


def convert_infix(infix):
    stack = []
    queue = deque()

    for element in infix:

        if is_number(element):
            queue.append(Operand(element))
            continue

        if is_operator(element):
            operator = create_operator(element)
            if len(stack):
                top = stack[-1]

                while (is_operator(top.symbol) and top.precedence > operator.precedence) or (
                        is_operator(top.symbol) and top.precedence == operator.precedence and operator.associative == 'L') and (top.symbol != ')'):
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
