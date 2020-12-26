# goal:두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의
# 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

# 제한사항
#   각 단어는 알파벳 소문자로만 이루어져 있습니다.
#   각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
#   words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
#   begin과 target은 같지 않습니다.
#   변환할 수 없는 경우에는 0를 return 합니다.

# Example
#   1) begin: hit	target: cog	   words: [hot, dot, dog, lot, log, cog]
#       hit -> hot -> dot -> dog -> cog

#   2) begin: hit	target: cog	   words: [hot, dot, dog, lot, log]

# Pesudocode
#   - if maximum depth reached, return
#   - if target word reached, compare depth with the current best, and replace if less
#   - for each word in words,
#   - check if word is one apart from 'in_process'
#   - recursively use the function on the word

def solution(begin, target, words):
    answer = 0
    return answer