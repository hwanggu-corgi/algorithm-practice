# goal: 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로,
# 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

# Example
#   1) FRANCE	french
#       A= {FR, RA, AN, NC, CE}  B = {FR, RE, EN, NC, CH}
#   A U B = {FR, RA, RE, AN, NC, EN, CE, VH}
#   A n B = {FR, NC}
#
#   J("FRANCE", "FRENCH") = 2/8 = 0.25
#   0.25 * 65536 = 16384.0

# Pseudocode
#   - divide str1 into list of two characters (str1_list). do the same for str2 (str2_list)
#   - find the length of the union of str1_list and str2_list
#   - find the length of intersection of str1_list and str2_list
#   - if the length of intersection is 0, then return 1 * 65536
#   - else, return int(length of intersection / length of union) * 65536


def solution(str1, str2):
    answer = 0
    return answer