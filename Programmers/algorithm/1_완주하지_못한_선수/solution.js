function solution(participant, completion) {
    let answer = '';
    let count = {};

    let N_completion = completion.length;
    let N_participant = participant.length;

    for (let i = 0; i < N_participant; i++) {
        if (!(participant[i] in count)) {
            count[participant[i]] = 1;
        } else {
            count[participant[i]] += 1;
        }
    }

    console.log(count);

    for (let i = 0; i < N_completion; i++) {
        count[completion[i]] -= 1;
    }

    console.log(count);

    for (let i = 0; i < N_participant; i++) {
        if (count[participant[i]] != 0 ) {
            answer = completion[i];
            break;
        }
    }

    return answer;
}

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"])); // leo
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])); // leo