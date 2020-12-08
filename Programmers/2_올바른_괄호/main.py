# goal: '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를
# return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

def solution(s):
    answer = True
    stack = []

    for parenthesis in s:
        if parenthesis == "(":
            stack.append(parenthesis)
            continue
        else:
            if len(stack) == 0:
                return False

            stack.pop()

    if len(stack) > 0:
        return False

    return True

if __name__ == "__main__":
    print(solution("()()")) #true
    print(solution("")) #true
    print(solution(")()(")) #false
    print(solution("(()(")) #false
    print(solution("(())()")) #true