function solution(s) {
    let half = Math.floor(s.length/2)
    // if the length of s is odd, then return s[half]
    // if the length of s is even, then return s[half-1] + s[half]
    return s.length % 2 !== 0 ? s[half] : s[half-1] + s[half];
}


console.log(solution("abcde")); // c
console.log(solution("qwer"));  // we