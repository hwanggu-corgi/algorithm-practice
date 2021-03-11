function solution(n, lost, reserve) {
    var answer = 0;

    // create set lost and reserve with value not in both sets
    let lost_set = new Set(lost);
    let reserve_set = new Set(reserve);

    lost_set = new Set([...lost].filter(x => reserve_set.has(x)));
    lost_set = new Set([...lost].filter(x => reserve_set.has(x)));

    // assign reserve to lost
    // if match, then take out value from lost and reserve

    // find total number of participants
    // n - number of lost

    return answer;
}