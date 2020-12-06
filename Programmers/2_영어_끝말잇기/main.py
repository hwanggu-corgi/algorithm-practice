# goal: 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저
# 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution
# 함수를 완성해주세요.

# 제한 사항
#   - 끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수입니다.
#   - words는 끝말잇기에 사용한 단어들이 순서대로 들어있는 배열이며, 길이는 n 이상 100 이하입니다.
#   - 단어의 길이는 2 이상 50 이하입니다.
#   - 모든 단어는 알파벳 소문자로만 이루어져 있습니다.
#   - 끝말잇기에 사용되는 단어의 뜻(의미)은 신경 쓰지 않으셔도 됩니다.
#   - 정답은 [ 번호, 차례 ] 형태로 return 해주세요.
#   - 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.

# Example
#   1. ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
#       - Person who said tank last is out (repeat)

#   2. ["hello", "one", "even", "never", "now", "world", "draw"]
#       - Person who got the connecting word wrong is out

# Example - detail
#   1. ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
#
#      1) {}
#         {1:0,2:0,3:0} --> raise word count player 1
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#              ^

#      2) {}
#         {1:1,2:0,3:0}
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#              ^

#      3) {}
#         {1:1,2:0,3:0} --> check if word connects --> skip since it's the first word
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#              ^

#      4) {}
#         {1:1,2:0,3:0} --> check if word in set --> No --> Add to set
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#              ^

#      5) {"tank"}
#         {1:1,2:0,3:0}
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#              ^

#      7) {"tank"}
#         {1:1,2:0,3:0} --> raise word count player 2
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#                          ^

#      8) {"tank"}
#         {1:1,2:1,3:0}
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#                          ^

#      9) {"tank"}
#         {1:1,2:1,3:0} --> check if word connects --> yes
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#                          ^

#      10){"tank"}
#         {1:1,2:1,3:0} --> check if word in set --> No --> Add to set
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#                          ^

#      11){"tank", "kick"}
#         {1:1,2:1,3:0}
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#                          ^

#      12){"tank", "kick"}
#         {1:1,2:1,3:0} --> raise word count player 3
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#                                       ^

#      13){"tank", "kick"}
#         {1:1,2:1,3:1}
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#                                       ^


#      14){"tank", "kick"}
#         {1:1,2:1,3:1} --> check if word connects --> yes
#         [["tank",1], ["kick",2], ["know",3], ["wheel",1], ["land",2], ["dream",3], ["mother",1], ["robot",2], ["tank",3]]
#                                       ^

#   2. ["hello", "one", "even", "never", "now", "world", "draw"]
#       - Person who got the connecting word wrong is out

# Pseudocode
#

def solution(n, words):
    answer = []

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer