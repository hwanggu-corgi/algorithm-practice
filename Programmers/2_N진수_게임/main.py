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
#     1) 0 - 0
#     2) 2 - 2
#     3) 4 - 4
#     4) 6 - 6
#     5) 8 - 8
#     6) 10 - A
#     7) 12 - C
#     8) 14 - E
#     9) 16 - 10
#     10)18 - 12
#     11)20 - 14
#     12)22 - 16
#     13)24 - 18
#     14)26 - 1A
#     16)28 - 1C

#     02468ACE1111111

#   n: 16 t: 16 (length of value to print) m: 2 (represents skip distance) p: 2
#     1) 1 - 1
#     2) 3 - 3
#     3) 5 - 5
#     4) 7 - 7
#     5) 9 - 9
#     6) 11 - B
#     7) 13 - D
#     8) 15 - F
#     9) 17 - 11
#     10)19 - 13
#     11)21 - 15
#     12)23 - 17
#     13)25 - 19
#     14)27 - 1B
#     16)29 - 1D

#     13579BDF13579BD

def solution(n, t, m, p):
    answer = ''

    return answer