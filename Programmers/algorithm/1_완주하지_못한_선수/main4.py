# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이
# 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
#   마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
#   completion의 길이는 participant의 길이보다 1 작습니다.
#   참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
#   참가자 중에는 동명이인이 있을 수 있습니다.


def solution(participant, completion):
    answer = ''
    count_dict = {}

    # store participants in dict
    for person in participant:
        if person not in count_dict:
            count_dict[person] = 1
        else:
            count_dict[person] += 1

    # subtract completees from participants
    for person in completion:
        count_dict[person] -= 1

    # print non-zero value
    for person in count_dict:
        if count_dict[person] == 1:
            answer = person
            break

    return answer

if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) #Leo