#!/bin/python3

import math
import os
import random
import re
import sys

def next_permutation(arr):
    index = len(arr) - 1
    while index > 0 and arr[index - 1] >= arr[index]:
        index -= 1

    if index <= 0:
        return None

    j = len(arr) - 1
    while arr[j] <= arr[index - 1]:
        j -= 1

    arr[index - 1], arr[j] = arr[j], arr[index - 1]

    j = len(arr) - 1
    while index < j:
        arr[index], arr[j] = arr[j], arr[index]
        index += 1
        j -= 1

    return arr
# Complete the biggerIsGreater function below.


def biggerIsGreater(w):
    res = next_permutation(list(w))
    if not res:
        return "no answer"
    return ''.join(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

