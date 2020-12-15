function solution(participant, completion) {
    let answer = '';
    let count = {};

    let N = completion.length;

    participant = participant.sort();
    completion = completion.sort();

    for (let i = 0; i < N; i++) {
        if (participant[i] != completion[i]) {
            console.log(participant[i]);
            answer = participant[i];
            break;
        }
    }

    if (participant.length > completion.length) {
        answer = participant[N];
    }

    return answer;
}

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"])); // leo
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])); // leo