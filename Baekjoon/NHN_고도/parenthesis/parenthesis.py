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

def main():
    # get input
    expression = input()
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
    expression.replace("(", "")
    expression.replace(")", "")

    expression = expression.split()
    N = len(expression)

    i = 1
    while i < N:
        # is error when first element is not a variable
        if i == 1:
            if not expression[i-1].isalpha():
                return False

        # is error when element after "+", "-", "*", "/" is not a variable
        # is error when element before "+", "-", "*", "/" is not a variable
        elif i != 0 and i != (N-1):
            if ((expression[i] is in ["+", "-", "*", "/"]) and
                (not (expression[i-1].isalpha() and expression[i+1].isalpha()))):

                return False

        # is error when last element is not a variable
        # i == (N-1)
        else:
            if not expression[i-1].isalpha():
                return False

        i += 1

    return True

def is_error_in_parenthesis(expression):
    # if parenthesis is not balanced, return error

    # if parenthesis is not surrounded by expression properly return error

def is_proper(expression):
    # if proper expression is contained in
    # is not proper when
    return True

if __name__ == "__main__":
    print(main())