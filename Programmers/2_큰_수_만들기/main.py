#goal: number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return
# 하도록 solution 함수를 완성하세요.

# 제한 조건
#   - number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
#   - k는 1 이상 number의 자릿수 미만인 자연수입니다.

# class Node:
#     def __init__(self, value):

# class LinkedList:
#     def __init__(self, nodes_list):
#         N = len(nodes_list)
#         self.head = None

#         if N == 0:
#             return

#         self.head = Node(nodes_list[0])

#         i = 1
#         while i < N:
#             self.append(Node(nodes_list[i]))
#             i += 1

from collections import deque

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.end = head

    def append(self, node):
        self.end = node
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node == None:
            self.head = next_node
            next_node.prev = None

        if next_node == None:
            self.end = prev_node
            prev_node.next = None

        if prev_node != None and next_node != None:
            next_node.prev = prev_node
            prev_node.next = next_node


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def solution(number, k):
    answer = ''

    # convert number to queue
    number_list = deque([x for x in number])
    N = len(number_list)
    # find biggest number after removing k
    i = 1
    while k > 0:
        current_node = None
        # start off with the second number i in list
        # if number_list[i - 1] < number_list[i], then remove number
        if number_list[i - 1] < number_list[i]:
            number_list.remove(number_list[i - 1])
            # also decrement k
            i = 1
            k -= 1
        else:
            # else, move i by 1
            i += 1


    while k > 0:
        number_list.pop()
        k -= 1

    # return result
    answer = "".join(list(number_list))
    return answer

if __name__ == "__main__":
    print(solution("1924", 2)) #94
    print(solution("1231234", 3)) #3234
    print(solution("1111", 2)) #11