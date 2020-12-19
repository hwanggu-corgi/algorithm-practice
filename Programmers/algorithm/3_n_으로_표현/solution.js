// goal: 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N
// 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

// Example
//  1) N: 5     Number: 12
//  12 = 5 + 5 + (5 / 5) + (5 / 5)
//      12 = 60 / 5 = (55 + 5) / 5 <- uses minimal number of 5s
//      12 = 1 + 11 = 1 + 5 + 5 = (5/5) + 5 + 5
//      12 = 2 + 10= 2 + 5 + 5 = 1 + 1 + 5 + 5 = (5/5) + (5/5) + 5 + 5
//      12 = 3 + 9 = 1 + 1 + 1 + 10 - 1 = 1 + 1 + 5 + 5 - 1 = (5/5) + (5/5) + 5 + 5 - (5/5)
//      12 = 4 + 8 = 2 + 2 + 8 = 2 + 2 + 5 + 3 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 5 = (5/5) + (5/5) + (5/5) + (5/5) + (5/5) + (5/5) + (5/5) + (5/5) + 5
//      12 = 5 + 7 = 5 + 1 + 1
//      12 = 6 + 6 = 5 + 1 + 5 + 1
//      12 = 5 + 5 + 1 + 1
//  12 = 55 / 5 + 5 / 5
//      12 = 11 + 1

//  12 = (55 + 5) / 5
//      12 = 60 / 5

// Dynamic Programming
// 0    1   2   3   4   5   6   7   8   9   10
// 0    0   4

// How many different patterns exist with 0 many 5's --> 0
// How many different patterns exist with 1 many 5's --> 0
// How many different patterns exist with 2 many 5's --> 4
//  - 5 x 5
//  - 5 - 5
//  - 5 + 5
//  - 5 / 5
// How many different patterns exist with 3 many 5's --> 16
//  - (5 x 5) + 5
//  - (5 x 5) - 5
//  - (5 x 5) * 5
//  - (5 x 5) / 5
//  - (5 - 5) + 5
//  - (5 - 5) - 5
//  - (5 - 5) * 5
//  - (5 - 5) / 5
//  - (5 + 5) + 5
//  - (5 + 5) - 5
//  - (5 + 5) * 5
//  - (5 + 5) / 5
//  - (5 / 5) + 5
//  - (5 / 5) - 5
//  - (5 / 5) * 5
//  - (5 / 5) / 5

// Cases
//  1. when N == number
//      - return 1
//  2. when N != number
//      - dynamic programming!!


function solution(N, number) {
    var answer = 0;
    return answer;
}