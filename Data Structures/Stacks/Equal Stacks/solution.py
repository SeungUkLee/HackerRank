#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    sum_h1, sum_h2, sum_h3 = sum(h1), sum(h2), sum(h3)
    while any([h1, h2, h3]):
        max_len = max(sum_h1, sum_h2, sum_h3)
        if sum_h1 == sum_h2 and sum_h2 == sum_h3:
            return sum_h1

        if max_len == sum_h1:
            sum_h1 -= h1.pop(0)
        if max_len == sum_h2:
            sum_h2 -= h2.pop(0)
        if max_len == sum_h3:
            sum_h3 -= h3.pop(0)
    return 0

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

