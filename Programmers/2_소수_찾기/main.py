# goal: 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는
# 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - numbers는 길이 1 이상 7 이하인 문자열입니다.
#   - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
#   - 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

def solution(numbers):
    answer = 0
    N = len(numbers)
    combinations = set()

    # split numbers to array of digits

    # use DFS to find all combination of words
    get_combinations("", numbers, combinations, N)

    print(combinations)

    # calculate length of combination of words
    return len(combinations)

def get_combinations(combined_number, numbers, combinations, target_length):

    # if combined word length matches target, add to set and return
    if len(combined_number) == target_length:
        return

    # if not, continue to add combinations
    # for each character in numbers
    N = len(numbers)
    i = 0
    while i < N:
        # pop it
        number = numbers[i]
        # add to combination
        new_combined_number = str(int(combined_number + number))

        # check prime number
        combinations.add(new_combined_number)

        # get reminaing numbers after pop
        new_numbers = numbers[:i] + numbers[i+1:]
        _solution(new_combined_number, new_numbers, combinations, target_length)

        i += 1

def is_prime_number(number):
    number = int(number)

    if number == 1 or number == 0:
        return False



if __name__ == "__main__":
    print(solution("17")) #3
    print(solution("011")) #2
    print(solution("")) #0