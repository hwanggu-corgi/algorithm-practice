# goal: 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N
# 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# Example
#  1) N: 5     Number: 12
#  12 = 5 + 5 + (5 / 5) + (5 / 5)
#      12 = 60 / 5 = (55 + 5) / 5 <- uses minimal number of 5s
#      12 = 1 + 11 = 1 + 5 + 5 = (5/5) + 5 + 5
#      12 = 2 + 10= 2 + 5 + 5 = 1 + 1 + 5 + 5 = (5/5) + (5/5) + 5 + 5
#      12 = 3 + 9 = 1 + 1 + 1 + 10 - 1 = 1 + 1 + 5 + 5 - 1 = (5/5) + (5/5) + 5 + 5 - (5/5)
#      12 = 4 + 8 = 2 + 2 + 8 = 2 + 2 + 5 + 3 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 5 = (5/5) + (5/5) + (5/5) + (5/5) + (5/5) + (5/5) + (5/5) + (5/5) + 5
#      12 = 5 + 7 = 5 + 1 + 1
#      12 = 6 + 6 = 5 + 1 + 5 + 1
#      12 = 5 + 5 + 1 + 1
#  12 = 55 / 5 + 5 / 5
#      12 = 11 + 1

#  12 = (55 + 5) / 5
#      12 = 60 / 5

# Dynamic Programming
# 0    1   2   3   4   5   6   7   8   9   10
# 0    0   4

# How many different patterns exist with 0 many 5's --> 0
# How many different patterns exist with 1 many 5's --> 0
# How many different patterns exist with 2 many 5's --> 4
# using only 5
    #  - 55                 {5: [5], 55: [55]}
    #  - 5 x 5 --> 25       {5: [25], 55: [55]}
    #  - 5 - 5 --> 0        {5: [25, 0], 55: [55]}
    #  - 5 + 5 --> 10       {5: [25, 0, 10], 55: [55]}
    #  - 5 / 5 --> 1        {5: [25, 0, 10, 1], 55: [55]}
# How many different patterns exist with 3 many 5's --> 16
# Using only 5
    #  - 555
    #  - 55 + 5 --> 60
    #  - 55 - 5 --> 50
    #  - 55 * 5 --> 275
    #  - 55 / 5 --> 11
    #  - (5 x 5) + 5 --> 30
    #  - (5 x 5) - 5 --> 25
    #  - (5 x 5) * 5 --> 125
    #  - (5 x 5) / 5 --> 5
    #  - (5 - 5) + 5 --> 5
    #  - (5 - 5) - 5 --> -5
    #  - (5 - 5) * 5 --> 0
    #  - (5 - 5) / 5 --> 0
    #  - (5 + 5) + 5 --> 15
    #  - (5 + 5) - 5 --> 5
    #  - (5 + 5) * 5 --> 50
    #  - (5 + 5) / 5 --> 2
    #  - (5 / 5) + 5 --> 6
    #  - (5 / 5) - 5 --> -4
    #  - (5 / 5) * 5 --> 5
    #  - (5 / 5) / 5 --> 0.2
    # How many different patterns exist with 4 many 5's --> 64
    #  - 5555
    #  - 555 + 5        --> 560
    #  - 555 - 5        --> 550
    #  - 555 * 5        --> 2275
    #  - 555 / 5        --> 111
    #  - 55 + 55        --> 110
    #  - 55 - 55        --> 50
    #  - 55 * 55        --> 3025
    #  - 55 / 55        --> 1
    #  - (55 + 5) + 5   --> 65
    #  - (55 + 5) - 5   --> 55
    #  - (55 + 5) * 5   --> 300
    #  - (55 + 5) / 5   --> 12 <--- return value 4
    #  - (55 - 5) + 5   --> 55
    #  - (55 - 5) - 5   --> 45
    #  - (55 - 5) * 5   --> 250
    #  - (55 - 5) / 5   --> 10
    #  - (55 * 5) + 5   --> 280
    #  - (55 * 5) - 5   --> 270
    #  - (55 * 5) * 5   --> 1375
    #  - (55 * 5) / 5   --> 55
    #  - (55 / 5) + 5   --> 16
    #  - (55 / 5) - 5   --> 6
    #  - (55 / 5) * 5   --> 55
    #  - (55 / 5) / 5   --> 2
    #  - ((5 * 5) + 5) + 5 --> 35
    #  - ((5 * 5) + 5) - 5 --> 25
    #  - ((5 * 5) + 5) * 5 --> 150
    #  - ((5 * 5) + 5) / 5 --> 6
    #  - ((5 * 5) - 5) + 5 --> 25
    #  - ((5 * 5) - 5) - 5 --> 15
    #  - ((5 * 5) - 5) * 5 --> 100
    #  - ((5 * 5) - 5) / 5 --> 4
    #  - ((5 * 5) * 5) + 5 --> 130
    #  - ((5 * 5) * 5) - 5 --> 120
    #  - ((5 * 5) * 5) / 5
    #  - ((5 * 5) * 5) * 5
    #  - ((5 * 5) / 5) + 5
    #  - ((5 * 5) / 5) - 5
    #  - ((5 * 5) / 5) * 5
    #  - ((5 * 5) / 5) / 5
    #  - ((5 - 5) + 5) + 5
    #  - ((5 - 5) + 5) - 5
    #  - ((5 - 5) + 5) * 5
    #  - ((5 - 5) + 5) / 5
    #  - ((5 - 5) - 5) + 5
    #  - ((5 - 5) - 5) - 5
    #  - ((5 - 5) - 5) * 5
    #  - ((5 - 5) - 5) / 5
    #  - ((5 - 5) * 5) + 5
    #  - ((5 - 5) * 5) - 5
    #  - ((5 - 5) * 5) * 5
    #  - ((5 - 5) * 5) / 5
    #  - ((5 - 5) / 5) + 5
    #  - ((5 - 5) / 5) - 5
    #  - ((5 - 5) / 5) * 5
    #  - ((5 - 5) / 5) / 5
    #  - ((5 + 5) + 5) + 5
    #  - ((5 + 5) + 5) - 5
    #  - ((5 + 5) + 5) * 5
    #  - ((5 + 5) + 5) / 5
    #  - ((5 + 5) - 5) + 5
    #  - ((5 + 5) - 5) - 5
    #  - ((5 + 5) - 5) * 5
    #  - ((5 + 5) - 5) / 5
    #  - ((5 + 5) * 5) + 5
    #  - ((5 + 5) * 5) - 5
    #  - ((5 + 5) * 5) * 5
    #  - ((5 + 5) * 5) / 5
    #  - ((5 + 5) / 5) + 5
    #  - ((5 + 5) / 5) - 5
    #  - ((5 + 5) / 5) * 5
    #  - ((5 + 5) / 5) / 5
    #  - ((5 / 5) + 5) + 5
    #  - ((5 / 5) + 5) - 5
    #  - ((5 / 5) + 5) * 5
    #  - ((5 / 5) + 5) / 5
    #  - ((5 / 5) * 5) + 5
    #  - ((5 / 5) * 5) - 5
    #  - ((5 / 5) * 5) * 5
    #  - ((5 / 5) * 5) / 5
    #  - ((5 / 5) / 5) + 5
    #  - ((5 / 5) / 5) - 5
    #  - ((5 / 5) / 5) * 5
    #  - ((5 / 5) / 5) / 5
    # How many different patterns exist with 5 many 5's --> 256
    #  - 55555
    #  - 5555 + 5
    #  - 5555 - 5
    #  - 5555 * 5
    #  - 5555 / 5
    #  - 555 + 55
    #  - 555 - 55
    #  - 555 * 55
    #  - 555 / 55

#  using 55 and 5

# Pseudocode (Top to bottom)
#   1. Start with 1 many 5
#   2. if value == number, then return number of 5's used
#   3. if number exists in memoization, then return
#   4. else add different combinations of computation of 5's
#       2.1 recursive_formula(existing + 5)
#           add to memoization
#       2.2 recursive_formula(existing - 5)
#           add to memoization
#       2.3 recursive_formula(existing * 5)
#           add to memoization
#       2.4 recursive_formula(existing // 5)
#           add to memoization
#   5. Repeat each above but using recursion until answer emerges
#   6. for a staring with number of 5's,
#   7. calculate number of b (i.e. b = number of 5's - a)
#   8. if b > a, then break
#   9. if b == 0, then return recursive function of a (e.g. recursive_function(a))
#   10. if b != 0, and a + b == number of 5s, then return recursive function of a and b (e.g. recursive_function(a))
#       10.1 recursive_formula(a many 5's + b many 5's)
#           add to memoization
#       10.2 recursive_formula(a many 5's - b many 5's)
#           add to memoization
#       10.3 recursive_formula(a many 5's * b many 5's)
#           add to memoization
#       10.4 recursive_formula(a many 5's // b many 5's)
#           add to memoization


# Pseudocode (Top to bottom)
#   1. for number_of_5s starting from 1,
#   2. initialize dp_temp = []
#   3. if value == number, then return number_of_5s
#   4. for each number in dp, perform different combinations of computation of 5's and add to queue
#       4.1 if number is in memo, then continue
#       2.1 dp_temp.append(dp[i] + 5)
#           add dp[i] + 5 to memo
#       2.2 dp_temp.append((dp[i] - 5)
#           add dp[i] - 5 to memo
#       2.3 dp_temp.append((dp[i] * 5)
#           add dp[i] * 5 to memo
#       2.4 dp_temp.append((dp[i] // 5)
#           add dp[i] // 5 to memo

#   6. for a staring with number of 5's,
#   7. calculate number of b (i.e. b = number of 5's - a)
#   8. if b > a, then break
#   9. if b == 0, then return recursive function of a (e.g. recursive_function(a))
#   10. if b != 0, and a + b == number of 5s, then return recursive function of a and b (e.g. recursive_function(a))
#       10.1 recursive_formula(a many 5's + b many 5's)
#           add to memoization
#       10.2 recursive_formula(a many 5's - b many 5's)
#           add to memoization
#       10.3 recursive_formula(a many 5's * b many 5's)
#           add to memoization
#       10.4 recursive_formula(a many 5's // b many 5's)
#           add to memoization

# Detailed Example

# Cases
#  1. when N == number
#      - return 1
#  2. when N != number
#      - dynamic programming!!


def solution(N, number):
    answer = 0



    return answer