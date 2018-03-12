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

"""
This class is converting infix to RPN expression using the Shunting-yard algorithm
using the instructions in: 
https://en.wikipedia.org/wiki/Shunting-yard_algorithm
"""


def create_operator(element):
    # Jump table for creating operators
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

    # Split by operators
    splitted = re.split(r'(\+|\-|\*|\/|\(|\)|\^)', infix)

    # Remove empty elements
    splitted = filter(None, splitted)

    return splitted


def convert_infix(infix, vars):
    stack = []
    queue = deque()

    splitted = split_elements(infix)

    for element in splitted:
        # If is number add it to queue
        if is_number(element):
            queue.append(Operand(element))
            continue
        # If is variable add it to queue
        if vars.is_variable(element):
            operand = vars.get_var_val(element)
            queue.append(operand)
            continue

        # if is operator
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

        # if open bracket add to queue
        if is_open_bracket(element):
            stack.append(OpenBracket())
            continue

        # if close bracket add to queue from stack until open bracket is found
        if is_close_bracket(element):
            while not is_open_bracket(stack[-1]):
                queue.append(stack.pop())
            stack.pop()

    # while there are still operator tokens on the stack pop to the queue
    while stack:
        queue.append(stack.pop())

    return list(queue)
