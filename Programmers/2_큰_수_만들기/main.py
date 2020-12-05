#goal: number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return
# 하도록 solution 함수를 완성하세요.

# 제한 조건
#   - number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
#   - k는 1 이상 number의 자릿수 미만인 자연수입니다.

class Node:
    def __init__(self, value):

class LinkedList:
    def __init__(self, nodes_list):
        N = len(nodes_list)
        self.head = None

        if N == 0:
            return

        self.head = Node(nodes_list[0])

        i = 1
        while i < N:
            self.append(Node(nodes_list[i]))
            i += 1


from collections import deque

def solution(number, k):
    answer = ''

    # convert number to queue
    number_list = deque([x for x in number])
    # find biggest number after removing k
    i = 1
    while k > 0:
        # start off with the second number i in list
        # if number_list[i - 1] < number_list[i], then remove number
        if number_list[i - 1] < number_list[i]:
            number_list.remove(i-1)
            # also decrement k
            k -= 1
        else:
            # else, move i by 1
            i += 1

    # return result
    answer = "".join(list(number_list))
    return answer

if __name__ == "__main__":
    print(solution("1924", 2)) #94