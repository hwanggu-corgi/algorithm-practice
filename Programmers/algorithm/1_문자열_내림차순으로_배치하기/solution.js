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

    let lowercase_s = get_lowercase_s(s);
    let uppercase_s = get_uppercase_s(s);

    let answer = s.split("").reverse().join("");
    return answer;
}

let lowercase_s = (s) => {
    let res = "";
    for(let char of s) {
        if (s.lowercase() == s) {

        }
    }
};

let uppercase_s = (s) => {

};


console.log(solution("Zbcdefg"));