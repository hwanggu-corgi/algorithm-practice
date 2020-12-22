def solution(arr):
    answer = []
    current_number = -1
    # if number if different, then append number to array, and memoize the changed number in variable
    for number in arr:
        if number != current_number:
            answer.append(number)
            current_number = number

    return answer

if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
    print(solution([[4,4,4,3,3])) # [4,3]