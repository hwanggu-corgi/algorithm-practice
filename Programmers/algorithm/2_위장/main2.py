# goal: 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return
#       하도록 solution 함수를 작성해주세요.


# 제한사항
#   clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
#   스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
#   같은 이름을 가진 의상은 존재하지 않습니다.
#   clothes의 모든 원소는 문자열로 이루어져 있습니다.
#   모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
#   스파이는 하루에 최소 한 개의 의상은 입습니다.


# Example
# [[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]
# head-gear : yellow hat, green turban, none
# eye-wear: blue sunglasses, none

# 3 x 2 - 1 (having all none) = 5


def solution(clothes):
    answer = 1
    count = {}

    for clothe in clothes:
        if clothe[1] not in count:
            count[clothe[1]] = 2 #including none
        else:
            count[clothe[1]] += 1

    for clothe_type in count:
        answer *= count[clothe_type]

    answer -= 1

    return answer

if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) #5
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) #3