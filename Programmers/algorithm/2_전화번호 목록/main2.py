# goal: 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤
#       번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution
#       함수를 작성해주세요.

# 제한 사항
#   phone_book의 길이는 1 이상 1,000,000 이하입니다.
#   각 전화번호의 길이는 1 이상 20 이하입니다.

def solution(phone_book):
    answer = True

    # for each number in phone_book
    # find smaller phone number
    # find larger phone number
    # check if smaller is in larger phone number
    # if yes, then break and return false
    # if all is well, then return true
    return answer