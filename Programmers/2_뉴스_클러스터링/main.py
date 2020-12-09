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

    # divide str1 into set of two characters (str1_list). do the same for str2 (str2_list)
    str1_list = create_list(str1)
    str2_list = create_list(str2)

    #find common keyword in union and intersection
    common_keys_union = set(str1_list) | set(str2_list)
    common_keys_intersection = set(str1_list) & set(str2_list)

    # find the length of the union of str1_list and str2_list
    length_union = sum([max(str1_list.count(e), str2_list.count(e)) for e in common_keys_union])
    # find the length of intersection of str1_list and str2_list
    length_intersection = sum([min(str1_list.count(e), str2_list.count(e)) for e in common_keys_intersection])
    # if the length of intersection is 0, then return 1 * 65536
    if length_intersection == 0 and length_union == 0:
        return 1 * 65536
    else:
        # else, return int(length of intersection / length of union) * 65536
        j = int((length_intersection / length_union) * 65536)

    answer = j
    return answer

def create_list(s):
    res = []
    N = len(s)
    s = s.upper()
    i = 0
    while i < (N-1):
        if not (s[i].isalpha() and s[i+1].isalpha()):
            i += 1
            continue

        res.append(s[i] + s[i+1])
        i += 1

    return res


if __name__ == "__main__":
    print(solution("FRANCE", "french")) #16384
    print(solution("handshake", "shake hands")) #65536
    print(solution("aa1+aa2", "AAAA12")) #43690
    print(solution("E=M*C^2", "e=m*c^2")) #65536
    print(solution("abc", "def")) #0
    print(solution("abc", "abc")) #65536
    print(solution("++a++", "a+++")) #65536