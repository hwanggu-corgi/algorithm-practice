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
//     [[0,2],[1,1], [2,3], [3,2]]
//     [0,2] [[1,1],[2,3], [3,2]] popleft --> check if priority matches target --> no --> append
//     [0,2] [[1,1],[2,3], [3,2]] popleft --> check if priority matches target --> no --> append
//
//      return 1

function solution(priorities, location) {
    var answer = 0;
    return answer;
}