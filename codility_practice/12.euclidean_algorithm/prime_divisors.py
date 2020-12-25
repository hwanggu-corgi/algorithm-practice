# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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
    # get gcd
    bigger = max(a,b)
    smaller = min(a,b)
    gcd_ab = gcd(bigger, smaller)

    # if a / gcd > 1 and b / gcd > 1, return False
    if (a / gcd_ab > 1) and (b / gcd_ab > 1):
        return False

    # if a / gcd == 1 and b / gcd == 1, return True
    if (a / gcd_ab == 1) and (b / gcd_ab == 1):
        return True

    # if a/gcd == 1 and b / gcd > 1 and gcd % b == 0, return True
    if (a / gcd_ab == 1) and (b / gcd_ab > 1) and (gcd_ab % (b/gcd_ab) == 0):
        return True
    else:
        return False

    # if b/gcd == 1 and a/ gcd > 1 and gcd % a == 0, return True
    if (b / gcd_ab == 1) and (a / gcd_ab > 1) and (gcd_ab % (a/gcd_ab) == 0):
        return True
    else:
        return False

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

# def solution(A, B):
#     n = len(A)
#     i = 0
#     count = 0
#     while i < n:
#         if check(A[i], B[i]):
#             count += 1
#         i += 1

#     return count


# def check(a, b):
#     # Factorize a and b
#     bigger = max(a,b)

#     prime_factors = arrayF(bigger)

#     a_factors = factorize(a, prime_factors)
#     b_factors = factorize(b, prime_factors)

#     # check if primes are the same
#     if b_factors == a_factors:
#         return True
#     else:
#         return False

# def arrayF(n):
#     F = [0] * (n+1)
#     i = 2
#     while (i * i <= n):
#         if (F[i] == 0):
#             k = i * i
#             while k <= n:
#                 if F[k] == 0:
#                     F[k] = i
#                 k += i
#         i += 1

#     return F
# def factorize(x,F):
#     prime_factors = set()
#     while (F[x] > 0):
#         prime_factors.add(F[x])
#         x //= F[x]
#     prime_factors.add(x)
#     return prime_factors


if __name__ == "__main__":
    print(solution([15, 10, 9], [75, 30, 5])) #1