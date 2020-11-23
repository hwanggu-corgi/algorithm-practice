# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: find missing element in array in the range [1 .. (N+1)] with exactly one element missing

def solution(A):
    # write your code in Python 3.6
    MAXIMUM = 100000
    # order the element
    A.sort()
    N = len(A)

    if N == 0:
        return 1

    # traverse the elements in the array and find the one not in it
    i = 1
    for number in A:
        if number != i:
            return i
        i += 1
