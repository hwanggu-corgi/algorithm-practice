// pseudocode
//  map element in numbers to string && multiply e by 3
//  sort elements in string in reverse
//  reduce elements in array to a single string
//  return value

function solution(numbers) {
    //  map element in numbers to string && multiply e by 3
    numbers = numbers.map(x => [x.toString(), x.toString().repeat(3)]);
    //  sort elements in string in reverse

    numbers = numbers.sort((a,b) => {
        if (a[1] > b[1]) {
            return -1;
        } else if (a[1] == b[1]) {
            return 0;
        } else {
            return 1;
        }
    });
    //  reduce elements in array to a single string
    let answer = numbers.reduce((acc, val) => acc += val[0], '');
    //  return value

    if (parseInt(answer) == 0) {
        answer = "0";
    }

    return answer;
}

console.log(solution([6, 10, 2])); // 6210

console.log(solution([40,403]))
console.log(solution([10,101]))
console.log(solution([1,11, 111, 1111]))
console.log(solution([0,0, 0, 0]))
console.log(solution([121, 12]))
console.log(solution([0, 0, 1, 10, 1000]))
console.log(solution([1, 10, 1000]))
console.log(solution([1, 10, 110]))
console.log(solution([6, 10, 2]))
console.log(solution([6]))
console.log(solution([0,1]))
console.log(solution([8,886,884]))