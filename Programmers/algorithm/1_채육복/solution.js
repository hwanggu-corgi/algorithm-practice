// Pseudocode

// sort lost and reserve
// turn lost and reserve to sets
// find available sets
    // remove number in both reserve and lost
// convert lost back to list
// lend reserve to peers
// for each lost
    // if the different between lost and reserve is 1 apart, lend gym shirt
    // if lent, add count
    // if lent, remove number from reserve
// return total number of participants in gym class
    // n - (lost.length - lentCount)

function solution(n, lost, reserve) {
    var answer = 0;
    // turn lost and reserve to sets
    lostSet = new Set(lost)
    reserveSet = new Set(reserve)
    // find available sets
    // remove number in both reserve and
    lostSet = lostSet - reserveSet;
    lostSet = lostSet - reserveSet;

    // convert lost back to list
    // sort lost
    // lend reserve to peers
    // for each lost
        // if the different between lost and reserve is 1 apart, lend gym shirt
        // if lent, add count
        // if lent, remove number from reserve
    // return total number of participants in gym class
        // n - (lost.length - lentCount)
    return answer;
}

function compare(a,b) {
    if (a > b) {
        return 1;
    } else if (a == b) {
        return 0;
    } else {
        return - 1;
    }
}