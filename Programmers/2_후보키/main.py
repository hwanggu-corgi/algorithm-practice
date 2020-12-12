# goal: 릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의
# 개수를 return 하도록 solution 함수를 완성하라.

# 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
# 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

# 제한사항
#   - relation은 2차원 문자열 배열이다.
#   - relation의 컬럼(column)의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
#   - relation의 로우(row)의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
#   - relation의 모든 문자열의 길이는 1 이상 8 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
#   - relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)

# Example
#   1)
#   [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
#   it's 2.
#   - [이름, 전공] as relation key

# Pesudocode
#   - create combination of column indexes (start from combination of 1 element)
#   - extract columns and zip them together
#   - put all in set and check if length of set is equal to length of array
#   - if so, return number of columns

from itertools import combinations

def solution(relation):
    # get number of columns
    N_cols = len(relation[0])
    N_rows = len(relation)
    columns_list = []
    answer = 1

    # create list of values by column
    for col_index in range(N_cols):
        column = get_column(relation, col_index, N_rows)
        columns_list.append(column)

    for number_of_cols in range(1,N_cols+1):
        # create combination of column indexes (start from combination of 1 element)
        combs = combinations(range(1,N_cols),number_of_cols)

        for combination in combs:
            key_relation = [columns_list[x] for x in combination]
            # extract columns and zip them together

            # put all in set and check if length of set is equal to length of array
            if len(set(zip(*key_relation))) == N_rows:
                # if so, return number of columns
                answer += 1
                has_key_relation = True
        if has_key_relation:
            break
    return answer

def get_column(relation, col_index, N_rows):
    return [relation[i][col_index] for i in range(N_rows)]

if __name__ == "__main__":
    test_a = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(test_a)) #2