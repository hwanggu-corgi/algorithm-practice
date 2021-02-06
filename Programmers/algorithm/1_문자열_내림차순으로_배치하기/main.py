# goal: 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을
# 완성해주세요.

# 제한 사항
#   str은 길이 1 이상인 문자열입니다.

def solution(s):
    lowercase_s = sorted([x for x in s if x.islower()], reverse=True)
    uppercase_s = sorted([x for x in s if x.isupper()], reverse=True)
    answer = ''.join(lowercase_s + uppercase_s)
    return answer

if __name__ == "__main__":
    print(solution("Zbcdefg"))