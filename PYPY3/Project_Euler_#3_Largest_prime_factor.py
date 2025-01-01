#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        d=list(filter(lambda fa:n%fa==0 and len(list(filter(lambda f:fa%f==0 ,range(1,fa+1))))==2,range(1,n+1)))
        print(d[-1])
