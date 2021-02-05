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
            important_list.push(contest[0])
        else:
            unimportant_list.push(contest[0])

    # order important by luck score
    important_list.sort()

    # Find the maximum luck possible
    answer = sum(important_list) + sum(unimportant_list)

    # evaluate net amount
    can_lose_amt =

    return answer