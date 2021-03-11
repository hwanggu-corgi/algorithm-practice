function solution(arr, divisor) {
    var answer = [];

    for (let number of arr) {
        if (number % divisor === 0) {
            answer.push(number);
        }
    }
    if (answer.length === 0) {
        return [-1];
    } else {
        return answer.sort((a,b) => a - b);
    }
}

console.log(solution([5, 9, 7, 10], 5)); // [5, 10]
console.log(solution([2, 36, 1, 3], 1)); // [1, 2, 3, 36]
console.log(solution([3,2,6], 10)); // [-1]