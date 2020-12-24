# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# pseudocode
# get gcd of A[i] and B[i]
# divide A[i] and B[i] by gcd
# find if prime divisor exists in A[i], if so skip i
# find if prime divisor exists in B[i], if so skip i
# if all is well, return i


# pseudocode
# for each divisor in A
# check if divisor is prime
# if prime, add to set

# for each divisor in B
# check if divisor is in set, if so remove divisor from set
# if not in set, return

def solution(A, B):
    n = len(A)
    i = 0
    count = 0
    while i < n:
        if check(A[i], B[i]):
            count += 1
        i += 1

    return count


def check(a, b):
    # get gcd of A[i] and B[i]
    while True:
        smaller = min(a, b)
        bigger = max(a, b)
        gcd_ab = gcd(bigger, smaller)

        if gcd_ab == 1:
            break
        # divide A[i] and B[i] by gcd
        a /= gcd_ab
        b /= gcd_ab

    # find if prime divisor exists in A[i], if so return False
    if a != 1:
        i = 2
        while i * i <= a:
            if a % i == 0:
                return False
            i += 1
    # find if prime divisor exists in B[i], if so return False
    if b != 1:
        i = 2
        while i * i <= a:
            if a % i == 0:
                return False
            i += 1
    # if all is well, return True