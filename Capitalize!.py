#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    temp = []
    for i in range(0,len(s)):
        if i > 0 and s[i - 1] == ' ' and s[i].isalpha():
            temp.append(s[i].upper())
        else:
            temp.append(s[i])
    if temp[0].isalpha():
        temp[0] = temp[0].upper()
    res =''
    for i in temp:
        res += i
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
