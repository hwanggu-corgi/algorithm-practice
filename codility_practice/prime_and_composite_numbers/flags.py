# goal: The goal is to set the maximum number of flags on the peaks, according to certain rules.

# Example
#   1)
#       A[0] = 1                1
#       A[1] = 5    <- peak 1   1
#       A[2] = 3                3
#       A[3] = 4    <- peak 2   3
#       A[4] = 3                5
#       A[5] = 4    <- peak 3   5
#       A[6] = 1                10
#       A[7] = 2                10
#       A[8] = 3                10
#       A[9] = 4                10
#       A[10] = 6   <- peak 4   10
#       A[11] = 2               -1

# pesudocode
#   find peaks
#   find K that works on most peaks
#   find number of flags

def solution(A):
    peaks_total, A = get_peaks(A)
    flags_amount = get_flags_amount(peaks_total, A)

    return flags_amount

def get_peaks(A):
    peaks_count = 0
    n = len(A)
    res = [-1] * n

    if n == 1:
        res[0] = 0
        peaks_count += 1
        return peaks_count, res

    i = n - 2
    while i >= 0:
        if (A[i-1] < A[i]) and (A[i] > A[i+1]):
            res[i] = i
            peaks_count += 1
        else:
            res[i] = next_peak_location
        i -= 1

    return peaks_count, res

def get_flags_amount(peaks_total, A):
    flags = peaks_total

    while flags >= 1:

        if is_possible(flags, A):
            break
        flags -= 1

    return flags


def is_possible(flags, A):
    n = len(A)
    distance_amt = flags
    i = 0
    while i < n and flags > 0:
        if not A[i] == True:
            i += 1
        else:
            flags -= 1
            i += distance_amt

    return True if flags == 0 else False