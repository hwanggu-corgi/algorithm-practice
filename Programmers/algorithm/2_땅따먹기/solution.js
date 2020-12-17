//goal: 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를
//완성해 주세요.

//- 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다

//제한사항
//행의 개수 N : 100,000 이하의 자연수
//열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.
//점수 : 100 이하의 자연수

// Example
// | 1 | 2 | 3 | 5 |

// | 5 | 6 | 7 | 8 |  --> add 5 to 2, 3 and 5 --> add 6 to 1 3 5 --> add 7 to 1 2 and 5 --> add 8 to 1 2 and 3

// | 4 | 3 | 2 | 1 |


// | 1 | 2 | 3 | 5 |

// | 5 | 6 | 7 | 8 |  --> add 5 to max of 2, 3 and 5 (5) --> add 6 to max of 1 3 5 (5) --> add 7 to max of 1 2 and 5 (5) --> add 8 to max of 1 2 and 3 (3)

// | 4 | 3 | 2 | 1 |


// | 1 | 2 | 3 | 5 |

// | 10 | 11 | 12 | 11 |

// | 4 | 3 | 2 | 1 |


// | 1 | 2 | 3 | 5 |

// | 10 | 11 | 12 | 11 |

// | 4 | 3 | 2 | 1 | --> add 4 to max of 11, 12 and 11 (12) --> add 3 to max of 10 12 11 (12) --> add 2 to mas of 10 11 11 (11) --> add 1 to max of 10 11 12 (12)


// | 1 | 2 | 3 | 5 |

// | 10 | 11 | 12 | 11 |

// | 16 | 15 | 13 | 13 | --> add 4 to max of 11, 12 and 11 (12) --> add 3 to max of 10 12 11 (12) --> add 2 to mas of 10 11 11 (11) --> add 1 to max of 10 11 12 (12)


// pseudocode code
// copy land call it dp
// while i start from 1 until n
// add dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
// add dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
// add dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
// add dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])


// return the max of the last row

function solution(land) {
    // copy land call it dp
    let dp = copy_array(land);
    let i = 1;
    let n = land.length;
    // while i start from 1 until n
    while (i < n) {
        // add dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        // add dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        // add dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
        // add dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

        dp[i][0] += Math.max(dp[i-1][1], dp[i-1][2], dp[i-1][3]);
        dp[i][1] += Math.max(dp[i-1][0], dp[i-1][2], dp[i-1][3]);
        dp[i][2] += Math.max(dp[i-1][0], dp[i-1][1], dp[i-1][3]);
        dp[i][3] += Math.max(dp[i-1][0], dp[i-1][1], dp[i-1][2]);
        i += 1
    }

    // return the max of the last row
    let answer = Math.max(...dp[n-1]);
    return answer;
}

let copy_array = (array) => {
    let res = [];
    for (let row of array) {
        let row_copy = [...row];
        res.push(row_copy);
    }
    return res;
}

console.log(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])); // 16