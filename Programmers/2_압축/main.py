#goal: 주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.

# 제한 사항
#   - 입력으로 영문 대문자로만 이뤄진 문자열 msg가 주어진다.
#   - msg의 길이는 1 글자 이상, 1000 글자 이하이다.

# 과정
#   - 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
#   - 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
#   - w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
#   - 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
#   - 단계 2로 돌아간다.

# Example
#   1. KAKAO
#       - K exists         --> "K":11 , {"A": 1, "B": 2, "C": 3, ..., "Z": 26}, [11]
#       - KA doesn't exist --> "KA":27 , {"A": 1, "B": 2, "C": 3, ..., "Z": 26, "KA": 27}, [11]
#       - A exists         --> "A": 1, {"A": 1, "B": 2, "C": 3, ..., "Z": 26, "KA": 27}, [11,1]
#       - AK doesn't exist --> "AK": 28, {"A": 1, "B": 2, "C": 3, ..., "Z": 26, "KA": 27, "AK": 28}, [1, 11]
#       - KA exist         --> "KA":27 , {"A": 1, "B": 2, "C": 3, ..., "Z": 26, "KA": 27}, [1,11,27]
#       - O exists         --> "O": 15, {"A": 1, "B": 2, "C": 3, ..., "Z": 26, "KA": 27, "AK": 28}, [1, 11, 27, 15]
#       - KAO doesnt exist --> "KAO": 29, {"A": 1, "B": 2, "C": 3, ..., "Z": 26, "KA": 27, "AK": 28, "KAO": 29}, [27, 28]

# 1. start with current_index=ending_index=0
# 2. check if msg[current_index:ending_index+1] is in dictionary
# 3. if exists, get number and add to array
# 3.1. move ending_index by 1
# 4. if doesn't exist, add to directionary with assigned number
# 4.1. set current_index to be the index where letter doesn't exist
# 4.2. move ending_index by 1

def solution(msg):
    answer = []
    return answer 