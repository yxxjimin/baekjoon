import sys 

n = int(input())

# Counting sort
counts = [0] * 10001
for _ in range(n):
    counts[int(sys.stdin.readline())] += 1

for num in range(10001):
    for _ in range(counts[num]):
        print(num)
