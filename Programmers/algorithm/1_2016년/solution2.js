function solution(a, b) {
    let answer = '';
    const day_of_week_ref = {0:"SUN", 1: "MON", 2: "TUE", 3:"WED", 4:"THU", 5:"FRI", 6:"SAT"};

    // convert input to date format
    const date = new Date(`2016-${a}-${b}`);

    // get day of week
    answer = day_of_week_ref[date.getDay()];

    // print
    return answer;
}


console.log(solution(5,24));