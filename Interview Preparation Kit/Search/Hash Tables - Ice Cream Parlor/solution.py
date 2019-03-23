#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_d = {}
    for i in range(len(cost)):
        target = money - cost[i]
        if target in cost_d:
            print(cost_d[target], i+1)
            break
        cost_d[cost[i]] = i + 1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

