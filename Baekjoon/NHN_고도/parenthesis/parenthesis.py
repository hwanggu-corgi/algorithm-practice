#Goal:
#   - Write a program that convert the C expression into the ICPC expression
#       - Is where pairs of parentheses should be used exactly as needed
#       -  uses following symbols (+, -, *, /, and %)
#   - If the expression is not an error in ICPC, then it should not be an error in C
#   - Once it is not an error in C, the usage of parentheses should be checked to determine whether it is a proper expression in ICPC or not.
#   - If the expression is not properly parenthesized, i.e., the number of parentheses is not exact as needed, then it is considered improper
#   - The line should contain one of the following words:
#       - error
#           - if the input C expression is erroneous
#       - proper
#           - print proper if it is parenthesized properly with the exact number
#              of parentheses needed for ICPC
#       - improper.
#           - print if not proper
import re

def main():
    # get input
    expression = input()
    expression = expression.replace(" ", "")
    # check for error
    if is_error_in_expression(expression):
        return "error"
    if is_error_in_parenthesis(expression):
        return "error"
    # check for parenthesis
    if is_proper(expression):
        return "proper"

    return "improper"

def is_error_in_expression(expression):
    # strip out parenthesis
    expression = expression.replace("(", "")
    expression = expression.replace(")", "")

    N = len(expression)

    if N == 0:
        return True

    if N == 1 and not expression.isalpha():
        return True

    if N == 2:
        return True

    # is error when first or last element is not a variable
    if not expression[0].isalpha() or not expression[-1].isalpha():
        return True

    i = 1
    while i < (N-1):
        # is error when element before and after "+", "-", "*", "/", "%" is not a variable
        if ((expression[i] in ["+", "-", "*", "/", "%"]) and
            (not (expression[i-1].isalpha() and expression[i+1].isalpha()))):
            return True

        if ((expression[i].isalpha() and
            (not (expression[i-1] in ["+", "-", "*", "/", "%"]) and
                 (expression[i+1] in ["+", "-", "*", "/", "%"])))):
            return True
        i += 1

    return False

def is_error_in_parenthesis(expression):
    N = len(expression)
    left_brackets = []

    # if parenthesis is not balanced, return error
    for character in expression:
        if character == "(":
            left_brackets.append(character)

        if character == ")":
            if len(left_brackets) == 0:
                return True
            left_brackets.pop()

    if len(left_brackets) != 0:
        return True

    # if parenthesis is not surrounded by expression properly return error
    i = 1
    while i < N:
        if ((expression[i-1] == "(" and expression[i] != "(") and
            (expression[i-1] == "(" and not expression[i].isalpha())):
            return True

        if ((expression[i] == ")" and expression[i-1] != ")") and
            (expression[i] == ")" and not expression[i-1].isalpha())):
            return True

        i += 1

    return False

def is_proper(expression):
    # set all letters as a
    expression = re.sub(r'\w', 'a', expression)
    # set all expressions as +
    expression = re.sub(r'[\+\-\/\*\%]', '+', expression)

    return _is_proper(expression)

def _is_proper(expression):
     # until the index for left bracket and right bracket cross
    N = len(expression)

    if expression == "a+a":
        return True

    if N == 1 and expression.isalpha():
        return True

    if N == 2:
        return False

    index_left_bracket = find_index_left_bracket(expression)
    index_right_bracket = find_index_right_bracket(expression)

    if ((index_left_bracket >= N and index_right_bracket < 0) and
        len(expression) != 0):
        return False

    # set all expressions between left bracket and right bracket to b
    test = expression[:index_left_bracket] + "b" + expression[index_right_bracket + 1:]
    # check if expression is in form
    if not (test == "b+a" or test == "a+b"):
        return False

    # take out all outer expressions including parenthesis at index_left_bracket and index_right_bracket

    expression = expression[index_left_bracket + 1: index_right_bracket]

    return _is_proper(expression)

def find_index_left_bracket(expression):
    i = 0
    N = len(expression)
    while i < N:
        if expression[i] == "(":
            return i
        i += 1

    return i

def find_index_right_bracket(expression):
    N = len(expression)
    i = N - 1

    while i >= 0:
        if expression[i] == ")":
            return i
        i -= 1

    return i

if __name__ == "__main__":
    print(main())