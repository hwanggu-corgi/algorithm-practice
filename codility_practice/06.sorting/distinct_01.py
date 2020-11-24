# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: return the number of distinct values in array A

def solution(A):
    # write your code in Python 3.6

    # sort elements in array
    number_of_distinct_elements = 1
    current_element = A[0]
    N = len(A)

    # traverse through elements in array
    i = 0
    while i < N:
        # if element its on and A[i] are the same, continue
        # if element its on and A[i] are different, increment number_of_distinct_elements and update current_element
        if current_element == A[i]:
            number_of_distinct_elements += 1
            current_element = A[i]
        i += 1

    return number_of_distinct_elements
