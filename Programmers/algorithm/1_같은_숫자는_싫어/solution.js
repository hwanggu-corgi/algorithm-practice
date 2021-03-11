function solution(arr)
{
    let answer = [];
    let current = -1;

    // if number is current, then skip
    // if not, then push to answer
    for (let number of arr) {
        if (number !== current) {
            answer.push(number);
            current = number;
        }
    }

    // return result
    return answer;
}


console.log(solution([1,1,3,3,0,1,1])); // [1,3,0,1]
console.log(solution([4,4,4,3,3]));     // [4,3]