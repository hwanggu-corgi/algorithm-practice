# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s2_set = set([x for x in s2])

    for char in s1:
        if char in s2_set:
            return "YES"

    return "NO"


if __name__ == "__main__":
    print(twoStrings("hello", "world")) # YES
    print(twoStrings("hi", "world")) #NO