#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n,fact=1):
    if n==0:
        return 1
    return fact*factorial((n-1),fact+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
