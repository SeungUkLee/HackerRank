#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d = defaultdict(int)
    for m in magazine:
        d[m] += 1

    for n in note:
        if n not in d or d[n] <= 0:
            print("No")
            return
        d[n] -= 1
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

