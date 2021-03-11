function solution(a, b) {
    let answer = 0;
    let lower = Math.min(a,b);
    let upper = Math.max(a,b);

    for (let i = lower; i <= upper; i++) {
        answer += i;
    }
    return answer;
}

console.log(solution(3,5)); //12
console.log(solution(3,3)); //3
console.log(solution(5,3)); //12
