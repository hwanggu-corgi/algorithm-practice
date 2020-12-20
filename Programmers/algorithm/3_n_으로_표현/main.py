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


# Pseudocode (bottom to top)
#   1. initialize dp = []
#   1. for number_counts starting from 1,
#   2. initialize dp_temp = []
#   4. for each number in dp, perform different combinations of computation of 5's and add to queue
#       2.1 dp_temp.append(dp[i] + 5)
#           if number is in memo, then continue
#           if dp[i] + 5 == number, then return number_counts
#           add dp[i] + 5 to memo
#           append to dp_temp
#       2.2 dp_temp.append((dp[i] - 5)
#           if number is in memo, then continue
#           if dp[i] - 5 == number, then return number_counts
#           add dp[i] - 5 to memo
#           append to dp_temp
#       2.3 dp_temp.append((dp[i] * 5)
#           if number is in memo, then continue
#           if dp[i] * 5 == number, then return number_counts
#           add dp[i] * 5 to memo
#           append to dp_temp
#       2.4 dp_temp.append((dp[i] // 5)
#           if number is in memo, then continue
#           if dp[i] // 5 == number, then return number_counts
#           add dp[i] // 5 to memo
#           append to dp_temp

#   5. for a staring with number of 5's,
#   6. calculate number of b (i.e. b = number of 5's - a)
#   7. if b > a, then break
#   8. if b == 0, then dp_temp.append(a many 5's)
#   9. if b != 0, then
#       9.1 dp_temp.append(a many 5's + b many 5's)
#            if number is in memo, then skip
#            add to memoization
#       9.2 dp_temp.append(a many 5's - b many 5's)
#            if number is in memo, then skip
#            add to memoization
#       9.3 dp_temp.append(a many 5's * b many 5's)
#            if number is in memo, then skip
#            add to memoization
#       9.4 dp_temp.append(a many 5's // b many 5's)
#            if number is in memo, then skip
#            add to memoization
#   10. set dp = dp_temp

# Detailed Example

# Cases
#  1. when N == number
#      - return 1
#  2. when N != number
#      - dynamic programming!!


def solution(N, number):
    answer = 0
    dp = {}

    if N == number:
        return 1

    for i in range(1,9):
        dp[i] = set()

    for i in range(1,9):
        dp[i].add(int(str(N) * i))
        i += 1

    for number_counts in range(1,9):
        j = number_counts
        while j >= 1:
            k = number_counts - j
            if k not in dp:
                j -= 1
                continue
            for a in dp[j]:
                for b in dp[k]:
                    for operand in ["+", "-", "*", "/"]:
                        new_value = 0
                        if operand == "+":
                            new_value = a + b
                        elif operand == "-":
                            new_value = a - b
                        elif operand == "*":
                            new_value = a * b
                        else:
                            if b == 0:
                                continue

                            new_value = a // b

                        if new_value in dp[number_counts]:
                            continue

                        if new_value == number:
                            return number_counts

                        dp[number_counts].add(new_value)

            j -= 1

    return -1



# def solution(N, number):
#     answer = 0

#     #   1. initialize dp = []
#     dp = []
#     memo = set()
#     number_counts = 1
#     #   1. for number_counts starting from 1,
#     while number_counts < 9:
#         dp_temp = []
#         #   3. for each number in dp, perform different combinations of computation of 5's and add to queue
#         for dp_value in dp:
#             #       3.1 dp_temp.append(dp[i] + 5)
#             #           if number is in memo, then continue
#             #           if dp[i] + 5 == number, then return number_counts
#             #           add dp[i] + 5 to memo
#             #           append to dp_temp
#             #       3.2 dp_temp.append((dp[i] - 5)
#             #           if number is in memo, then continue
#             #           if dp[i] - 5 == number, then return number_counts
#             #           add dp[i] - 5 to memo
#             #           append to dp_temp
#             #       3.3 dp_temp.append((dp[i] * 5)
#             #           if number is in memo, then continue
#             #           if dp[i] * 5 == number, then return number_counts
#             #           add dp[i] * 5 to memo
#             #           append to dp_temp
#             #       3.4 dp_temp.append((dp[i] // 5)
#             #           if number is in memo, then continue
#             #           if dp[i] // 5 == number, then return number_counts
#             #           add dp[i] // 5 to memo
#             #           append to dp_temp
#             for operand in ["+", "-", "*", "/"]:
#                 new_value = 0
#                 if operand == "+":
#                     new_value = dp_value + N
#                 elif operand == "-":
#                     new_value = dp_value - N
#                 elif operand == "*":
#                     new_value = dp_value * N
#                 else:
#                     new_value = dp_value // N

#                 if new_value in memo:
#                     continue

#                 if new_value == number:
#                     return number_counts

#                 memo.add(new_value)
#                 dp_temp.append(new_value)

#         #   4. for a staring with number of 5's,
#         a = number_counts
#         while a >= 1:
#             #   5. calculate number of b (i.e. b = number_counts - a)
#             b = number_counts - a

#             a_number_of_N = int(str(N) * a)
#             b_number_of_N = int(str(N) * b) if b > 0 else 0
#             #   6. if b > a, then break
#             if b > a:
#                 break
#             #   7. if b == 0, then dp_temp.append(a many 5's)
#             elif b == 0:
#                 new_value = a_number_of_N
#                 if new_value in memo:
#                     continue

#                 if new_value == number:
#                     return number_counts

#                 memo.add(new_value)
#                 dp_temp.append(new_value)
#             #   8. if b != 0, then
#             else:
#                 #       8.1 dp_temp.append(a many 5's + b many 5's)
#                 #            if number is in memo, then skip
#                 #            if a many 5's + b many 5's == number, then return number_counts
#                 #            add to memoization
#                 #            append to dp_temp
#                 #       8.2 dp_temp.append(a many 5's - b many 5's)
#                 #            if number is in memo, then skip
#                 #            if a many 5's - b many 5's == number, then return number_counts
#                 #            add to memoization
#                 #            append to dp_temp
#                 #       8.3 dp_temp.append(a many 5's * b many 5's)
#                 #            if number is in memo, then skip
#                 #            if a many 5's * b many 5's == number, then return number_counts
#                 #            add to memoization
#                 #            append to dp_temp
#                 #       8.4 dp_temp.append(a many 5's // b many 5's)
#                 #            if number is in memo, then skip
#                 #            if a many 5's / b many 5's == number, then return number_counts
#                 #            add to memoization
#                 #            append to dp_temp
#                 for operand in ["+", "-", "*", "/"]:
#                     new_value = 0
#                     if operand == "+":
#                         new_value = a_number_of_N + b_number_of_N
#                     elif operand == "-":
#                         new_value = a_number_of_N - b_number_of_N
#                     elif operand == "*":
#                         new_value = a_number_of_N * b_number_of_N
#                     else:
#                         new_value = a_number_of_N // b_number_of_N

#                     if new_value in memo:
#                         continue

#                     if new_value == number:
#                         return number_counts

#                     memo.add(new_value)
#                     dp_temp.append(new_value)
#             a -= 1
#         #   9. set dp = dp_temp
#         dp = dp_temp
#         #   10. increment number_counts
#         number_counts += 1

#     return -1

if __name__ == "__main__":
    print(solution(5, 12)) # 4
    print(solution(2, 11)) # 3
    print(solution(5, 5)) # 1
    print(solution(1, 111)) # 1