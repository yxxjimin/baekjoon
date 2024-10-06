src, tgt = map(int, input().split())

visited = [False] * 100001
queue = [src]
distance = 0
found = False
while queue:
    for _ in range(len(queue)):
        loc = queue.pop(0)
        
        if loc == tgt:
            found = True
            break
        else:
            next_locs = [loc - 1, loc + 1, loc * 2]
            for next_loc in next_locs:
                if next_loc in range(100001) and not visited[next_loc]:
                    queue.append(next_loc)
                    visited[next_loc] = True
            
    if found:
        break
    else:
        distance += 1

print(distance)
