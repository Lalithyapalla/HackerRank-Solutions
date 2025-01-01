#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    a=arr[1:]
    max=sum(a)
    b=arr[:-1]
    min=sum(b)
    return (str(min),str(max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
   # print(arr)
    print(' '.join(miniMaxSum(arr)))
    #print(miniMaxSum(arr))
