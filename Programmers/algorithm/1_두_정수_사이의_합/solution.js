// goal: 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수,
// solution을 완성하세요.

function solution(a, b) {
    var answer = 0;
    let total_sum = 0;
    let smaller = Math.min(a,b);
    let larger = Math.max(a,b);
    for (let i = smaller; i <= larger; i++) {
        total_sum += i;
    }
    answer = total_sum;
    return answer;
}