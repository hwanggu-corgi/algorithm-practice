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
    let lentCount = 0;
    let N_lost = lost.length;
    // turn lost and reserve to sets
    let lostSet = new Set(lost);
    let reserveSet = new Set(reserve);

    // find available sets
    // remove number in both reserve and lost
    lost = lost.filter(x => !(x in reserveSet));
    reserve = reserve.filter(x => !(x in lostSet));
    reserveSet = new Set(reserve);

    // sort lost
    lost = lost.sort(compare);
    // lend reserve to peers
    // for each lost
    console.log(lost);
    for (i in lost) {
        // if the different between lost and reserve is 1 apart, lend gym shirt
        if ((i-1) in reserveSet) {
            // if lent, add count
            lentCount += 1;

            // if lent, remove number from reserve
            reserveSet.remove(i-1);
        }
    }

    // return total number of participants in gym class
    answer = n - (lost.length - lentCount);
    return answer;
}

function compare(a,b) {
    if (a > b) {
        return -1;
    } else if (a == b) {
        return 0;
    } else {
        return 1;
    }
}

console.log(solution(5, [2,4], [1,3,5])); // 5