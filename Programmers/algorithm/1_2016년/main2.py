# goal: 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아
# 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

from datetime import datetime

def solution(a, b):
    answer = ''
    day = datetime.strptime("{}-{}-2016".format(a,b), "%m-%d-%Y").strftime("%a")
    answer = day.upper()
    return answer