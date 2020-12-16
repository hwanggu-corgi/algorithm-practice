function solution(s){
    let stack = [];
    for (let parenthesis of s) {
        if (parenthesis == "(") {
            stack.push(parenthesis);
        } else {
            if (stack.length == 0) {
                return false;
            }

            stack.pop();
        }
    }

    if (stack.length > 0) {
        return false;
    }

    return true;
}

console.log(solution("()()"));