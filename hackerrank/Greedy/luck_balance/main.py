# If Lena loses no more than k important contests, what is the maximum amount of
# luck she can have after competing in all the preliminary contests? This value
# may be negative.


#constraints


def luckBalance(k, contests):
    answer = 0
    important_list = []
    unimportant_list = []

    # Separate important from unimportant
    for contest in contests:
        if contest[1] == 1:
            important_list.append(contest[0])
        else:
            unimportant_list.append(contest[0])

    # order important by luck score
    important_list.sort()

    # evaluate net amount
    must_win_amt = len(important_list) - k
    answer = sum(important_list[must_win_amt:]) - sum(important_list[:must_win_amt]) + sum(unimportant_list)

    return answer

if __name__ == "__main__":
    print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])) #29
    print(luckBalance(4, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])) #31
    print(luckBalance(0, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])) #-1s
    print(luckBalance(0, [[5, 1]])) #-5
    print(luckBalance(1, [[5, 1]])) #-5