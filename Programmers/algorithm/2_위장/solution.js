function solution(clothes) {
    var answer = 0;
    let count = {};

    for (let clothe of clothes) {
        let clothe_type = clothe[1];

        if (clothe_type in count) {
            count[clothe_type] += 1;
        } else {
            count[clothe_type] = 2; // + 1 from wearing none of the type
        }
    }

    answer = Object.values(count).reduce((acc, val) => acc *= val, 1) - 1; // -1 to remove all nones

    return answer;
}

console.log(solution(	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])); // 5