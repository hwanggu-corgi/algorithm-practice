# goal:  두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을
# 완성하세요
#   - 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다

# 제한 조건
#   - 2016년은 윤년입니다.
#   - 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

def solution(a, b):
    number_of_days = 0
    # write number of days per month
    day_label_by_distance_from_friday = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUES",
                                         5: "WED", 6: "THU"}
    number_of_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # find number of days from January up to month a
    index = a -1
    number_of_days += sum(number_of_days_in_month[:index])

    print(number_of_days)

    # add b to number of days
    number_of_days += b

    # find distance from closest friday
    distance_from_friday = number_of_days % 7

    # find the day name
    answer = day_label_by_distance_from_friday[distance_from_friday]

    return answer

if __name__ == "__main__":
    print(solution(1, 1))
    print(solution(5, 24)) #TUES