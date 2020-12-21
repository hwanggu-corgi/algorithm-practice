function solution(n, computers) {
    network_count = 0
    let searched = new Set()
    let N_rows = computers.length

    for (let computer_id = 0; computer_id < N_rows; computer_id++):
        if (searched.has(computer_id)) {
            continue
        }

        _solution(computer_id, searched, computers)

        network_count += 1
    return network_count
}

let _solution = (computer_id, searched, computers) => {
    if (searched.has(computer_id)) {
        return;
    }

    searched.add(computer_id)

    for neighbouring_computer_id in queue:
        # perform recursion on value
        _solution(neighbouring_computer_id, searched, computers)
}