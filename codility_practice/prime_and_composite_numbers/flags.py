# goal: The goal is to set the maximum number of flags on the peaks, according to certain rules.

# Example
#   1)
#       A[0] = 1
#       A[1] = 5    <- peak 1
#       A[2] = 3
#       A[3] = 4    <- peak 2
#       A[4] = 3
#       A[5] = 4    <- peak 3
#       A[6] = 1
#       A[7] = 2
#       A[8] = 3
#       A[9] = 4
#       A[10] = 6   <- peak 4
#       A[11] = 2

# pesudocode
#   find peaks
#   find K that works on most peaks
#   find number of flags

def solution(A):
    # write your code in Python 3.6
    # find peaks
    peaks = get_peaks(A)
    # find K that works on most peaks
    # find number of flags
    flags_amount = get_flags_amount(A)

    return flags_amount

def get_peaks(A):
    # cases
    #   - when peak exists in edges A[0] or A[-1]
    #       - A[0] > A[1]
    #       - A[-1] > A[-2]
    #   - When peak exsists between A[0] and A[-1]
    #       - A[i-1] < A[i] > A[i+1]

    # return list of indicies
    pass


def get_flags_amount(A):
    pass
