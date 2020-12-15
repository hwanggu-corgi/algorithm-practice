function solution(answers) {
    var answer = [];
    let N = answers.length;
    let pattern_1 = [1, 2, 3, 4, 5];
    let N_pattern_1 = pattern_1.length;
    let pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5];
    let N_pattern_2 = pattern_2.length;
    let pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    let N_pattern_3 = pattern_3.length;

    let correct_count = {1: 0, 2: 0, 3: 0};

    for (let i = 0; i < N; i++) {
        correct_count[1] += 1 ? pattern_1[i % N_pattern_1] : 0;
        correct_count[2] += 1 ? pattern_2[i % N_pattern_2] : 0;
        correct_count[3] += 1 ? pattern_3[i % N_pattern_3] : 0;
    }
    return answer;
}