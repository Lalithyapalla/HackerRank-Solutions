#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    lst=s.split(':')
    if lst[-1][2:]=='AM' and int(lst[0])==12:
        lst[0]='00'
        return (':'.join(lst)[:-2])
    elif lst[-1][2:]=='AM':
        return (s[:-2])
    if  lst[-1][2:]=='PM' and lst[0]!='12' :
        lst[0]=str(12+int(lst[0]))
        return  (':'.join(lst)[:-2])
    else:
        return (':'.join(lst)[:-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

