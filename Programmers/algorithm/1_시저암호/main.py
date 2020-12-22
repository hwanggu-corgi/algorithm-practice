# goal: 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

def solution(s, n):
    s = [x for x in s]
    n = len(s)

    i = 0
    while i < n:

        if s[i] = s[i].lower():
            new_char = ((ord(s[i]) - ord('a')) + n) % 26
            s[i] = chr(ord('a') + new_char)
        else:
            new_char = ((ord(s[i]) - ord('A')) + n) % 26
            s[i] = chr(ord('A') + new_char)
        i+=1

    answer = "".join(s)

    return answer