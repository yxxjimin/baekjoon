from collections import deque

num_ladders, num_snakes = map(int, input().split())

# Ladders and Snakes
ladders = dict()
for _ in range(num_ladders):
    start, end = map(int, input().split())
    ladders[start] = end

snakes = dict()
for _ in range(num_snakes):
    start, end = map(int, input().split())
    snakes[start] = end

# BFS
queue = deque()
queue.append(1)
visited = [False] * 101
visited[1] = True
arrived = False
distance = 0
while queue:
    for _ in range(len(queue)):
        curr_loc = queue.popleft()

        # If arrived at 100
        if arrived or curr_loc == 100:
            arrived = True
            break
        
        # Ladders or snakes
        if curr_loc in ladders:
            curr_loc = ladders[curr_loc]
            visited[curr_loc] = True
        elif curr_loc in snakes:
            curr_loc = snakes[curr_loc]
            visited[curr_loc] = True

        # Roll the dice
        for dice in range(1, 7):
            if curr_loc + dice < 100 and not visited[curr_loc + dice]:
                queue.append(curr_loc + dice)
                visited[curr_loc + dice] = True
            # Shortcut
            elif curr_loc + dice == 100:
                queue.appendleft(100)
                arrived = True
                break

    distance += 1
    if arrived:
        break

print(distance)
