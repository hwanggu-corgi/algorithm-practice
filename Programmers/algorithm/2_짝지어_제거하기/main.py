# goal: 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요

# 제한사항
#   문자열의 길이 : 1,000,000이하의 자연수
#   문자열은 모두 소문자로 이루어져 있습니다.

# Example
#   1. baabaa
#       1) bbaa
#       2) aa
#       3)      -> return 1
#

#   2. cdcd
#       1) cdcd     -> doesn't exist. cannot be removed anymore
#                   -> return 0

# pseudocode
#   search for first repeating characters
#   if it exists, show where it starts
#       remove characters
#   if it doesn't exist, return 0


def solution(s):
    answer = 0
    stack = []

    if len(s) == 0:
        return 0

    for letter in s:
        if len(stack) == 0:
            stack.append(letter)
            continue

        if stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)

    if len(stack) == 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    print(solution("baabaa")) #1
    print(solution("cdcd")) #0