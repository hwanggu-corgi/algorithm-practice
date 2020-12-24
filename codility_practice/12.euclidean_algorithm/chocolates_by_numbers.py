# goal: The goal is to count the number of chocolates that you will eat, following
# the above rules.

# - You begin with eating chocolate number 0.
# -  if you ate chocolate number X, then you will next eat the chocolate with number
# (X + M) modulo N (remainder of division).
# - You stop eating when you encounter an empty wrapper.

# Example
#   1) N = 10   M = 4
#       0, 4, 8, 2 ,6

# find gcd of the two
# divide N by gcd

def solution(N, M):
    # find gcd of the two
    bigger = max(N,M)
    smaller = min(N,M)

    gcd_NM = gcd(bigger, smaller)

    # divide N by gcd
    answer = N // gcd_NM

    return answer

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Pseudocode
# while chocolate to eat is not in set
# add chocolate to set
# shift chocolate by M

# def solution(N, M):
#     # write your code in Python 3.6

#     chocolates_eaten_set = set()
#     current_chocolate = 0
#     # while chocolate to eat is not in set
#     while not current_chocolate in chocolates_eaten_set:

#         # add chocolate to set
#         chocolates_eaten_set.add(current_chocolate)
#         # shift chocolate by M
#         current_chocolate = (current_chocolate + M) % N

#     return len(chocolates_eaten_set)


if __name__ == "__main__":
    print(solution(20, 4)) # 5
    print(solution(10, 3)) # 10
