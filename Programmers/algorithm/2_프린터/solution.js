// goal: 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가
// 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가
// 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

// 제한사항
//   - 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
//   - 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
//   - location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.


// Example
//  1) [2, 1, 3, 2] location 2
//     get priority of target location 2 --> 3
//     find max priority --> 3
//     [[0,2],[1,1],[2,3], [3,2]]
//     [0,2] [[1,1],[2,3], [3,2]] popleft --> check if priority matches first priority --> no --> append
//     [1,1] [[2,3],[3,2], [0,2]] popleft --> check if priority matches first priority --> no --> append
//     [2,3] [[3,2],[0,2], [1,1]] popleft --> check if priority matches first priority--> yes --> add count --> check if priority matches target --> yes --> return count
//      return 1

// Pseudocode
//  while priorities not equal to 0
//  popleft an element
//  check if priority matches first priority
//      if no, push item
//      if yes, add count
//      check if location is the target location
//      if yes, return count

function solution(priorities, location) {
    var answer = 0;
    let count = 0;

    priorities = Array.from(priorities.entries());
    let highest_priority = get_highest_priority(priorities);

    // while priorities not equal to 0
    while (priorities.length > 0) {
        // popleft an element
        let item = priorities.shift();
        let item_priority = item[1];
        let item_location = item[0];
        // check if priority matches first priority
        // if no, push item
        if (item_priority != highest_priority) {
            priorities.push(item);
            continue
        }

        // if yes, add count
        count += 1;

        // check if location is the target location
        // if yes, return count
        if (item_location == location) {
            return count;
        }

        highest_priority = get_highest_priority(priorities);
    }
    return answer;
}

let get_highest_priority = (priorities) => {
    let maximum = -1;
    for (let item of priorities) {
        let item_priority = item[1];
        maximum = Math.max(item_priority, maximum);
    }

    return maximum;
}

console.log(solution([2, 1, 3, 2], 2)); // 1
console.log(solution([1, 1, 9, 1, 1, 1], 0)); // 5