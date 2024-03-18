from itertools import combinations
import sys

n, m = map(int, input().split())

# Find houses & chickens
houses = []
chickens = []
for r in range(n):
    line = list(map(int, input().split()))
    for c in range(n):
        if line[c] == 1:
            houses.append((r, c))
        elif line[c] == 2:
            chickens.append((r, c))

# Calculate all distances between houses and chickenjib
distance_matrix = []
for house in houses:
    row = []
    for chicken in chickens:
        row.append(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
    distance_matrix.append(row)

# All possible combinations of survived chickenjib
new_combinations = combinations(range(len(chickens)), m)
minimum_distance_sum = sys.maxsize
for comb in new_combinations:
    current_distance_sum = 0
    for house in distance_matrix:
        current_distance_sum += min([house[i] for i in comb])
    if current_distance_sum < minimum_distance_sum:
        minimum_distance_sum = current_distance_sum

print(minimum_distance_sum)
