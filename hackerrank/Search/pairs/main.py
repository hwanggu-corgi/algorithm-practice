# goal: Given an array of integers and a target value, determine the number of
# pairs of array elements that have a difference equal to the target value.

from collections import Counter

def pairs(k, arr):
    count = 0
    # count numbers in arr
    e_count = Counter(arr)

    # for each arr in arr, check if arr[i] - k exists
    for e in arr:
        # if it exists, increment cound, and decrement e_count[arr[i] - k]
        if e_count.get(e - k, 0) > 0:
            count += 1
            e_count[e - k] -= 1
        # if it doesn't exist, then continue


    # return count
    return count

if __name__ == "__main__":
    print(pairs(2, [1, 5, 3, 4, 2])) #3