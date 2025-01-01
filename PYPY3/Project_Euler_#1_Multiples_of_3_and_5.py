#!/bin/python3

import math
import os
import random
import re
import sys

def sum_of_multiples(n, multiple):
    p = (n - 1) // multiple
    return multiple * (p * (p + 1)) // 2

def multiple_3_5(num):
    return sum_of_multiples(num, 3) + sum_of_multiples(num, 5) - sum_of_multiples(num, 15)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(multiple_3_5(n))

