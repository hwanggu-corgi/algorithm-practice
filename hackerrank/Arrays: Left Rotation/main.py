import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    n = len(a)
    a_new = [0] * n

    for i in range(n):
        a_new[i - d] = a[i]

    return a_new


if __name__ == "__main__":
    print(rotLeft([1,2,3,4,5], 4)) #[5,1,2,3,4]