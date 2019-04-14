#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def rec(str_n):
    if len(str_n) <= 1:
        return str_n
    
    p = sum(int(c) for c in str_n)
    return rec(str(p))

def superDigit(n, k):
    # input이 123 3 일때
    # 123123123 -> 1 + 2 + 3 +...+ 3 = 18
    # 123123123 을 전달하지말고
    # 123 -> 1+2+3 = 6 이다
    # 6 * 3 = 18 을 전달하면 된다
    return rec(str(sum(int(c) for c in n) * k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

