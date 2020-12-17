function solution(clothes) {
    var answer = 0;
    let count = {};

    for (clothe of clothes) {
        clothe_type = clothe[1];

        if (!count.has(clothe_type)) {
            count[clothe_type] += 1;
        } else {
            count[clothe_type] = 2; // + 1 from wearing none of the type
        }
    }

    answer = count.values().reduce((acc, val) => {acc *= val;}, 1) - 1; // -1 to remove all nones

    return answer;
}