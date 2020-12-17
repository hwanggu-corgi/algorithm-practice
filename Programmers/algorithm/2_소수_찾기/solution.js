// goal: 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는
// 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

// 제한사항
//   - numbers는 길이 1 이상 7 이하인 문자열입니다.
//   - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
//   - 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

// Pseudocode
// find length of numbers, call it n
// for number length from 1 to n,
// use recursion to find combination of digits of length n
// if found, add integer of number to set

function solution(numbers) {
    var answer = 0;
    // find length of numbers, call it n
    let n = numbers.length;
    let prime_set = new Set();

    // for number length from 1 to n,
    // use recursion to find combination of prime numbers of length from 1 to n
    for (let number_length = 1; number_length <= n; number_length++) {
        get_combined_prime_numbers("", numbers, number_length, prime_set);
    }

    answer =prime_set.size;
    return answer;
}

let get_combined_prime_numbers = (number, numbers, n, prime_set) => {
    // if number length == n, check prime
    // if prime, add to prime_set
    if (number.length == n) {
        number = parseInt(number);
        if (!prime_set.has(number) && is_prime(number)) {
            prime_set.add(number)
        }
        return;
    }

    // else continue to add combination of numbers
    for (const [index, e] of Object.entries(numbers)) {
        let new_numbers = numbers.substring(0, index) + numbers.substring(index+1);
        get_combined_prime_numbers(number + e, new_numbers, n, prime_set);
    }
}

let is_prime = (number) => {
    if (number == 1 || number == 0) {
        return false;
    }

    for (let i = 2; i < number; i++) {
        if (number % i == 0) {
            return false
        }
    }

    return true;
}

console.log(solution("17")); // 3
console.log(solution("011")); // 2