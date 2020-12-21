# goal: 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온
# 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을
# return 하도록 solution 함수를 작성해주세요.

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    # filter who has spare but lost
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    # give spares
    for student_number in reserve_set:
        if (student_number - 1) in lost_set:
            lost_set.remove(student_number - 1)
        elif (student_number + 1) in lost_set:
            lost_set.remove(student_number + 1)

    # calculate total who takes lessons
    answer = n - len(lost_set)
    return answer

if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5])) # 5
    print(solution(5, [2, 4], [3])) # 4
    print(solution(3, [3], [1])) # 2