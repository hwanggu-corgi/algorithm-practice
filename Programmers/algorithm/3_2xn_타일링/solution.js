// goal: 직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return
// 하는 solution 함수를 완성해주세요.

// 타일을 가로로 배치 하는 경우
// 타일을 세로로 배치 하는 경우


// Example
//  1)
//      V V V V --> possible
//      V V V H --> not possible
//      V V H H --> possible
//      V H H V --> possible
//      H H V V --> possible
//      V H H H --> not possible
//      H H H V --> not possible
//      H H H H --> possible


// Creating a permutation
//
// n = 1 -> there is  1 combination (V)
// n = 2 -> there are 2 combinations ([V,V], [2H])
// n = 3 -> there are 3 combinations ([V,V,V], [2H,V], [V,2H])
// n = 4 -> there are 5 combinations ([V,V,V,V], [V,2H,V], [V,V,2H], [2H,V,V], [2H, 2H])

function solution(n) {
    if (n == 0 || n == 1 || n == 2) {
        return n;
    }
    let a = 1;
    let b = 2;
    let i = 3;
    while (i < (n+1)) {
        c = (a + b) % 1000000007;
        b = c;
        a = b;
        i += 1;
    }

    let answer = c;
    return answer;
}

console.log(solution(4)); // 5