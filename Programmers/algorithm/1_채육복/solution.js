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

    // turn lost and reserve to sets
    let lostSet = new Set(lost);
    let reserveSet = new Set(reserve);

    // find available sets
    // remove number in both reserve and lost
    lost = lost.filter(x => !(reserveSet.has(x)));
    reserve = reserve.filter(x => !(lostSet.has(x)));
    reserveSet = new Set(reserve);

    // sort lost
    lost = lost.sort(compare);
    // lend reserve to peers
    // for each lost
    for (let i of lost) {
        // if the different between lost and reserve is 1 apart, lend gym shirt
        if (reserveSet.has(i-1)) {
            // if lent, add count
            lentCount += 1;

            // if lent, remove number from reserve
            reserveSet.delete(i-1);
            continue;
        }

        if (reserveSet.has(i+1)) {
            // if lent, add count
            lentCount += 1;

            // if lent, remove number from reserve
            reserveSet.delete(i+1);
            continue;
        }
    }

    // return total number of participants in gym class
    let answer = n - (lost.length - lentCount);
    return answer;
}

function compare(a,b) {
    if (a > b) {
        return 1;
    } else if (a == b) {
        return 0;
    } else {
        return -1;
    }
}
console.log(solution(3, [1], [4])); // 2
console.log(solution(5, [1,2], [1])); // 4
console.log(solution(5, [1,2], [1,2])); // 5
console.log(solution(5, [2,4], [1,3,5])); // 5