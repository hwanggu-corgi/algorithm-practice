function solution(n, computers) {
    let network_count = 0;
    let searched = new Set();
    let N_rows = computers.length;

    for (let computer_id = 0; computer_id < N_rows; computer_id++) {
        if (searched.has(computer_id)) {
            continue
        }

        _solution(computer_id, searched, computers);

        network_count += 1;
    }
    return network_count;
}

let _solution = (computer_id, searched, computers) => {
    let N_cols = computers[computer_id].length;

    if (searched.has(computer_id)) {
        return;
    }

    searched.add(computer_id);

    for (let neighbouring_computer_id = 0 ; neighbouring_computer_id < N_cols ; neighbouring_computer_id++) {
        let connected = computers[computer_id][neighbouring_computer_id];

        if (neighbouring_computer_id == computer_id) {
            continue;
        }

        if (searched.has(neighbouring_computer_id)) {
            continue;
        }

        if (connected == 0) {
            continue;
        }

        _solution(neighbouring_computer_id, searched, computers);
    }
}


console.log(solution(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])) //1
console.log(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])) //3
console.log(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) //2
console.log(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) //1