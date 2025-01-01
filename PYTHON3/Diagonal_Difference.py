#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    lr_sum=rl_sum=0
    for ind in range(len(arr)):
        lr_sum+=arr[ind][ind]
        rl_sum+=arr[ind][len(arr)-ind-1]
    if lr_sum-rl_sum<0:
        return rl_sum-lr_sum
    else:
        return lr_sum-rl_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
