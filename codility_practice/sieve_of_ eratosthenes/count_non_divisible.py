# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# count elements in A store in dictionary count

# for each element in A,
# for each key in count,
# if element % key == 0 --> continue
# else
#   if element == key and count[key] > 0, add count[key] - 1 to total
#   if element != key count[key] to total

# write your code in Python 3.6

def solution(A):
    answer = []
    e_count = {}

    for e in A:
        if e not in e_count:
            e_count[e] = 1
        else:
            e_count[e] += 1


    for a in A:
        non_divisors_count = 0
        for key in e_count:
            if a % key == 0:
                continue

            non_divisors_count += e_count[key]

        answer.append(non_divisors_count)
    return answer


if __name__ == "__main__":
    print(solution([3, 1, 2, 3, 6])) #