def solution(A):
    # write your code in Python 3.6
    total = 0
    cars_to_west = sum(A)

    if cars_to_west == 0:
        return 0

    for index, car in enumerate(A):
        if car == 0:
            total += sum(A[index:])
            cars_to_west -= 1

    return total