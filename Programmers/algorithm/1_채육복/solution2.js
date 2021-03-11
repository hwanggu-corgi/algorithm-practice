function solution(n, lost, reserve) {
    var answer = 0;

    // create set lost and reserve with value not in both sets
    let lost_set_tmp = new Set(lost);
    let reserve_set_tmp = new Set(reserve);

    let lost_set = new Set(lost.filter(x => !reserve_set_tmp.has(x)));
    let reserve_set = new Set(reserve.filter(x => !lost_set_tmp.has(x)));

    // assign reserve to lost
    // if match, then take out value from lost and reserve
    for (let item of reserve_set) {
        if (lost_set.has(item-1)) {
            lost_set.delete(item-1);
        } else if (lost_set.has(item+1)) {
            lost_set.delete(item+1);
        }
    }

    // find total number of participants
    // n - number of lost

    return answer;
}