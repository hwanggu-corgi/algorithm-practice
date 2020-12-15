function solution(participant, completion) {
    let answer = '';

    let N = completion.length;

    participant = participant.sort();
    completion = completion.sort();
    console.log(participant);
    console.log(completion);

    for (let i = 0; i < N; i++) {
        if (participant[i] != completion[i]) {
            console.log(participant[i]);
            answer = participant[i];
            break;
        }
    }
    return answer;
}

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"])); // leo