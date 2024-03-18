import sys
from functools import cmp_to_key

num_students = int(input())

scores = []
for _ in range(num_students):
    name, kor, eng, math = sys.stdin.readline().split()
    scores.append([name, int(kor), int(eng), int(math)])

def cmp_score(a, b):
    # Decreasing order of KOR score
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    # Increasing order of ENG score
    elif a[2] < b[2]:
        return -1
    elif a[2] > b[2]:
        return 1
    # Decreasing order of MATH score
    elif a[3] > b[3]:
        return -1
    elif a[3] < b[3]:
        return 1
    # Increasing order of name
    elif a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        return 0
    
scores.sort(key=cmp_to_key(cmp_score))
print(*map(lambda x: x[0], scores), sep='\n')
