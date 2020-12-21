# goal: 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

import math

def solution(s):
    answer = ''
    n = len(s)
    if n % 2 == 1:
        middle_index = math.floor(n/2)
        answer = s[middle_index]
    else:
        middle_index = n // 2
        answer = s[middle_index-1:middle_index+1]

    return answer

if __name__ == "__main__":
    print(solution("abcde"))
    print(solution("qwer"))