# goal: 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는
# 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - numbers는 길이 1 이상 7 이하인 문자열입니다.
#   - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
#   - 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

def solution(numbers):
    answer = 0
    N = len(numbers)
    combinations = set()

    # split numbers to array of digits

    # use DFS to find all combination of words
    i = 0
    while i < N:
        _solution(..., N, combinations)
        i += 1

    # calculate length of combination of words
    return len(combinations)

def _solution(...):

    # if combined word length matches target, add to set and return
    if len(combined_word) == N:
        combinations.add(combined_word)
        return

    # if not, continue to add combinations
    # for each character in word
    while ...:
        # pop it
        # add to combination
        # get reminaing words after pop
        _solution(...)
