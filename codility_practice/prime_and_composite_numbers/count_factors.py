# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 4 - > 1 2 4
# 5 ->  1 5
# 6 ->  1 2 3 6
# 7 ->  1 7
# 8 ->  1 2 4 8
# 9 ->  1 3 9
# 16 -> 1 2 4 8 16

# cases
import math

def solution(N):
    count = 0

    if N == 1:
        return 1

    i = 1
    while i * i <= N:
        if N % i == 0:
            count += 1
        i += 1

    sqrt = math.sqrt(N)
    if sqrt == int(sqrt):
        return count * 2 - 1
    else:
        return count * 2

if __name__ == "__main__":
    print(solution(24)) # 8
    print(solution(16)) # 5