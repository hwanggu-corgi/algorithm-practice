# source: https://www.oncoder.com/ground/r1KQacTxQ

#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, n):
        return self.fib(n)

    def fib(self, n):
        if n == 1:
            return 1

        if n == 0:
            return 0

        return self.fib(n-1) + self.fib(n-2)