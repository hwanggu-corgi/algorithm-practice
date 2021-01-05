# goal: 문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
#   문자열 s의 길이 : 2,500 이하의 자연수
#   문자열 s는 알파벳 소문자로만 구성

# Pseudocode
# for each letter in string, check if is palindrome
# if palindrome expand length by 1
# if not

def solution(s):

    if len(s) == 0:
        return 0

    max_palindrome_length_even = get_max_palindromic_length_even(s)

    max_palindrome_length_odd = get_max_palindromic_length_odd(s)

    answer = max(max_palindrome_length_even, max_palindrome_length_odd)

    return answer

def get_max_palindromic_length_even(s):
    max_length = 0

    for i in range(1, len(s)):
        palindrome_end = i
        palindrome_start = i - 1

        # if is palindrome increase length by 1 on either side
        while is_palindrome(palindrome_start, palindrome_end, s):
            max_length = max(max_length, (palindrome_end - palindrome_start) + 1)
            palindrome_start -= 1
            palindrome_end += 1

    return max_length

def get_max_palindromic_length_odd(s):
    max_length = 0

    for i in range(1, len(s)):
        palindrome_end = i
        palindrome_start = i

        # if is palindrome increase length by 1 on either side
        while is_palindrome(palindrome_start, palindrome_end, s):
            max_length = max(max_length, (palindrome_end - palindrome_start) + 1)
            palindrome_start -= 1
            palindrome_end += 1

    return max_length


def is_palindrome(palindrome_start, palindrome_end, s):

    if palindrome_start < 0:
        return False

    if palindrome_end == palindrome_start:
        return True
    try:
        while palindrome_start != palindrome_end:
            if s[palindrome_start] != s[palindrome_end]:
                return False

            palindrome_end -= 1
            palindrome_start += 1

    except IndexError:
        return False

    return True

# Pseudocode
# start with palindrome_start = 0 and palindrome_end = n-1
# check if s[palindrome_start:palindrome_end+1] is palindrome
# if so, return length
# if not, traverse in one of two directions (recursively)
#   palindrome_start + 1
#   palindrome_end - 1


# def solution(s):
#     answer = 0
#     memo = {}
#     palindrome_start = 0
#     palindrome_end = len(s)-1

#     if len(s) == 0:
#         return 0

#     max_palindrome_length = _solution(palindrome_start, palindrome_end, s, memo)

#     return max_palindrome_length

# def _solution(palindrome_start, palindrome_end, s, memo)  :
#     if is_palindrome(palindrome_start, palindrome_end, s):
#         memo[(palindrome_start, palindrome_end)] = (palindrome_end-palindrome_start)+1
#         return (palindrome_end-palindrome_start)+1

#     if (palindrome_start, palindrome_end) in memo:
#         return memo[(palindrome_start, palindrome_end)]

#     length_1 = _solution(palindrome_start+1, palindrome_end, s, memo)
#     length_2 = _solution(palindrome_start, palindrome_end-1, s, memo)

#     max_length = max(length_1, length_2)
#     return max_length

# def is_palindrome(palindrome_start, palindrome_end, s):

#     if palindrome_start < 0 or palindrome_end > (len(s)-1):
#         return False

#     if palindrome_end == palindrome_start:
#         return True
#     try:
#         while palindrome_start != palindrome_end:
#             if s[palindrome_start] != s[palindrome_end]:
#                 return False

#             palindrome_end -= 1
#             palindrome_start += 1

#     except IndexError:
#         return False

#     return True

# def solution(s):
#     answer = 0
#     palindrome_start = 0
#     palindrome_end = len(s)-1

#     if len(s) == 0:
#         return 0

#     max_palindrome_length = _solution(palindrome_start, palindrome_end, s)

#     return max_palindrome_length

# def _solution(palindrome_start, palindrome_end, s)  :
#     if is_palindrome(palindrome_start, palindrome_end, s):
#         return (palindrome_end-palindrome_start)+1

#     length_1 = _solution(palindrome_start+1, palindrome_end, s)
#     length_2 = _solution(palindrome_start, palindrome_end-1, s)

#     max_length = max(length_1, length_2)
#     return max_length

# def is_palindrome(palindrome_start, palindrome_end, s):

#     if palindrome_start < 0 or palindrome_end > (len(s)-1):
#         return False

#     if palindrome_end == palindrome_start:
#         return True
#     try:
#         while palindrome_start != palindrome_end:
#             if s[palindrome_start] != s[palindrome_end]:
#                 return False

#             palindrome_end -= 1
#             palindrome_start += 1

#     except IndexError:
#         return False

#     return True

# while it's not the end of array,
# for each letter, check if it's palindrome
# while it's palindrome, expand expand length of it's palindrome
# repeat until it's not palindrome anymore
# update biggest length of palindrome
# continue until the end of array
# return length

# def solution(s):
#     answer = 0
#     max_palindrome_length = 0
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

#     # check palindrome odd
#     # while it's not the end of array,
#     for index, letter in enumerate(s):
#         palindrome_start = index
#         palindrome_end =index
#         # for each letter, check if it's palindrome
#         # while it's palindrome, expand expand length of it's palindrome
#         while is_palindrome(palindrome_start, palindrome_end, s):
#             # repeat until it's not palindrome anymore
#             # update biggest length of palindrome
#             max_palindrome_length = max(max_palindrome_length, (palindrome_end - palindrome_start) + 1)

#             palindrome_start -= 1
#             palindrome_end += 1

#     # continue until the end of array
#     # return length
#     return max_palindrome_length

# def get_max_palindrome_length_odd(s):
#     max_palindrome_length = 0

#     # while it's not the end of array,
#     for index, letter in enumerate(s):
#         palindrome_start = index
#         palindrome_end =index
#         # for each letter, check if it's palindrome
#         # while it's palindrome, expand expand length of it's palindrome
#         while is_palindrome(palindrome_start, palindrome_end, s):
#             # repeat until it's not palindrome anymore
#             # update biggest length of palindrome
#             max_palindrome_length = max(max_palindrome_length, (palindrome_end - palindrome_start) + 1)

#             palindrome_start -= 1
#             palindrome_end += 1

#     return max_palindrome_length

# def is_palindrome(palindrome_start, palindrome_end, s):

#     if palindrome_end == palindrome_start:
#         return True
#     try:
#         while palindrome_start != palindrome_end:
#             if s[palindrome_start] != s[palindrome_end]:
#                 return False

#             palindrome_end -= 1
#             palindrome_start += 1

#     except IndexError:
#         return False

#     return True

if __name__ == "__main__":
    print(solution("")) #0
    print(solution("abcdcba")) #7
    print(solution("abacde")) #3