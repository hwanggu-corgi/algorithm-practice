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
    # is error when first and last element are not variables
    # is error when expression between variable is not an expression (+, -, *, /, and %)
    pass

def is_proper(expression):
    pass

if __name__ == "__main__":
    print(main())