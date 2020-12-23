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
    peaks_total, peaks = get_peaks(A)
    flags_amount = get_flags_amount(peaks_total, peaks)

    return flags_amount

def get_peaks(A):
    peaks_count = 0
    next_peak_location = -1
    n = len(A)
    res = [-1] * n

    if n == 1:
        return peaks_count, res

    i = n - 2
    while i > 0:
        if (A[i-1] < A[i]) and (A[i] > A[i+1]):
            res[i] = i
            next_peak_location = i
            peaks_count += 1
        else:
            res[i] = next_peak_location
        i -= 1

    return peaks_count, res

def get_flags_amount(peaks_total, peaks):
    flags = peaks_total

    while flags >= 1:

        if is_possible(flags, peaks):
            break
        flags -= 1

    return flags


def is_possible(flags, peaks):
    n = len(peaks)
    distance_amt = flags
    i = peaks[0]
    while i < n and flags > 0:
        try:
            flags -= 1
            i = peaks[i+distance_amt]
        except IndexError:
            break

    return True if flags == 0 else False

if __name__ == "__main__":
    print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])) #3
    print(solution([1,2,3])) #0
    print(solution([1,4,2])) #1
    print(solution([1,1,1])) #0
    print(solution([3,2,1])) #0