# goal: 어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정
# 프로그램을 작성하시오.

# 입력 형식
#   - 캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
#   - cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
#   - cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
#   - 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

# Example
#   1) [Jeju, Pangyo, Seoul, NewYork, LA, Jeju, Pangyo, Seoul, NewYork, LA]
#       - Jeju --> cache miss [Jeju] {Jeju} 5
#       - Pangyo --> cache miss [Jeju]-[Pangyo] {Jeju, Pangyo}10
#       - Seoul --> cache miss [Jeju]-[Pangyo]-[Seoul] {Jeju, Pangyo, Seoul} 15
#       - NewYork --> cachemiss [Pangyo]-[Seoul]-[NewYork] {Pangyo, Seoul, NewYork} 20
#       - LA --> cachemiss [Seoul]-[NewYork]-[LA] {Seoul, NewYork, LA} 25
#       - Jeju --> cachemiss [NewYork]-[LA]-[Jeju] {NewYork, LA, Jeju} 30
#       - Pangyo --> cachemiss [LA]-[Jeju]-[Pangyo] {LA, Jeju, Pangyo} 35
#       - Seoul --> cachemiss [Jeju]-[Pangyo]-[Seoul] {Jeju, Pangyo, Seoul} 40
#       - NewYork --> cachemiss [Pangyo]-[Seoul]-[NewYork] {Pangyo, Seoul, NewYork} 45
#       - LA --> cachemiss [Seoul]-[NewYork]-[LA] {Seoul, NewYork, LA} 50

# Pseudocode
# create a queue called cache_queue
# create a set called cache_set
# for each city in cities
# if city not in cache_set (cache miss),
#   if len(cache_queue) == cacheSize, popleft cache_queue and remove popped item from cache_set
#   append to cache_queue and add to cache_set

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    # create a queue called cache_queue
    cache_queue = deque()
    # create a set called cache_set
    cache_set = set()

    # for each city in cities
    for city in cities:
        city = city.lower()
        # if city in cache_set (cache hit),
        if city in cache_set:
            # add answer by 1 and continue
            answer += 1
            continue

        # else (cache miss)
        # if len(cache_queue) == cacheSize, popleft cache_queue and remove popped item from cache_set
        answer += 5

        if cacheSize == 0:
            continue

        if len(cache_queue) == cacheSize:
            popped_city = cache_queue.popleft()
            cache_set.remove(popped_city)
        # append to cache_queue and add to cache_set
        cache_queue.append(city)
        cache_set.add(city)
    return answer

if __name__ == "__main__":
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) #50
    print(solution(3, 	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) #21
    print(solution(2, 	["Jeju", "Pangyo", "NewYork", "newyork"])) #16