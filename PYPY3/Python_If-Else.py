#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
a=n%2
if a==1:
    print("Weird")
if a==0:
    if(n>=2 and n<5):
        print("Not Weird")
    elif(n>20):
        print("Not Weird")
    else:
        print("Weird")

    
