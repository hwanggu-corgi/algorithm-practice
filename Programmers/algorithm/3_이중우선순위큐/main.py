# goal: 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가
# 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

# 제한사항
#   - operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
#   - operations의 원소는 큐가 수행할 연산을 나타냅니다.
#   - 원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
#   - 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

# Examples
#   1) [I 16,D 1]
#       I 16
#       - 최대: [-16]  최소: []
#       D 1
#       - 최대: []    최소: []
#       - [0,0] since empty

#   2) [I 7,I 5,I -5,D -1]
#       I 7
#       - 최대: [-7]  최소: []
#       I 5
#       - 최대: [-7,-5]  최소: []
#       I -5
#       - 최대: [-7,-5]  최소: [5]
#       D -1
#       - 최대: [-7,-5]  최소: []
#
#       [7,5]

# Pesudocode
#   - Create two heap array max and min
#   - for each instruction,
#       - if I -number, then add number to min heap array
#       - if I number, then add -number to max heap array
#       - if D -number, then remove number amount from min heap array
#       - if D number, then remove number amount from max heap array
#       - return max and min number
#           - if min array is empty then return two numbers from max
#           - if max array is empty, then return two highest numbers from min
#           - otherwise, return max and min from max heap array and min heap array

def solution(operations):
    #   - Create two heap array max and min
    #   - for each instruction,
    for instruction in operations:
        # Parse instruction
        parsed = instruction.split(" ")
        # if I -number, then add number to min heap array
        if parsed[0] == "I" and int(parsed[1]) < 0:
        # if I number, then add -number to max heap array
        elif parsed[0] == "I" and int(parsed[1]) >= 0:
        # if D -number, then remove number amount from min heap array
        elif parsed[0] == "D" and int(parsed[1]) < 0:
        # if D number, then remove number amount from max heap array
        else:

    # return max and min number
    #   if min array is empty then return two numbers from max
    #   if max array is empty, then return two highest numbers from min
    #   otherwise, return max and min from max heap array and min heap array
    return answer