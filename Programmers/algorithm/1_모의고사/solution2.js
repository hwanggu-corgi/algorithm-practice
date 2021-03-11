function solution(answers) {
    var answer = [];
    let student_1 = [1,2,3,4,5];
    let student_2 = [2, 1, 2, 3, 2, 4, 2, 5];
    let student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    let scores = [0,0,0];

    // find number of correct answers for each student
    for (let i = 0; i < answers.length; i++) {

        // if correct, then raise score
        if (answers[i] === student_1[i % student_1.length]) {
            scores[0] += 1;
        }

        if (answers[i] === student_2[i % student_2.length]) {
            scores[1] += 1;
        }

        if (answers[i] === student_3[i % student_3.length]) {
            scores[2] += 1;
        }
    }

    // write who has the biggest score of all
    const max_score = Math.max(...scores);

    for(let i = 0; i < scores.length; i++) {
        if (scores[i] === max_score) {
            answer.push(i+1)
        }
    }

    return answer;
}


console.log(solution([1,2,3,4,5])) // [1]
console.log(solution([1,3,2,4,2])) // [1,2,3]