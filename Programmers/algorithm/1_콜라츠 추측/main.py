# goal: 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요. 단, 작업을
# 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

def solution(num):
    answer = 0
    count = 0

    while count <= 500:
        if num == 1:
            return count

        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1

        count += 1

    return -1

if __name__ == "__main__":
    print(solution(6)) #8
    print(solution(16)) #4
    print(solution(626331)) #-1