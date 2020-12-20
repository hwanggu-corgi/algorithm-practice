

function solution(N, number) {
    var answer = 0;
    let dp = {};

    if (N == number) {
        return 1;
    }

    for (let i = 1; i < 9; i ++) {
        dp[i] = new Set();
    }

    for (let i = 1; i < 9; i++) {
        dp[i].add(parseInt(N.toString().repeat(i)));
    }

    for (let number_counts = 1; number_counts < 9; number_counts++) {
        for (let j = number_counts; j >= 1; j--) {
            let k = number_counts - j;
            if (!(k in dp)) {
                continue;
            }

            for (a of dp[j]) {
                for (b of dp[k]) {
                    dp[number_counts].add(a + b)
                    dp[number_counts].add(a - b)
                    dp[number_counts].add(a * b)
                    if (b != 0) {
                        dp[number_counts].add(parseInt(a / b))
                    }

                    if (dp[number_counts].has(number)) {
                        return number_counts
                    }
                }
            }
        }
    }
    return answer;
}

console.log(solution(5, 12)) // 4
console.log(solution(2, 11)) // 3
console.log(solution(5, 5)) // 1
console.log(solution(1, 111)) // 3