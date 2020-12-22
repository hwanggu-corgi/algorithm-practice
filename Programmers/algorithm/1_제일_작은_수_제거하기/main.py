# goal: 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요

def solution(arr):
    min_val = min(arr)
    arr.remove(min_val)
    return arr if len(arr) > 0 else [-1]