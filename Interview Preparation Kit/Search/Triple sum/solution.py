#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.

from bisect import bisect

def triplets(a, b, c):
    sorted_a, sorted_c = sorted(set(a)), sorted(set(c))
    return sum(bisect(sorted_a, v) * bisect(sorted_c, v) for v in set(b))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
