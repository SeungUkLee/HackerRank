#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    strings_map = Counter(strings)
    # res = list()
    # for query in queries:
    #     res.append(strings_map[query]) if query in strings_map else res.append(0)
    # return res
    return [strings_map[query] if query in strings_map else 0 for query in queries]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

