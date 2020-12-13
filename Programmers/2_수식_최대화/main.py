# goal 참가자에게 주어진 연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때, 우승 시 받을 수
# 있는 가장 큰 상금 금액을 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
#   - expression은 길이가 3 이상 100 이하인 문자열입니다.
#   - expression은 공백문자, 괄호문자 없이 오로지 숫자와 3가지의 연산자(+, -, *) 만으로 이루어진 올바른 중위표기법(연산의 두 대상 사이에 연산기호를 사용하는 방식)으로 표현된 연산식입니다. 잘못된 연산식은 입력으로 주어지지 않습니다.
#       - 즉, "402+-561*"처럼 잘못된 수식은 올바른 중위표기법이 아니므로 주어지지 않습니다.
#   - expression의 피연산자(operand)는 0 이상 999 이하의 숫자입니다.
#       - 즉, "100-2145*458+12"처럼 999를 초과하는 피연산자가 포함된 수식은 입력으로 주어지지 않습니다.
#       - "-56+100"처럼 피연산자가 음수인 수식도 입력으로 주어지지 않습니다.
#   - expression은 적어도 1개 이상의 연산자를 포함하고 있습니다.
#   - 연산자 우선순위를 어떻게 적용하더라도, expression의 중간 계산값과 최종 결괏값은 절댓값이 263 - 1 이하가 되도록 입력이 주어집니다.
#   - 같은 연산자끼리는 앞에 있는 것의 우선순위가 더 높습니다.


# Example
#   1) 100-200*300-500+20 Ans:60420
#       using combination * > + > -
#           100-(200*300)-500+20
#           100-60000-(500+20)
#           (100-60000)-520
#           -59900-520
#           |-60420|
#           60420

# Cases
#   When consists only of positive number
#   When consists only of negative number
#   When consists of both positive and negative number

# Pseudocode
#   get combination of operands
#   for each combination, starting from left most operand perform calculation
#   if the current calculated value is greater than highest value, replace

#   return calculated value


# ===========

# Example in detail

# 5 + 5
#
#   5 + 5
#   ^
#   number [5]
#   operand [+]
#   expression queue [+,5]
#   new expression queue []

#   5 + 5
#     ^
#   number queue [5]
#   operand queue [+]
#   expression queue [5]
#   new expression queue []

#   5 + 5
#       ^
#   number queue [5,5]
#   operand queue [+]
#   expression queue []
#   new expression queue []

#   5 + 5
#       ^
#   number queue []
#   operand queue []
#   expression queue []
#   new expression queue [10]


# Example 2: "100-200*300-500+20"

#   100-200*300-500+20
#    ^
#   number queue []
#   operand queue []
#   expression queue [100,-,200,*,300,-,500,+,20]
#   new expression queue []

from itertools import permutations
import sys

def solution(expression):
    answer = 0
    highest_value = -sys.maxsize
    operands = ["+", "*", "-"]
    # get combination of operands
    perms = permutations(operands, len(operands))

    # for each combination, starting from left most operand perform calculation
    for permutation in perms:
        calculated_value = abs(calculate(expression, permutation))
        # if the current calculated value is greater than highest value, replace
        highest_value = max(highest_value, calculated_value)
    # return calculated value
    answer = highest_value
    return answer

def calculate(expression, permutation):
    value = 0
    current_expression = expression

    for target_operand in permutation:
        i = current_expression.find(target_operand)
        while i > 0:
            # find signs and numbers around operand
            index_start = get_expression_start(i, current_expression)
            index_end = get_expression_end(i, current_expression)

            # use python's eval to comput value
            calculated_value = eval(current_expression[index_start:index_end+1])

            # add to next expression
            current_expression = current_expression[:index_start] + str(calculated_value) + current_expression[index_end+1:]

            i = current_expression.find(target_operand)
    return int(eval(current_expression))

# from itertools import permutations
# import sys

# def solution(expression):
#     answer = 0
#     highest_value = -sys.maxsize
#     operands = ["+", "*", "-"]
#     # get combination of operands
#     perms = permutations(operands, len(operands))

#     # for each combination, starting from left most operand perform calculation
#     for permutation in perms:
#         calculated_value = abs(calculate(expression, permutation))
#         # if the current calculated value is greater than highest value, replace
#         highest_value = max(highest_value, calculated_value)
#     # return calculated value
#     answer = highest_value
#     return answer

# def calculate(expression, permutation):
#     value = 0
#     current_expression = expression

#     for target_operand in permutation:
#         i = current_expression.find(target_operand)
#         while i > 0:
#             # find signs and numbers around operand
#             index_start = get_expression_start(i, current_expression)
#             index_end = get_expression_end(i, current_expression)

#             # use python's eval to comput value
#             calculated_value = eval(current_expression[index_start:index_end+1])

#             # add to next expression
#             current_expression = current_expression[:index_start] + str(calculated_value) + current_expression[index_end+1:]

#             i = current_expression.find(target_operand)
#     return int(eval(current_expression))

# def get_expression_start(i, current_expression):

#     i -= 1

#     while i > 0:
#         if not current_expression[i].isdigit():
#             break

#         i -= 1

#     if i == 0:
#         return i

#     if not current_expression[i-1].isdigit():
#         return i

#     return i+1

# def get_expression_end(i, current_expression):

#     i += 1
#     if current_expression[i] == "-":
#         i += 1

#     while i < len(current_expression):
#         if not current_expression[i].isdigit():
#             break
#         i += 1

#     return i - 1

if __name__ == "__main__":
    print(solution("10")) #10
    print(solution("5+5")) #10
    print(solution("50*6-3*2")) #300
    print(solution("100-200*300-500+20")) #60420