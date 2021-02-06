# goal: 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤
#       번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution
#       함수를 작성해주세요.

# 제한 사항
#   phone_book의 길이는 1 이상 1,000,000 이하입니다.
#   각 전화번호의 길이는 1 이상 20 이하입니다.

def solution(phone_book):
    # for each number in phone_book
    n = len(phone_book)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            smaller = min(phone_book)
            larger =  phone_book[j] if smaller == phone_book[i] else phone_book[i]
            if smaller in larger:
                return False
            j += 1
        i += 1
    return True

if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"])) #False
    print(solution(["123", "456", "789"])) #True
    print(solution(["97674223", "119", "1195524421"])) #False
