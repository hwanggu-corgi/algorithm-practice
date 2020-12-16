function solution(n) {
    // set n as string
    n = n.toString();

    // split string into array arr
    let n_array = n.split();

    // reverse array
    n_array = n_array.sort((a,b) => {
        if (a > b) {
            return -1;
        } else if (a == b){
            return 0;
        } else {
            return 1;
        }
    });

    // recombine and convert to integer
    n = int(n_array.join(""));

    // return
    let answer = n;
    return answer;
}