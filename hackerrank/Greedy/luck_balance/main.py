# If Lena loses no more than k important contests, what is the maximum amount of
# luck she can have after competing in all the preliminary contests? This value
# may be negative.


#constraints


def luckBalance(k, contests):
    answer = 0
    important_list = []
    unimportant_list = []

    # order important by luck score
    contests.sort(key= lambda e: e[0])

    must_win_count = len([x[0] for x in contests if x[1] == 1]) - k

    # Separate important from unimportant
    for contest in contests:
        if contest[1] == 0:
            answer += contest[0]
        elif must_win_count > 0:
            answer -= contest[0]
            must_win_count -= 1
        else:
            answer += contest[0]

    return answer

if __name__ == "__main__":
    print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])) #29
    print(luckBalance(4, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])) #31
    print(luckBalance(0, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])) #-1s
    print(luckBalance(0, [[5, 1]])) #-5
    print(luckBalance(1, [[5, 1]])) #5
    print(luckBalance(5, [[5, 1]])) #5