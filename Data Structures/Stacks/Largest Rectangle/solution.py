#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    max_area = 1
    for i in range(0, len(h)):
        left_cnt = 0
        right_cnt = 0

        if h[i] == 1:
            max_area = max(max_area, 1 * len(h))
            continue

        for left in range(i - 1, -1, -1):
            if h[left] < h[i]:
                break
            left_cnt += 1

        for right in range(i + 1, len(h)):
            if h[right] < h[i]:
                break
            right_cnt += 1

        max_area = max(max_area, h[i] * (left_cnt + right_cnt + 1))
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

