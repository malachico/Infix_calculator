from Common import *


def calc_expression(exp, v_manager, stack):
    if not exp:
        if not stack:
            return 0
        return stack[0]

    current = exp.pop(0)

    if v_manager.is_variable(current):
        stack.append(current)
        return calc_expression(exp,v_manager, stack)

    if is_number(current):
        stack.append(current)
        return calc_expression(exp, v_manager, stack)

    if is_operator(current):
        operand1 = stack.pop()
        operand2 = stack.pop()
        result = current.evaluate(operand1, operand2)
        stack.append(result)
        return calc_expression(exp, v_manager, stack)


