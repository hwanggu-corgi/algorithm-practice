# goal: 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열
# completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

def solution(participant, completion):
    temp = {}

    for person in participant:
        if not person in temp:
            temp[person] = 1

        else:
            temp[person] += 1

    for person in completion:
        temp[person] -= 1

    for person in temp:
        if temp[person] == 1:
            answer = person
            break

    return answer