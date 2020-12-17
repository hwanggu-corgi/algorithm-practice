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
    return answer;
}

console.log(solution([6, 10, 2])); // 6210