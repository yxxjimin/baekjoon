import sys

num_solutions = int(input())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()

# Two-pointer
i, j = 0, len(solutions) - 1
min_value = sys.maxsize
alkaline, acid = None, None
while i != j:
    curr_value = solutions[i] + solutions[j]

    if abs(curr_value) < min_value:
        min_value = abs(curr_value)
        alkaline, acid = solutions[i], solutions[j]

    # Decrement j to lower the sum
    if curr_value > 0:
        j -= 1
    # Increment i to raise the sum
    else:
        i += 1
    
print(alkaline, acid)
