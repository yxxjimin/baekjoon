import sys

num_cases = int(sys.stdin.readline())

cache = { 1: 1, 2: 2, 3: 4 }
for i in range(4, 11):
    cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]

answer = []
for _ in range(num_cases):
    num = int(sys.stdin.readline())
    answer.append(cache[num])

print(*answer, sep='\n')
