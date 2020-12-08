# goal: 숫자 게임이 익숙하지 않은 튜브는 게임에 져서 벌칙을 받는 굴욕을 피하기 위해, 자신이 말해야 하는
# 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다. 튜브의 프로그램을 구현하라.

# Example
#   n: 2 t: 4 (length of value to print) m: 2 (represents skip distance) p: 1
#     1) 0 - 0
#     2) 2 - 10
#     3) 4 - 100
#     4) 6 - 110

#     0111

#   n: 16 t: 16 (length of value to print) m: 2 (represents skip distance) p: 1
#     0) 0 - 0  < -
#     1) 1 - 1
#     2) 2 - 2  < -
#     3) 3 - 3
#     4) 4 - 4  < -
#     5) 5 - 5
#     6) 6 - 6  < -
#     7) 7 - 7
#     8) 8 - 8  < -
#     9) 9 - 9
#     10)10 - A < -
#     11)11 - B
#     12)12 - C < -
#     13)13 - D
#     14)14 - E < -
#     16)15 - F
#     16)16 - 10 < -
#             ^
#     16)17 - 11 < -
#              ^
#     16)18 - 12 < -
#              ^
#     16)19 - 13 < -
#              ^
#     16)20 - 14 < -
#              ^
#     16)21 - 15 < -
#              ^
#     16)22 - 16 < -
#              ^

#     02468ACE1111111

#   n: 16 t: 16 (length of value to print) m: 2 (represents skip distance) p: 2
#     0) 0 - 0
#     1) 1 - 1  < -
#     2) 2 - 2
#     3) 3 - 3  < -
#     4) 4 - 4
#     5) 5 - 5  < -
#     6) 6 - 6
#     7) 7 - 7  < -
#     8) 8 - 8
#     9) 9 - 9  < -
#     10)10 - A
#     11)11 - B < -
#     12)12 - C
#     13)13 - D < -
#     14)14 - E
#     16)15 - F < -
#     16)16 - 10 < -
#              ^
#     16)17 - 11 < -
#              ^
#     16)18 - 12 < -
#              ^
#     16)19 - 13 < -
#              ^
#     16)20 - 14 < -
#              ^
#     16)21 - 15 < -
#              ^
#     16)22 - 16 < -
#              ^

#     13579BDF13579BD

# Example Detail
#   n: 2 t: 4 (length of value to print) m: 2 (represents skip distance) p: 1
#       - [] -> go to (p-1) --> out of bound --> fill values (first 5 values (0,1,2,3,4,5))
#       - [0, 1, 1, 0, 1, 1, ...] -> go to p-1 (0) --> value exists --> add to answer ("0")
#          ^
#       - [0, 1, 1, 0, 1, 1, ...] -> increase by m (2)
#          ^

#       - [0, 1, 1, 0, 1, 1, ...] -> is length t (4)? --> no --> continue
#          ^

#       - [0, 1, 1, 0, 1, 1, ...] -> value exists --> add to answer ("01")
#                ^

#       - [0, 1, 1, 0, 1, 1, ...] -> increase by m (2)
#                ^

#       - [0, 1, 1, 0, 1, 1, ...] -> is length t (4)? --> no --> continue
#                      ^

#       - [0, 1, 1, 0, 1, 1, ...] -> value exists --> add to answer ("011")
#                      ^

#       - [0, 1, 1, 0, 1, 1, ...] -> increase by m (2)
#                      ^

#       - [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1] -> is length t (4)? --> no --> continue
#                      ^



#       - [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1] -> value exists --> add to answer ("0111")
#                            ^

#       - [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1] -> increase by m (2)
#                            ^

#       - [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1] -> is length t (4)? --> no --> exit
#                                  ^


# Pseudocode
# start with i = (p-1)
# while the length of answer is less than t,
#   go to arr[i]
#   if not indexerror, add value to answer
#   if indexerror, fill arr by 5 values in n-ary form
#   increment i by m
# return answer

def solution(n, t, m, p):
    answer = ""
    arr = []
    number_ending = 0

    # start with i = (p-1)
    i = p-1
    # while the length of answer is less than t,
    while len(answer) < t:
        try:
            #   go to arr[i]
            #   if not indexerror, add value to answer
            answer += arr[i]
            #   increment i by m
            i += m
        except IndexError:
            #   if indexerror, fill arr by 5 values in n-ary form
            number_ending = fill_values(arr, number_ending, n)
    # return answer

    return answer

def fill_values(arr, number_ending, n):

    i = 0
    while i < 5:
        nary_number = get_nary(number_ending, n)
        i += 1

    number_ending += i

    return number_ending