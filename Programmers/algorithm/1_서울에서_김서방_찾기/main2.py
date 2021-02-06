# goal: String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을
#       반환하는 함수, solution을 완성하세요.

def solution(seoul):
    index = seoul.index("Kim")
    return "김서방은 {}에 있다".format(index)