//goal: 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,
// 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return
// 하는 solution 함수를 완성해 주세요

// - 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다

// 제한사항
// N : 21 이상 220 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)
// A, B : N 이하인 자연수 (단, A ≠ B 입니다.)

// Cases
//  -

// Example
//  1 - 2 3 - 4 5 - 6 7 - 8 9 - 10 11- 12 13 - 14 15 - 16
//    1     2     3     4     5       6      7       8
//       1           2            3

// while True
//  when odd --> Math.ceil(number / 2)
//  when even--> number / 2
//  add count
//  check if number_left == number_right
//  if so , return count

function solution(n,a,b)
{
    let count = 0;

    // while True
    while (true) {
        //  when odd --> Math.ceil(number / 2)
        a = a % 2 == 1 ? Math.ceil(a / 2) : a/2;
        //  when even--> number / 2
        b = b % 2 == 1 ? Math.ceil(b / 2) : b/2;
        //  add count
        count += 1
        //  check if number_left == number_right
        if (a == b) {
            break;
        }
    }
    //  if so , return count
    let answer = count;
    return answer;
}


console.log(solution(8,4,7)); // 3