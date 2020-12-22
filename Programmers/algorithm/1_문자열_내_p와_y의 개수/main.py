from collections import Counter

def solution(s):
    count = Counter(s.lower())
    return True if count['p'] == count['y'] else False