def solution(A):
    total = 0

    cars_to_west = sum(A)

    for index, car in enumerate(A):
        if car == 0:
            total += cars_to_west
        else:
            cars_to_west -= 1

        if total > 1000000000:
            return -1

    return total