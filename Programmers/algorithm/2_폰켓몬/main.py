# goal: N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 폰켓몬을 선택하는
# 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return
# 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
#   - nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
#   - 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
#   - 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.

# Example
#   1) [3,1,2,3]
#       -[3,1] 2마리
#       -[3,2] 2마리
#       -[3,3] 1마리
#       -[1,2] 2마리
#       -[1,3] 2마리
#       -[2,3] 2마리

# 최대 두마리

#   2) [3,3,3,2,2,4]
# 최대 세마리 [2,3,4]

#   3) [3,3,3,2,2,2]
# 최대 두마리 [2,3]

# Pseudocode
#    create set of nums (nums_set)
#   if length of nums_set is greater than len(nums) // 2, then return len(nums) // 2
#   if length of nums_set is less than len(nums) // 2, then return len(nums_set)

def solution(nums):
    answer = 0
    N =len(nums)
    #   create set of nums (nums_set)
    nums_set = set(nums)

    #   if length of nums_set is greater than len(nums) // 2, then return len(nums) // 2
    if len(nums_set) > (N // 2):
        return (N // 2)
    else:
        #   if length of nums_set is less than or equal to len(nums) // 2, then return len(nums_set)
        return len(nums_set)
    return answer

if __name__ == "__main__":
    print(solution([3,1,2,3])) #2
    print(solution([3,3,3,2,2,4])) #3
    print(solution([3,3,3,2,2,2])) #2
    print(solution([3,3])) #1
    print(solution([3,2])) #2
