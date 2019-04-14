#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from collections import defaultdict

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    adj_list, color = defaultdict(list), defaultdict(int)
    visit = [0] * (graph_nodes+1)
    
    for from_node, to_node in zip(graph_from, graph_to):
        adj_list[from_node].append(to_node)
        adj_list[to_node].append(from_node)

    for i, c in enumerate(ids):
        color[i+1] = c
    
    # 찾고자하는 val의 color 와 같은 색깔이 있는지 확인
    val_color = color[val]
    same_color = [id_ for id_ in ids if id_ == val_color]
    
    if len(same_color) <= 1:
        return -1

    L = []
    def dfs(node, d):
        visit[node] = 1
        if d != 0 and color[node] == color[val]:
            L.append(d)
        for nei in adj_list[node]:
            if not visit[nei]:
                dfs(nei, d+1)
    dfs(val, 0)
    
    return min(L)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

