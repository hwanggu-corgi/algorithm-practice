# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: Write a function that given a string S consisting of N characters,
# returns 1 if S is properly nested and 0 otherwise.

class BracketStack:
    def __init__(self):
        self.left_brackets = []

    def push(self, left_bracket):
        self.left_brackets.append(bracket)

    def pop(self):
        if len(self.left_brackets) == 0:
            return ''
        else:
            return self.left_brackets.pop()

def solution(S):
    # write your code in Python 3.6

    # initialize Bracket
    left_brackets = BracketStack()

    # for each bracket in S
    for bracket in S:
        # if bracket is left bracket, then push to Bracket
        if bracket in ["(", "[", "{"]:
            left_brackets.push(brack)
        else:
            # if bracket is right bracket, then pop from the Bracket
            left_bracket = left_brackets.pop()

            # if brackets don't match return 0
            if ((bracket == ")" and left_bracket != "(") or
                (bracket == "]" and left_bracket != "[") or
                (bracket == "}" and left_bracket != "{")):
                return 0
        # if brackets match keep going

    # if all is well, return 1
    return 1
