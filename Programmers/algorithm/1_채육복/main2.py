# goal: 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온
# 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을
# return 하도록 solution 함수를 작성해주세요.

def solution(n, lost, reserve):
    answer = 0
    lost_set = set(lost)
    reserve_set = set(reseve)

    # filter who has spare but lost
    lost_set = lost_set - reserve_set
    reserve_set = reserve_set - lost_set

    # give spares

    # calculate total who takes lessons
    return answer