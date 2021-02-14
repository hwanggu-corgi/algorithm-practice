# goal: 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를
# 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

def solution(phone_number):
    n = len(phone_number)
    if n - 4 <= 0:
        return phone_number

    return "*" * (n - 4) + phone_number[n-4:]


if __name__ == "__main__":
    print(solution("01033334444")) # *******4444
    print(solution("027778888")) # *****8888
    print(solution("22")) # 22
    print(solution("4444")) # 4444
    print(solution("44444")) # *4444