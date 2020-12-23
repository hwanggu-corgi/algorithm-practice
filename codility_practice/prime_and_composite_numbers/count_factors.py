# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# cases

def solution(N):
    count = 0

    i = 1
    while i * i <= N:
        if N % i == 0:
            count += 1
        i += 1

    return count * 2

if __name__ == "__main__":
    print(solution(24)) # 8