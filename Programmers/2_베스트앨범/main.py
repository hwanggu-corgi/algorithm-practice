# goal: 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가
# 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

# 제한사항
#   - genres[i]는 고유번호가 i인 노래의 장르입니다.
#   - plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
#   - genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
#   - 장르 종류는 100개 미만입니다.
#   - 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
#   - 모든 장르는 재생된 횟수가 다릅니다.


def solution(genres, plays):
    answer = []
    return answer