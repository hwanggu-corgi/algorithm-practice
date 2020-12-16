// pseudocode

// sort list in order
// for each large element add small elements until full (no small element exists or small element + large weight >= limit)
// when full, add count
// repeat until empty

function solution(people, limit) {
    var answer = 0;
    let N = people.length;
    let i_left = 0;
    let i_right = N-1;

    // sort list in order
    people = people.sort();

    while (i_left < i_right) {
        // for each large element add small elements until full (no small element exists or small element + large weight >= limit)
        // when full, add count
        // repeat until empty
    }

    return answer;
}