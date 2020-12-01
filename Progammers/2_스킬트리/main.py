# goal: 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질
# 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

#제한 조건
    # - 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
    # - 스킬 순서와 스킬트리는 문자열로 표기합니다.
        # - 예를 들어, C → B → D 라면 CBD로 표기합니다
    # - 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
    # - skill_trees는 길이 1 이상 20 이하인 배열입니다.
    # - skill_trees의 원소는 스킬을 나타내는 문자열입니다.
    # - skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.

def solution(skill, skill_trees):
    answer = 0

    # for each skill_tree in skill trees
    for skill_tree in skill_trees:
        # if skill is not valid in skill_tree, continue
        if not is_valid(skill, skill_tree):
            continue
        # else, add count
        answer += 1

    # return answer

    return answer

def is_valid(skill, skill_tree):
    index_skill = 0
    index_skill_tree = 0

    N_skill = len(skill)
    N_skill_tree = len(skill_tree)

    while index_skill <

    # if index_skill_tree is out of bound and skill[skill_index] is in skill_tree, then return False

    # otherwise, return true

    return True

if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) #2