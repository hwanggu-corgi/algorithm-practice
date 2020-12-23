# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# pseudocode
#   start i from 1
#   find other value x satisfying i * x = N
#   evaluate perimeter
#   store val in min_perimeter = min(min_perimeter, perimeter)
import sys
def solution(N):
    # write your code in Python 3.6
    min_perimeter = sys.maxsize
    a = 1
    while a * a <= N:
        if N % a == 0:
            b = N // a
            perimeter = (a + b) * 2
            min_perimeter = min(perimeter, min_perimeter)
        a += 1

    return min_perimeter

if __name__ == "__main__":
    print(solution(30)) # 22
    print(solution(1)) # 4
