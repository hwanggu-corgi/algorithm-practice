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

# Pseudocode
# while the length of answer is less than t,
#   print value of p distance in m
#   increment by m

def solution(n, t, m, p):
    answer = ''

    return answer