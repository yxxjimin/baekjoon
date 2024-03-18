from collections import deque

m, n = map(int, input().split())

boxes = [list(map(int, input().split())) for _ in range(n)]

# Utils
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def get_adjacent_tomatoes(row: int, col: int) -> set:
    tomatoes = set()
    for dx, dy in dir:
        if (row + dy in range(n)
            and col + dx in range(m)
            and boxes[row + dy][col + dx] == 0):
            tomatoes.add((row + dy, col + dx))

    return tomatoes

# Find initial tomatoes
queue = deque()
for r in range(n):
    for c in range(m):
        if boxes[r][c] == 1:
            queue.append((r, c))

# BFS
days = -1
while queue:
    for _ in range(len(queue)):
        row, col = queue.popleft()
        adj_tomatoes = get_adjacent_tomatoes(row, col)
        for new_row, new_col in adj_tomatoes:
            queue.append((new_row, new_col))
            # Mark as visited
            boxes[new_row][new_col] = days + 3
    days += 1
    
# Check if all tomatoes are rotten
valid = True
for row in boxes:
    if 0 in row:
        valid = False
        break

print(days if valid else -1)
