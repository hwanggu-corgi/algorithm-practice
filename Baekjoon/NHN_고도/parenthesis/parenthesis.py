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
    expression = input().split()
    # check for error
    if is_error(expression):
        return "error"
    # check for parenthesis
    if is_proper(expression):
        return "proper"

    return "improper"

def is_error(expression):
    N = len(expression)

    i =1
    while i < N:
        # is error when first and last element are not variables
        if i == 1 or i == (N-1):
            if not expression[i-1].isalpha():
                return False

            if expression[i] not in ["+", "-", "*", "/", "%"]:
                return False

        if i != 0 and i != (N-1):
            if
        # is error when expression between variable is not an expression (+, -, *, /, and %)

        # is error when element after ( is not ( or a variable
        # is error when element before ) is not ) or a variable

        i += 1

    return True

def is_proper(expression):
    # if proper expression is contained in
    # is not proper when
    return True

if __name__ == "__main__":
    print(main())