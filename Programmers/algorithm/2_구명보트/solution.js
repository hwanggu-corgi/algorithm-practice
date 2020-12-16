// pseudocode

// sort list in order
// for each large element add small elements until full (no small element exists or small element + large weight >= limit)
// when full, add count
// repeat until empty

function solution(people, limit) {
    var answer = 0;
    let N = people.length;

    // sort list in order
    people = people.sort(compare);
    while (i_left <= i_right) {
        let current_weight = people[i_right];

        // for each large element add small elements until full (no small element exists or small element + large weight >= limit)
        while ((current_weight + people[i_left] < limit) && (i_left < i_right)) {
            // when full, add count
            current_weight += people[i_left];
            console.log(current_weight);
            // repeat until empty
            i_left += 1;
        }
        answer += 1;
        i_right -= 1;
    }

    return answer;
}

let compare = (a,b) => {
    return a - b;
}

console.log(solution([70, 50, 80, 50], 100)); //3
console.log(solution([70, 80, 50], 100)); //3