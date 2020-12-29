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

# create a dictionary of queue called 'destinations' with items in queue sorted in alphabetical order
# create a variable called answer (val [])
# create a variable called current_airport (val "ICN")
# while len(answer) is not n
# popleft destination[current_airport]
# Add popped value to answer and current_airport


def solution(tickets):
    answer = []
    return answer

if __name__ == "__main__":
    print(solution())