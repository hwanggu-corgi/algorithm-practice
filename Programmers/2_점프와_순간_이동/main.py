# goal:아이언 슈트 구매자가 이동하려는 거리 N이 주어졌을 때, 사용해야 하는 건전지 사용량의 최솟값을
# return하는 solution 함수를 만들어 주세요

# - (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동을 할 수 있다
# - 순간이동을 하면 건전지 사용량이 줄지 않다
# - 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 듭니다

# 제한 사항
#   - 숫자 N: 1 이상 10억 이하의 자연수
#   - 숫자 K: 1 이상의 자연수

# example
#   n: 5
#   current position          final Position
                    #      0  1  2  3  4  5
                    # 0    0  1  2  3  4  5
                    # 1    -  0  0  1  0  1
                    # 2    -  -  0  1  0  1
                    # 3    -  -  -  0  1  2
                    # 4    -  -  -  -  0  1
                    # 5    -  -  -  -  -  0

# 0 1 2 3 4 5
# 0 1 1 2 1 2

# 0 1 2 3 4 5 6
# 0 1 1 2 1 2 2

# 0 1 2 3 4 5 6 7 it's a dynamic programming!!!
# 0 1 1 2 1 2 2 3

# Detailed Example
# n =7
# dp = [0,0,0,0,0,0,0,0]
# dp = [0,0,0,0,0,0,0,0] 1 is odd --> dp[1] = dp[1 // 2] + 1 = 1
# dp = [0,1,0,0,0,0,0,0] 2 is even --> dp[2] = dp[2 // 2] = 1       2 % 2 = 0 + 1 = 1
# dp = [0,1,1,0,0,0,0,0] 3 is odd --> dp[3] = dp[3 // 2] + 1 = 2    3 % 2 = 1 + 1 = 2
# dp = [0,1,1,2,0,0,0,0] 4 is even --> dp[4] = dp[4 // 2] = 1       4 % 2 = 0 + 1 = 1
# dp = [0,1,1,2,1,0,0,0] 5 is odd --> dp[5] = dp[5 // 2] + 1 = 2    5 % 2 = 1 + 1 = 2
# dp = [0,1,1,2,0,0,0,0] 6 is even --> dp[6] = dp[6 // 2] = 2       6 % 2 = 0 + 2 = 2
# dp = [0,1,1,2,0,0,0,0] 7 is odd --> dp[7] = dp[7 // 2] + 1 = 3    7 % 2 = 1 + 2 = 3
# dp = [0,1,1,2,0,0,0,0] 8 is even --> dp[8] = dp[8 // 2] = 1       8 % 2 = 0 + 1 = 1

# pseudocode
#   create array of size n+1 (call it dp)
#   for i from 1 until n+1,
#   if i is odd, set dp[i] = dp[i//2] + 1
#   if i is even, set dp[i] = dp[i//2]
#   return last number dp[-1]

# cases
#   1. when n = 1
#   2. when n != 1

def solution(n):
    ans = 0

    #   create array of size n+1 (call it dp)
    dp = [0] * (n+1)
    #   for i from 1 until n,
    i = 1
    while i < n+1:
        #   if i is odd, set dp[i] = dp[i//2] + 1
        dp[i] = dp[i//2] if i %2 == 0 else dp[i//2] + 1
        #   if i is even, set dp[i] = dp[i//2]
        i += 1

    ans = dp[-1]
    return ans

if __name__ == "__main__":
    print(solution(5)) #2
    print(solution(6)) #2
    print(solution(5000)) #5
    print(solution(1000000)) #5