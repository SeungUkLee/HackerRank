#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack, opened_brackets = [], ('(', '[', '{')
    brackets = {
        ']': '[',
        ')': '(',
        '}': '{',
    }

    for bracket in s:
        if bracket in opened_brackets:
            stack.append(bracket)
            continue
        if not stack or brackets[bracket] != stack[-1]:
            return "NO"
        stack.pop()
    return "YES" if not stack else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()


