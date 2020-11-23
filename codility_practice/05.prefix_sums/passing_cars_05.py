# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: count passing cars.

def solution(A):
    # write your code in Python 3.6
    count = 0
    cars_to_west = sum(A)

    for car in A:
        # if i is car traveling west, deduct cars_to_west by 1
        if car == 1:
            cars_to_west -= 1
        # if i is car traveling east, then add by number of cars traveling to west from i (cars_to_west)
        else:
            count += cars_to_west

    # return count

    return count
