# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Goal: given integer K, tie the ropes in such a way that the number of ropes whose
# length is greater than or equal to K is maximal.


def solution(K, A):
    # write your code in Python 3.6
    count = length_ending = 0

    # for each rope, take sum
    for length in A:
        # add length to sum
        length_ending += length

        # Greedy choice: if sum is over K, then reset sum and increment number of ropes length is greater than or equal to K
        if length_ending >= K:
            count += 1
            length_ending = 0

    return count
