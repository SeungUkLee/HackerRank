#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_d = str_to_dict(s1)
    
    for c in s2:
        if c in s1_d:
            return "YES"
    return "NO"
        
def str_to_dict(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
            continue
        d[c] = 1
    return d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()


