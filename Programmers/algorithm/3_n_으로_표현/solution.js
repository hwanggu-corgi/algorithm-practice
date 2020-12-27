

function solution(N, number) {
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
            if (!(k.toString() in dp)) {
                continue;
            }

            for (let a of dp[j.toString()]) {
                for (let b of dp[k.toString()]) {
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
    return -1;
}

console.log(solution(5, 12)) // 4
console.log(solution(2, 11)) // 3
console.log(solution(5, 5)) // 1
console.log(solution(1, 111)) // 3