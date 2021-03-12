function solution(s) {
    if (s.length !== 4 && s.length !== 6) {
        return false;
    }
    const found = s.match(/[^0-9]/);
    return found && found.length > 0 ? false : true;
}

console.log(solution("a234")); // false
console.log(solution("1234")); // true