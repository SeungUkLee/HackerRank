from collections import Counter

def isValid(s):
    d = Counter(s)
    cmp_v = d[s[0]]
    diff_k = [k for k, v in d.items() if cmp_v != v]

    cond1 = len(diff_k) == 0
    cond2 = len(diff_k) == 1 and (abs(d[diff_k[0]] - cmp_v) == 1 or d[diff_k[0]] == 1)

    if cond1 or cond2:
        return "YES"
    return "NO"

# 기존의 solution.py 코드에서 문제점 발견
# aaabc 인 경우 NO가 나와야되는데 YES 가 나옴
# 그래서 로직 변경

# 기준 값과 값이 다른 키를 찾는다
# 해당 키의 갯수가 여러개이다 -> NO
# 해당 키의 갯수가 1이다 -> 해당 키에 해당하는 값이 1 이거나 기준값과의 차이가 1이면 YES 