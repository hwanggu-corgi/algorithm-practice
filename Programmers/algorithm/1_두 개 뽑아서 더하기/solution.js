
// Pseudocode

// get combinations from numbers
// for each combination, add two and push to set

// when it's all done, convert to array and return answer

function solution(numbers) {
    let N = numbers.length;
    let numbersSet = new Set();

    for (let i = 0; i < N; i++) {
        for (let j = (i+1) ; j < N; j++) {
            // get combinations from numbers
            let number_1 = numbers[i];
            let number_2 = numbers[j];
            // for each combination, add two and push to set
            numbersSet.add(number_1 + number_2);
        }

    }

    // when it's all done, convert to array and return answer
    let answer = Array.from(numbersSet).sort((a,b) => {
        if (a > b) {
            return 1;
        } else if (a == b) {
            return 0;
        } else {
            return - 1;
        }
    });
    return answer;
}

console.log(solution([2,1,3,4,1]));
console.log(solution([5, 0, 2, 7]));