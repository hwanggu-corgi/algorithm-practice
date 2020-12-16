

function solution(n) {
    var answer = '';
    // for i from 1 to n
    for (let i = 1; i <= n; i++){
        // if i is odd, add 수 to answer
        // if i is even, add 박 to answer
        answer += (i % 2 == 1) ? "수" : "박";
    }
    // return string
    return answer;
}

console.log(solution(1));
console.log(solution(2));
console.log(solution(3));
console.log(solution(4));