# goal: 문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
#   문자열 s의 길이 : 2,500 이하의 자연수
#   문자열 s는 알파벳 소문자로만 구성

# while it's not the end of array,
# for each letter, check if it's palindrome
# while it's palindrome, expand expand length of it's palindrome
# repeat until it's not palindrome anymore
# update biggest length of palindrome
# continue until the end of array
# return length

def solution(s):
    answer = 0
    max_palindrome_length = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    # while it's not the end of array,
    for index, letter in enumerate(s):
        palindrome_start = index
        palindrome_end =index
        # for each letter, check if it's palindrome
        # while it's palindrome, expand expand length of it's palindrome
        while is_palindrome(palindrome_start, palindrome_end, s)
            # repeat until it's not palindrome anymore
            max_palindrome_length = max(max_palindrome_length, (palindrome_end - palindrome_start) + 1)
            # update biggest length of palindrome
            palindrome_start -= 1
            palindrome_end += 1

    # continue until the end of array
    # return length

    return max_palindrome_length

def is_palindrome(palindrome_start, palindrome_end, s):

    if palindrome_end == palindrome_start:
        return True
    try:
        while palindrome_end != palindrome_start:


            palindrome_end -= 1
            palindrome_start += 1
    except IndexError:
        return False