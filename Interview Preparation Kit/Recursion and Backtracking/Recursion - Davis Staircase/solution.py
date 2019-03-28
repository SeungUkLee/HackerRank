#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.

def gen_step(n):
    dp = [0, 1, 2, 4]
    
    for _ in range(4, n):
        dp_3, dp_2, dp_1 = dp[3], dp[2], dp[1]
        dp[3], dp[2], dp[1] = dp_3 + dp_2 + dp_1, dp_3, dp_2
        yield dp_3 + dp_2 + dp_1

def stepPerms(n):
    # P(n) - P(n - 1) + P(n - 2) + P(n - 3)
    dp = [0, 1, 2, 4]
    if n <= 3:
        return dp[n]
    
    step = None
    for step in gen_step(n + 1):
        pass

    return step


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()


