function solution(strings, n) {
    strings.sort();
    strings.sort((a,b) => {
        if (a[n] > b[n]) {
            return 1;
        } else if (a[n] === b[n]) {
            return 0;
        } else {
            return -1;
        }
    });
    return strings;
}

console.log(solution(["sun", "bed", "car"], 1)); // 	["car", "bed", "sun"]