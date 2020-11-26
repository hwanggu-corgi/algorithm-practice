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
    left_brackets = []

    for character in expression:
        if character == "(":
            left_brackets.append(character)

        if character == ")":
            if len(left_bracket) == 0:
                return True
            left_brackets.pop()


    # if parenthesis is not surrounded by expression properly return error
    i = 1
    while i < N:
        if ((not (expression[i-1] == "(" and expression[i] == "(")) and
            (not (expression[i-1] == "(" and expression[i] == ")")) and
            (not (expression[i-1] == "(" and expression[i].isalpha()))):

            return True

        if ((not (expression[i] == ")" and expression[i-1] == ")")) and
            (not (expression[i] == ")" and expression[i-1] == "(")) and
            (not (expression[i] == ")" and expression[i-1].isalpha()))):

            return True

    return False

def is_proper(expression):
    # set all letters as a
    # set all expressions as +

    if expression[0] == "(" and expression[-1] == ")":
        return False

    # until the index for left bracket and right bracket cross
    while len(expression) != 0:
        # find location of left brackets
        # find location of right brackets
        index_left_bracket = re.search(r'^\(', expression).start()
        index_right_bracket = re.search(r'\)$', expression).end()

        # set all expressions between left bracket and right bracket to b
        # check if expression is in form

        # take out all outer expressions including parenthesis at index_left_bracket and index_right_bracket
        expression = expression[index_right_bracket + 1: index_right_bracket - 1]
        if len(expression) == 1:
            return False
    return True

f

if __name__ == "__main__":
    print(main())