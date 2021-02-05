# Given an array of integers, sort the array in ascending order using the Bubble
# Sort algorithm above. Once sorted, print the following three lines:

# Complete the countSwaps function below.


def countSwaps(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(n-1):
            if (a[j] > a[j + 1]):
                swap(j,j+1, a)
                count += 1

    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


def swap(j_1, j_2, a):
    temp = a[j_1]
    a[j_1], a[j_2] = a[j_2], temp


if __name__ == "__main__":
    countSwaps([6,4,1])
    countSwaps([1,2,3])