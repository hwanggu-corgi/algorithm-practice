# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를
# 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
#   시험은 최대 10,000 문제로 구성되어있습니다.
#   문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
#   가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.


def solution(answers):
    answer = []
    student1_solution = [1, 2, 3, 4, 5]
    n1 = len(student1_solution)
    student2_solution = [2, 1, 2, 3, 2, 4, 2, 5]
    n2 = len(student2_solution)
    student3_solution = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    n3 = len(student3_solution)

    score = [0,0,0]

    # score test
    for index, correct in enumerate(answers):
        if student1_solution[index % n1] == correct:
            score[0] += 1

        if student2_solution[index % n2] == correct:
            score[1] += 1

        if student3_solution[index % n3] == correct:
            score[2] += 1

    # find the highest score
    max_score = max(score)

    # return person with highest score
    if score[0] == max_score:
        answer.append(1)
    if score[1] == max_score:
        answer.append(2)
    if score[2] == max_score:
        answer.append(3)

    return answer

if __name__ == "__main__":
    print(solution([1,2,3,4,5])) # [1]
    print(solution([1,3,2,4,2])) # [1,2,3]