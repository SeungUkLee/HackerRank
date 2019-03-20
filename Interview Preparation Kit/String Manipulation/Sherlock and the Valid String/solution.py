#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def str_to_dict(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def isValid(s):
    d = str_to_dict(s)
    cmp_v, flag = d[s[0]], False
    print(d)

    for _, v in d.items():
        if cmp_v != v and flag:
            return "NO"
        elif cmp_v != v and not flag:
            flag = True
            
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

