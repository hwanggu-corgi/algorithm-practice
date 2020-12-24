# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# count elements in A store in dictionary count


def solution(A):
    n = len(A)
    a_count = {}
    b_count = {}
    for a in A:
        if a not in a_count:
            a_count[a] = 1
        else:
            a_count[a] += 1

    for a in a_count:
        divisors_count = 0
        b = 1
        while b * b <= a:
            # put count of a // b in dictionary by b
            if a % b == 0:
                print("{} {}".format(a,b))
                print(a_count)
                c = a // b
                if b in a_count:
                    b_count[b] = b_count[b] + a_count[a] if b in b_count else a_count[a]

                if c in a_count:
                    b_count[c] = b_count[c] + a_count[a] if c in b_count else a_count[a]
                print(b_count)
            b += 1
    answer = [b_count[x] for x in A]
    return answer


# def solution(A):
#     n = len(A)
#     answer = [0] * n

#     A = [x for x in zip(range(n), A)]
#     A.sort(key= lambda e: e[1])

#     for index_a, a in enumerate(A):
#         non_divisors_count = 0
#         for index_b, b in enumerate(A):
#             if index_a == index_b:
#                 continue

#             if b[1] > a[1]:
#                 non_divisors_count += n - index_b
#                 break

#             if a[1] % b[1] != 0:
#                 non_divisors_count += 1

#         answer[a[0]] = non_divisors_count
#     return answer


# for each element in A,
# for each key in count,
# if element % key == 0 --> continue
# else
#   if element == key and count[key] > 0, add count[key] - 1 to total
#   if element != key count[key] to total

# write your code in Python 3.6


# def solution(A):
#     answer = []
#     e_count = {}

#     for e in A:
#         if e not in e_count:
#             e_count[e] = 1
#         else:
#             e_count[e] += 1


#     for a in A:
#         non_divisors_count = 0
#         for key in e_count:
#             if a % key == 0:
#                 continue

#             non_divisors_count += e_count[key]

#         answer.append(non_divisors_count)
#     return answer


if __name__ == "__main__":
    print(solution([3, 1, 2, 3, 6])) #