# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: return the length of it's longest binary gap

def solution(N):
    # write your code in Python 3.6

    # convert number to string of binary
    binary = '{0:08b}'.format(N)
    maximum = 0
    count = 0
    first_1_exists = False

    # count gap
    for bit in binary:
        # if 1 exists, check maximum and reset count
        if (bit == '1'):
            maximum = max(maximum, count)
            first_1_exists = True
            count = 0

        # count the number of zeros
        if (bit == '0' and first_1_exists):
            count += 1

    # return zeros
    return maximum
