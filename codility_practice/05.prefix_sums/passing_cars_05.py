# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: count passing cars.

def solution(A):
    # write your code in Python 3.6
    count = 0
    cars_to_west = sum(A)
    N = len(A)

    if cars_to_west == 0:
        return 0

    if cars_to_west == N:
        return 0

    for car in A:
        # if i is car traveling west, deduct cars_to_west by 1
        if car == 1:
            cars_to_west -= 1
        # if i is car traveling east, then add by number of cars traveling to west from i (cars_to_west)
        else:
            count += cars_to_west

    # return −1 if the number of pairs of passing cars exceeds 1,000,000,000
    if count > 1000000000:
        return -1

    # return count
    return count
