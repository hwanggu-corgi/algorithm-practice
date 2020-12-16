function solution(strings, n) {
    // sort strings in increasing order
    strings = strings.sort();
    // sort strings by nth index
    strings = strings.sort((a,b) => {
        if (a[n] > b[n]) {
            return 1;
        } else if (a[n] == b[n]) {
            return 0;
        } else {
            return -1;
        }
    });

    let answer = strings;
    return answer;
}

console.log(solution(["sun", "bed", "car"], 1));
console.log(solution(["abce", "abcd", "cdx"], 2));