#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, n):
        storage = {}
        return self.fib(n, storage)

    def fib(self, n, storage):
        if n == 1:
            return 1

        if n == 0:
            return 0

        if n in storage:
            return storage[n]

        res = self.fib(n-1, storage) + self.fib(n-2, storage)

        storage[n] = res

        return res