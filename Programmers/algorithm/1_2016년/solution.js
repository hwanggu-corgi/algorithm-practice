// January - 31 days
// February - 28 days in a common year and 29 days in leap years
// March - 31 days
// April - 30 days
// May - 31 days
// June - 30 days
// July - 31 days
// August - 31 days
// September - 30 days
// October - 31 days
// November - 30 days
// December - 31 days

// pseudocode

// find the closest friday to target from january 1st
    // convert month to days (i.e number of days in (5 - 1) months from january) store in daysCount
    // add b to daysCount
// find the distance from the closest friday
    // daysCount % 7
// print day


function solution(a, b) {
    let answer = '';
    let daysCount = 0;
    let days = {0: "FRI", 1: "SAT", 2:"SUN", 3:"MON", 4:"TUES", 5:"WED", 6:"THU"};

    // find the closest friday to target from january 1st
    daysCount += get_days(a-1);

    // find the distance from the closest friday
    offset = daysCount % 7;

    answer = days[offset];
    return answer;
}

let get_days = (months) => {
    let daysCount = 0;
    let daysInMonth = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    };
    if (months == 0) {
        return 0;
    }

    for (let i = 1; i <= months; i++) {
        daysCount += daysInMonth[i];
    }

    return daysCount;
}

console.log(solution(5,24)) // TUE