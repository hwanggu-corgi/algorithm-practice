function solution(s){
    let p_count = 0;
    let y_count = 0;
    s = s.toLowerCase();

    for (let char of s) {
        if (char === "p") {
            p_count += 1;
        } else if (char === "y") {
            y_count += 1;
        }
    }

    return true ? p_count === y_count : false;
}


console.log(solution("pPoooyY")); // true
console.log(solution("Pyy")); // false
