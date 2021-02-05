def solution(s):
    answer = ''
    center = len(s) // 2

    # if even return two
    if len(s) % 2 == 0:
        answer = s[center-1] + s[center]
    else:
    # if odd return char at the center
        answer = s[center]

    return answer

if __name__ == "__main__":
    print(solution("abcde")) #c
    print(solution("qwer")) #we