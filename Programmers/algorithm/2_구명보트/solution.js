// pseudocode

// sort list in order
// for each large element add small elements until full (no small element exists or small element + large weight >= limit)
// when full, add count
// repeat until empty

function solution(people, limit) {
    var answer = 0;

    // sort list in order
    people = people.sort(compare);
    while (people.length > 0) {
        let current_weight = people.pop();

        // for each large element add small elements until full (no small element exists or small element + large weight >= limit)
        while (true) {
            if (people.length == 0) {
                break;
            }

            if (current_weight + people[0] >  limit) {
                break;
            }

            // repeat until empty
            let small_weight = people.shift();
            current_weight += small_weight;

        }
        answer += 1;
    }

    return answer;
}


let compare = (a,b) => {
    return a - b;
}

console.log(solution([70, 50, 80, 50], 100)); //3
console.log(solution([70, 80, 50], 100)); //3