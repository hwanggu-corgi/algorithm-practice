function solution(array, commands) {
    var answer = [];
    for (let command of commands) {
        let sliced_arr = array.slice(command[0]-1, command[1]).sort((a,b) => a - b);
        answer.push(sliced_arr[command[2] - 1]);
    }

    return answer;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])); // [5, 6, 3]