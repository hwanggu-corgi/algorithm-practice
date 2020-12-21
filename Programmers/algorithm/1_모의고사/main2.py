# goal: 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은
# 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]
    N_p1 = len(pattern_1)
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    N_p2 = len(pattern_2)
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    N_p3 = len(pattern_3)

    correct_count = [[1,0] [2,0], [3,0]]

    # add counts
    for index, answer in enumerate(answers):
        if pattern_1[index % N_p1] == answer:
            correct_count[0][1] += 1

    # return person in increasing order if correct count is the same
    return answer