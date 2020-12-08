# goal: 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로,
# 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

# Example
#   1) FRANCE	french
#       A= {FR, RA, AN, NC, CE}  B = {FR, RE, EN, NC, CH}
#   A U B = {FR, RA, AN, CE, RE, EN, CH}
#   A n B = {FR, }

def solution(str1, str2):
    answer = 0
    return answer