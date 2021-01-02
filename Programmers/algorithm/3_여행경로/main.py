# goal: 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에
# 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
#   - 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
#   - 주어진 공항 수는 3개 이상 10,000개 이하입니다.
#   - tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
#   - 주어진 항공권은 모두 사용해야 합니다.
#   - 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
#   - 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

# Example
#
#                   ICN
#               ATL     SFO
#            ICN   SFO
#         SFO
#      ATL
#   SFO


# Example 2
#   [["ICN","BOO"],["ICN","COO"],["COO","ICN"]]
#   {"ICN": ["BOO", "COO"], "COO": ["ICN"]}
#
#                   ICN
#                BOO  COO
#                       ICN
#                         BOO
#


# Pesudocode
#   1. Separate tickets by {airport: [list of destinations]}
#   2. find the length of expected output
#   3. Start with ICN, travel each destination
#   4. If path terminates(if doesn't exist, or tickets_dict[airport] == []), check and see if the count matches expected output
#   5. If so, return answer
#   6. otherwise, return (back track)
#   7. copy tickets_dict
#   8. copy answer
#   11. for each element in tickets_dict[airport]
#   12. pop element from tickets_dict[airport]
#   13. append element to array
#   14. move to next destination (travel(new_airport, tickets_dict, answer))
#   15. return array with greater length

def solution(tickets):

    return answer


# Pesudocode
#   1. Separate tickets by {airport: [list of destinations]}
#   2. Start with ICN, check first destination
#   3. if first destination doesn't exist, backtrack and move to next
#   4. pop the destination and put to output array
#   5. go to the airport
#   6. go to the first destination
#   7. repeat step 2 to 6 until all has been traveled

# def solution(tickets):
#     answer = ["ICN"]
#     tickets_dict = {}

#     for ticket in tickets:
#         airport = ticket[0]
#         destination = ticket[1]
#         if airport in tickets_dict:
#             tickets_dict[airport].append(destination)
#         else:
#             tickets_dict[airport] = [destination]
#         print(tickets_dict)
#     for key in tickets_dict:
#         tickets_dict[key].sort()

#     travel("ICN", tickets_dict, answer)
#     print(tickets_dict)
#     return answer

# def travel(airport, tickets_dict, answer):
#     new_airport = ""

#     while len(tickets_dict[airport]) != 0:
#         i = 0
#         while i < len(tickets_dict[airport]):
#             new_airport = tickets_dict[airport][i]
#             if len(tickets_dict.get(new_airport, [])) != 0:
#                 break

#             i += 1

#         if i == len(tickets_dict[airport]):
#             answer.append(new_airport)
#             return

#         tickets_dict[airport].pop(i)
#         answer.append(new_airport)
#         travel(new_airport, tickets_dict, answer)


# Example
#   1) tickets: [[ICN, JFK], [HND, IAD], [JFK, HND]]
#       - ICN -> JFK -> HND -> IAD
#       ["ICN", "JFK", "HND", "IAD"]

#   2) tickets: [[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]]
#       - {ICN: {ATL, SFO}, SFO: {ATL}, ATL: {ICN, SFO}}
#       ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# Detailed Example

#   2) tickets: [[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]]

#       - [[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]] --> generate queue of items in dictionary order --> {ICN: [ATL, SFO], SFO: [ATL], ATL: [ICN, SFO]}
#       - start from first value of ICN
#         {ICN: [ATL, SFO], SFO: [ATL], ATL: [ICN, SFO]} []

#       - add ICN to answer and current_airport
#         {ICN: [ATL, SFO], SFO: [ATL], ATL: [ICN, SFO]} answer = ["ICN"] current_airport = "ICN"

#       - pop left destination["ICN"] --> ATL
#         "ATL" {ICN: [SFO], SFO: [ATL], ATL: [ICN, SFO]} ["ICN"] answer = ["ICN"] current_airport = "ICN"

#       - Add ATL to answer and current_airport
#         {ICN: [SFO], SFO: [ATL], ATL: [ICN, SFO]} answer = ["ICN", "ATL"] current_airport = "ATL"

#       - pop left destination["ATL"] --> ICN
#         "ICN" {ICN: [SFO], SFO: [ATL], ATL: [SFO]} answer = ["ICN"] answer = ["ICN"] current_airport = "ICN"

#       - Add ICN to answer and current_airport
#         {ICN: [SFO], SFO: [ATL], ATL: [SFO]} answer = ["ICN", "ATL", "ICN"] current_airport = "ICN"

#       - pop left destination["ICN"] --> SFO
#         "SFO" {ICN: [], SFO: [ATL], ATL: [SFO]} answer = ["ICN", "ATL", "ICN"] current_airport = "ICN"

#       - Add SFO to answer and current_airport
#         {ICN: [], SFO: [ATL], ATL: [SFO]} answer = ["ICN", "ATL", "ICN", "SFO"] current_airport = "SFO"

#       - pop left destination["SFO"] --> ATL
#         "ATL" {ICN: [], SFO: [], ATL: [SFO]} answer = ["ICN", "ATL", "ICN", "SFO"] current_airport = "SFO"

#       - Add SFO to answer and current_airport
#         {ICN: [], SFO: [], ATL: [SFO]} answer = ["ICN", "ATL", "ICN", "SFO", "ATL"] current_airport = "ATL"


#       ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# pseudocode

# create a dictionary of queue called 'queue' with items in queue sorted in alphabetical order
# create a variable called answer (val [])
# create a variable called current_airport (val "ICN")
# while len(answer) is not n
# popleft destination[current_airport]
# Add popped value to answer and current_airport



# from collections import deque

# def solution(tickets):
#     n = len(tickets)
#     # create a variable called answer (val [])
#     answer = ["ICN"]
#     # create a dictionary of queue called 'queue' with items in queue sorted in alphabetical order
#     queue = create_queue(tickets)
#     # create a variable called current_airport (val "ICN")
#     current_airport = "ICN"
#     final_destination = ""

#     # while len(answer) is not n
#     while len(queue[current_airport]) > 0:
#         # popleft queue[current_airport]
#         tmp = queue[current_airport].popleft()

#         if len(queue[tmp]) == 0 and not final_destination:
#             final_destination = tmp
#             continue

#         # Add popped value to answer and current_airport
#         answer.append(tmp)
#         current_airport = tmp

#     answer.append(final_destination)
#     current_airport = final_destination

#     while len(queue[current_airport]) > 0:
#         tmp = queue[current_airport].popleft()

#         answer.append(tmp)
#         current_airport = tmp

#     return answer

# def create_queue(tickets):
#     res = {}

#     for start, target in tickets:
#         if start not in res:
#             res[start] = [target]
#         else:
#             res[start].append(target)

#         if target not in res:
#             res[target] = []

#     for key in res:
#         res[key].sort()
#         res[key] = deque(res[key])

#     return res


# from collections import deque

# def solution(tickets):
#     n = len(tickets)
#     # create a variable called answer (val [])
#     answer = ["ICN"]
#     # create a dictionary of queue called 'queue' with items in queue sorted in alphabetical order
#     queue = create_queue(tickets)
#     # create a variable called current_airport (val "ICN")
#     current_airport = "ICN"

#     # while len(answer) is not n
#     while len(queue[current_airport]) > 0:
#         # popleft queue[current_airport]
#         tmp = queue[current_airport].popleft()
#         # Add popped value to answer and current_airport
#         answer.append(tmp)
#         current_airport = tmp

#     return answer

# def create_queue(tickets):
#     res = {}

#     # ticket 정보 dictionary 안에 집어 넣기
#     for start, target in tickets:
#         if start not in res:
#             res[start] = [target]
#         else:
#             res[start].append(target)

#         if target not in res:
#             res[target] = []

#     # dictionary 안에있는 list를 오름차순으로 정렬
#     # dictionary 안에있는 list를 큐로 변경
#     for key in res:
#         res[key].sort()
#         res[key] = deque(res[key])

#     return res

if __name__ == "__main__":
    print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]])) # [ICN, A, ICN, A]
    # print(solution([["ICN", "A"], ["A", "ICN"], ["ICN", "A"]])) # [ICN, A, ICN, A]
    # print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]])) # [ICN, A, D, B, A, C]
    # print(solution([["ICN","BOO"],["ICN","COO"],["COO","ICN"]])) # [ICN, COO, ICN, BOO]
    # print(solution([["ICN","A"],["A","B"],["B","A"],["A","ICN"],["ICN","A"]])) # [ICN,A,B,A,ICN,A]
    # print(solution([["ICN", "A"], ["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A","ICN"]])) #[ICN, ATL, ICN, SFO, ATL, SFO]
    # print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) #[ICN, ATL, ICN, SFO, ATL, SFO]
    # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) #[ICN, JFK, HND, IAD]