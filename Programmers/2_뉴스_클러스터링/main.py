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
#   - divide str1 into list of two characters (str1_set). do the same for str2 (str2_set)
#   - find the length of the union of str1_set and str2_set
#   - find the length of intersection of str1_set and str2_set
#   - if the length of intersection is 0, then return 1 * 65536
#   - else, return int(length of intersection / length of union) * 65536


def solution(str1, str2):

    # divide str1 into set of two characters (str1_set). do the same for str2 (str2_set)
    str1_set = create_set(str1)
    str2_set = create_set(str2)
    # find the length of the union of str1_set and str2_set
    length_union = calculate_union_length(str1_set, str2_set)
    print(length_union)
    # find the length of intersection of str1_set and str2_set
    length_intersection = calculate_intersection_length(str1_set, str2_set)
    print(length_intersection)
    # if the length of intersection is 0, then return 1 * 65536
    if length_intersection == 0:
        return 1 * 65536
    else:
        # else, return int(length of intersection / length of union) * 65536
        j = int((length_intersection / length_union) * 65536)

    answer = j
    return answer

def create_set(s):
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

def calculate_union_length(set1, set2):
    length = 0
    common_keys = []
    frequency_set1 = {}
    frequency_set2 = {}
    print(set1)
    print(set2)

    # count frequency of each element in set1
    for e in set1:
        if e not in frequency_set1:
            frequency_set1[e] = 1
        else:
            frequency_set1[e] += 1

    # count frequency of each element in set2
    for e in set2:
        if e not in frequency_set2:
            frequency_set2[e] = 1
        else:
            frequency_set2[e] += 1

    # calculate length
    if len(frequency_set1) > len(frequency_set2):
        for key in frequency_set2:
            if key in frequency_set1:
                length += max(frequency_set1[key], frequency_set2[key])
                common_keys.append(key)
    else:
        for key in frequency_set1:
            if key in frequency_set2:
                length += max(frequency_set1[key], frequency_set2[key])
                common_keys.append(key)

    # clean up
    for key in common_keys:
        del frequency_set1[key]
        del frequency_set2[key]

    # calculate remaining length
    if len(frequency_set1) > 0:
        for key in frequency_set1:
            length += frequency_set1[key]

    if len(frequency_set2) > 0:
        for key in frequency_set1:
            length += frequency_set1[key]


    return length


def calculate_intersection_length(set1, set2):
    length = 0
    frequency_set1 = {}
    frequency_set2 = {}

    # count frequency of each element in set1
    for e in set1:
        if e not in frequency_set1:
            frequency_set1[e] = 1
        else:
            frequency_set1[e] += 1

    # count frequency of each element in set2
    for e in set2:
        if e not in frequency_set2:
            frequency_set2[e] = 1
        else:
            frequency_set2[e] += 1

    # calculate length
    if len(frequency_set1) > len(frequency_set2):
        for key in frequency_set2:
            if key in frequency_set1:
                length += min(frequency_set1[key], frequency_set2[key])
    else:
        for key in frequency_set1:
            if key in frequency_set2:
                length += min(frequency_set1[key], frequency_set2[key])

    return length


if __name__ == "__main__":
    print(solution("FRANCE", "french")) #16384
    print(solution("handshake", "shake hands")) #65536