from functools import reduce

def solution(a, b):
    return reduce(lambda acc, b: acc + (b[0] * b[1]), zip(a,b), 0)

if __name__ == "__main__":
    print(solution([1,2,3,4], [-3,-1,0,2])) #3
    print(solution([-1, 0, 1], [1, 0, -1])) #-2