# goal: Given  strings of brackets, determine whether each sequence of brackets
#       is balanced. If a string is balanced, return YES. Otherwise, return NO.

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []

    for bracket in s:
        # if it's left bracket then append to array
        if bracket in ['[', '(', '{']:
            stack.append(bracket)

        # if it's right bracket then pop from array
        else:
            if len(stack) == 0:
                return "NO"

            left_bracket = stack.pop()

            # check if popped bracket matches the right bracket
            if ((bracket == ']' and left_bracket == '[') or
                (bracket == ')' and left_bracket == '(') or
                (bracket == '}' and left_bracket == '{')):

                continue

            # if not match, then return NO
            else:
                return "NO"


    # if array is non-empty, return NO
    if len(stack) > 0:
        return "NO"

    # if all is well, return YES
    return "YES"

if __name__ == "__main__":
    print(isBalanced("{[()]}")) # YES
    print(isBalanced("{[()]")) # NO
    print(isBalanced("{{[[(())]]}}")) # YES