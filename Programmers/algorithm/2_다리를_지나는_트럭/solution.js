// goal: solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight,
// 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
// return 하도록 solution 함수를 완성하세요.

// 제한 조건
//   - bridge_length는 1 이상 10,000 이하입니다.
//   - weight는 1 이상 10,000 이하입니다.
//   - truck_weights의 길이는 1 이상 10,000 이하입니다.
//   - 모든 트럭의 무게는 1 이상 weight 이하입니다.

// Exmaple
//  1) bridge_length: 2, weight: 10, truck_weights: [7,4,5,6]
//  start of i = 0        [0,0]     [7,4,5,6]
//  start of i = 1        [0,7]     [4,5,6]     <-- weight limit reached, wait
//  start of i = 2        [7,0]     [4,5,6]
//  start of i = 3        [0,4]     [5,6]
//  start of i = 4        [4,5]     [6]
//  start of i = 5        [5,0]     [6]
//  start of i = 6        [0,6]     []
//  start of i = 7        [6,0]     []
//  start of i = 8        []        []

// Pseudocode
//      start from i = 0
//      while length of truck_weights is greater than 0,
//      shift bridge
//      append 0 to bridge
//      if truck weight is less than bridge weight, push to bridge
//      else
//

function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    return answer;
}