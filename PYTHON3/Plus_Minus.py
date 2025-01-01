#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n_c=len(list(filter(lambda num:num<0,arr)))/len(arr)
    p_c=len(list(filter(lambda num:num>0,arr)))/len(arr)
    z_c=len(list(filter(lambda num:num==0,arr)))/len(arr)
    return (str(p_c),str(n_c),str(z_c))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print('\n'.join(plusMinus(arr)) ) 
