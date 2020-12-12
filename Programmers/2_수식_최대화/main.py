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
#

def solution(expression):
    answer = 0
    return answer