# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: Write a function that, given an array A consisting of N integers, returns index
# of any element of array A in which the dominator of A occurs
#   - Dominator is the value that occurs in more than half of the elements of A
#   - Return index of any element of array A in which the dominator of A occurs
#   - Return -1 if array A does not have a dominator

def solution(A):
    # write your code in Python 3.6

    N = len(A)
    count = {}

    if len(A) == 0:
        return -1

    if len(A) == 1:
        return 0

    # for each element in array add count to dictionary with it as key
    i = 0
    while i < N:
        integer = A[i]
        # if element doesn't exist in dictionary, then initialize to 0
        if integer not in count:
            count[integer] = 0
        else:
            # if element does exist, then incrememt count by 1
            count[integer] += 1

        is_dominator = True if count[integer] > N/2 else False
        # if element is dominator (count is greater than N/2), return index
        if is_dominator:
            return i

        i += 1

    # return -1 if doesn't exist
    return -1
