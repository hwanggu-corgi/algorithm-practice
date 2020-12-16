// if comparing two lowercase letters, compare as usual
// if comparing two uppercase letters, compare as usual
// if comparing one lowercase and one uppercase letter, priortize lowercase letter

// or

// separate uppercase letters from lowercase letters

// sort lower case letters

// sort uppercase letters

// combine two

function solution(s) {
    let N = s.length;

    let lowercase_s = get_lowercase_s(s).split("").sort().reverse().join("");
    let uppercase_s = get_uppercase_s(s).split("").sort().reverse().join("");

    let answer = lowercase_s + uppercase_s;
    return answer;
}

let get_lowercase_s = (s) => {
    let res = "";
    for(let char of s) {
        if (char.toLowerCase() == char) {
            res += char;
        }
    }

    return res;
};

let get_uppercase_s = (s) => {
    let res = "";
    for(let char of s) {
        if (char.toUpperCase() == char) {
            res += char;
        }
    }

    return res;
};


console.log(solution("Zbcdefg")); // gfedcbZ