#goal: 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,
# 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return
# 하는 solution 함수를 완성해 주세요

# - 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다

# 제한사항
# N : 21 이상 220 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)
# A, B : N 이하인 자연수 (단, A ≠ B 입니다.)

# Example
#   1 - 2 3 - 4 5 - 6 7 - 8
#     1  -  2     3  -  4
#        1           2

# Pseudocode
# find smaller of two values, call it smaller
# find larger of two values, call it larger
# while both floor and larger are not 1
# if larger/smaller is odd, do, math.ceil(a/2)
# if larger/smaller is even, do math.floor(a/2)
# add count
# return count
import math

def solution(n,a,b):
    count = 0
    # find smaller of two values, call it smaller
    smaller = min(a,b)
    # find larger of two values, call it larger
    larger = max(a,b)

    # while both floor and larger are not 1
    while smaller != 1 or larger != 1:
        # if larger/smaller is odd, do, math.ceil(a/2)
        smaller = math.floor(smaller/2) if smaller % 2 == 0 else math.ceil(smaller/2)
        # if larger/smaller is even, do math.floor(a/2)
        larger = math.floor(larger/2) if larger % 2 == 0 else math.ceil(larger/2)

        # add count
        count += 1
    # return count
    answer = count
    return answer

if __name__ == "__main__":
    print(solution(8,4,7)) #3
    print(solution(8,2,3)) #2
    print(solution(8,1,8)) #3
    print(solution(8,3,6)) #3
    print(solution(8,1,2)) #1
    print(solution(2,1,2)) #1