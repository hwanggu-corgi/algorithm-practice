# goal: 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요

def solution(x):
    return True if x % sum([int(x) for x in str(x)]) == 0 else False