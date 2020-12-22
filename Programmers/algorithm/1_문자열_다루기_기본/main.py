def solution(s):
    try:
        int(s)
        return True if (len(s) == 6 or len(s) == 4) else False
    except:
        return False


if __name__ == "__main__":
    print(solution("a234")) # false
    print(solution("1234")) # true