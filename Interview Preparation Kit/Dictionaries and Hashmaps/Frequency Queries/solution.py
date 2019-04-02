#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
    freq, cnt, ans = defaultdict(int), defaultdict(int), []

    for op, x in queries:
        if op == 1:
            cnt[freq[x]] -= 1
            freq[x] += 1
            cnt[freq[x]] += 1
        elif op == 2:
            if freq[x] > 0:
                cnt[freq[x]] -= 1
                freq[x] -= 1
                cnt[freq[x]] += 1
        elif op == 3:
            if cnt[x] > 0:
                ans.append(1)
            else:
                ans.append(0)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()


