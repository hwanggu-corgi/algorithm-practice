from collections import Counter

def solution(s):
    count = Counter(s.lower())
    return True if count['p'] == count['y'] else False

if __name__ == "__main__":
    print(solution("pPoooy"))  # False
    print(solution("pPoooyY")) # True