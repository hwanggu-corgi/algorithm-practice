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


// Pseudocode
//  1) Create permutations of V and H
//  2) for each permutation, check if solution is valid
//  3) if valid, add to count


// Creating a permutation
//

function solution(n) {
    var answer = 0;
    return answer;
}