# goal: 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라
# 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - s의 길이는 1 이상 1,000 이하입니다.
#   - s는 알파벳 소문자로만 이루어져 있습니다.

import sys
def solution(s):
    N = len(s)
    minimum_length = sys.maxsize

    # while i < N where i represents length of compression string
    substring_length = 1
    while substring_length < N:
        # find the length of string after compression
        length_after_compression = compress_string(s,substring_length,N)
        if length_after_compression == -1:
            substring_length += 1
            continue
        # if length of string is less current, update minimum value
        minimum_length = min(minimum_length, length_after_compression)
        substring_length += 1

    # return minimum value
    answer = minimum_length
    return answer

def compress_string(s,substring_length,N):
    current_length = 1
    substrings_list = []
    substring = ''
    i = 0

    while i < N:

        if (current_length % substring_length == 0):
            substrings_list.append(substring)
            substring = ''

        substring += s[i]
        current_length += 1
        i += 1

    return length

if __name__ == "__main__":
    print(solution("aabbaccc"))