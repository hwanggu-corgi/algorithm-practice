
def gcd(a,b):
    if a % b == 0:
        return b

    return gcd(b, a % b)

def lcm(a,b):
    return (a * b) // gcd(a,b)

def solution(n, m):
    return [gcd(n,m), lcm(n,m)]

if __name__ == "__main__":
    print(solution(3, 12)) # [3, 12]
    print(solution(2, 5))  # [1, 10]