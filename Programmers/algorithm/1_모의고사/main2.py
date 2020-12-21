def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]
    N_p1 = len(pattern_1)
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    N_p2 = len(pattern_2)
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    N_p3 = len(pattern_3)

    correct_count = [[1,0], [2,0], [3,0]]

    for index, answer in enumerate(answers):
        if pattern_1[index % N_p1] == answer:
            correct_count[0][1] += 1

        if pattern_2[index % N_p2] == answer:
            correct_count[1][1] += 1

        if pattern_3[index % N_p3] == answer:
            correct_count[2][1] += 1

    max_count = max(correct_count, key=lambda e: e[1])[1]
    correct_count = sorted(correct_count, key= lambda e: e[1])
    answer = [x[0] for x in correct_count if x[1] == max_count]
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))
    print(solution([[1, 3, 2, 4, 2]]))