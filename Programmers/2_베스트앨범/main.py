# goal: 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가
# 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

# 제한사항
#   - genres[i]는 고유번호가 i인 노래의 장르입니다.
#   - plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
#   - genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
#   - 장르 종류는 100개 미만입니다.
#   - 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
#   - 모든 장르는 재생된 횟수가 다릅니다.

# Example
#   1)  [classic, pop, classic, classic, pop] [500, 600, 150, 800, 2500]
#       - 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
#           BEFORE [(0, classic, 500), (1, pop, 600), (2, classic, 150), (3, classic, 800), (4, pop, 2500)]
#           AFTER  [(1, pop, 600), (4, pop, 2500), (2, classic, 150), (3, classic, 800), (0,classic, 500)]

#       - 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
#           BEFORE [(1, pop, 600), (4, pop, 2500), (2, classic, 150), (3, classic, 800), (0,classic, 500)]
#           AFTER  [(4, pop, 2500), (1, pop, 600), (3, classic, 800), (0, classic, 500), (2,classic, 150)]

#       - 2 per genre
#           BEFORE [(4, pop, 2500), (1, pop, 600), (3, classic, 800), (0, classic, 500), (2,classic, 150)]
#           AFTER  [(4, pop, 2500), (1, pop, 600), (3, classic, 800), (0, classic, 500)]


# peseudocode
#   - zip them together (range, genre, plays)
#   - put item in dictionary by genre {pop: [(1, pop, 600),  (4, pop, 2500)], classic:[(0, classic, 500), (2, classic, 150), (3, classic, 800)]}
#   - count total plays by genre {pop: 3100, classic: 1450}
#   - count items in each genre by times played (stable) {pop: [(4, pop, 2500),  (1, pop, 600)], classic:[(3, classic, 800), (0, classic, 5000), (2, classic, 150)]}
#   - sort genres by total frequency [pop, classic]
#   - add music (2 per genre) [(4, pop, 2500), (1, pop, 600), (3, classic, 800), (0, classic, 500)]
#   - return result

def solution(genres, plays):
    answer = []
    dictionary = {}
    plays_by_genre = {}
    N = len(genres)
    # zip them together (range, genre, plays)
    zipped_list = list(zip(range(N), genres, plays))

    # print [(0, 'classic', 800), (1, 'pop', 500)]
    # print(zipped_list)

    # put item in dictionary by genre {pop: [(1, pop, 600),  (4, pop, 2500)], classic:[(0, classic, 500), (2, classic, 150), (3, classic, 800)]}
    for item in zipped_list:
        genre = item[1]
        if genre not in dictionary:
            dictionary[genre] = []
            dictionary[genre].append(item)
        else:
            dictionary[genre].append(item)

    # print {'classic': [(0, 'classic', 800)], 'pop': [(1, 'pop', 500)]}
    # print(dictionary)

    # count total plays by genre {pop: 3100, classic: 1450}
    # convert to list of tuples [(pop, 3100), (classic, 1450)]
    # sort genres by total frequency [pop, classic]
    plays_by_genre = count_plays_by_genre(zipped_list)

    # print {'classic': 800, 'pop': 500}
    # print(plays_by_genre)

    plays_by_genre = sorted(zip(plays_by_genre.keys(), plays_by_genre.values()), key= lambda e: e[1], reverse=True)

    # print [('classic', 800), ('pop', 500)]
    # print(plays_by_genre)

    # sort items in each genre by times played (stable) {pop: [(4, pop, 2500),  (1, pop, 600)], classic:[(3, classic, 800), (0, classic, 5000), (2, classic, 150)]}
    for genre in dictionary:
        dictionary[genre] = sorted(dictionary[genre], key=lambda e: e[2], reverse=True)

    # print [('classic', 800), ('pop', 500)]
    # print(dictionary)

    # add music (2 per genre) [(4, pop, 2500), (1, pop, 600), (3, classic, 800), (0, classic, 500)]
    for genre, _ in plays_by_genre:
        i = 0
        N_genre = len(dictionary[genre])
        while i < min(N_genre ,2):
            answer.append(dictionary[genre][i][0])
            i += 1
    # return result
    return answer

def count_plays_by_genre(zipped_list):
    plays_by_genre = {}
    for item in zipped_list:
        genre = item[1]
        plays = item[2]
        if genre not in plays_by_genre:
            plays_by_genre[genre] = plays
        else:
            plays_by_genre[genre] += plays
    return plays_by_genre

if __name__ == "__main__":
    print(solution([], [])) #[]
    print(solution(["classic"], [800])) #[0]
    print(solution(["classic", "pop"], [800, 500])) #[0, 1]
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 800, 800, 2500])) #[4, 1, 2, 3]
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) #[4, 1, 3, 0]