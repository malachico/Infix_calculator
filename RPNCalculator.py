from Common import *


def calc_expression(exp, v_manager, stack):
    # If the expression is empty
    if not exp:
        # If stack is empty
        if not stack:
            return 0
        # Return the result
        return stack[0]

    # Get the current element
    current = exp.pop(0)

    # If is variable add it to stack
    if v_manager.is_variable(current):
        stack.append(current)
        return calc_expression(exp, v_manager, stack)

    # If is number add it ti stack
    if is_number(current):
        stack.append(current)
        return calc_expression(exp, v_manager, stack)

    # If is operator - calc the result and push to stack
    if is_operator(current):
        operand1 = stack.pop()
        operand2 = stack.pop()
        result = current.evaluate(operand1, operand2)
        stack.append(result)
        return calc_expression(exp, v_manager, stack)
